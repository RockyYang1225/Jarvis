#!/usr/bin/env python3
"""Validate a JSON email payload before draft handoff or sending."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
SECRET_RE = re.compile(
    r"(api[_-]?key|secret|token|password|private[_-]?key|access[_-]?key|BEGIN\s+(RSA|OPENSSH|PRIVATE)\s+KEY)",
    re.IGNORECASE,
)


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    return [str(value)]


def validate_addresses(field: str, payload: dict[str, Any], errors: list[str]) -> None:
    for address in as_list(payload.get(field)):
        if not EMAIL_RE.match(address.strip()):
            errors.append(f"Invalid {field} address: {address}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate email payload JSON.")
    parser.add_argument("payload", help="Path to JSON payload")
    parser.add_argument(
        "--self-only",
        action="store_true",
        help="Require every recipient to be in the owner/self allowlist.",
    )
    parser.add_argument(
        "--allowed-recipient",
        action="append",
        default=[],
        help="Allowlisted owner/self recipient. Can be passed multiple times.",
    )
    args = parser.parse_args()

    payload_path = Path(args.payload).expanduser().resolve()
    if not payload_path.exists():
        print(f"Payload does not exist: {payload_path}", file=sys.stderr)
        return 2

    try:
        payload = json.loads(payload_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"Could not read payload JSON: {exc}", file=sys.stderr)
        return 2

    if not isinstance(payload, dict):
        print("Payload must be a JSON object.", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    to_list = as_list(payload.get("to"))
    if not to_list:
        errors.append("Missing required field: to")
    validate_addresses("to", payload, errors)
    validate_addresses("cc", payload, errors)
    validate_addresses("bcc", payload, errors)

    if args.self_only:
        allowed = {item.strip().lower() for item in args.allowed_recipient if item.strip()}
        if not allowed:
            errors.append("--self-only requires at least one --allowed-recipient.")
        all_recipients = to_list + as_list(payload.get("cc")) + as_list(payload.get("bcc"))
        for address in all_recipients:
            if address.strip().lower() not in allowed:
                errors.append(f"Recipient is not in self-email allowlist: {address}")

    subject = str(payload.get("subject") or "").strip()
    body = str(payload.get("body") or "").strip()
    if not subject:
        errors.append("Missing required field: subject")
    if not body:
        errors.append("Missing required field: body")

    combined_text = "\n".join([subject, body])
    if SECRET_RE.search(combined_text):
        errors.append("Potential secret-like text detected in subject/body.")

    attachments = as_list(payload.get("attachments"))
    for attachment in attachments:
        path = Path(attachment).expanduser()
        if not path.exists():
            errors.append(f"Attachment does not exist: {attachment}")
        elif path.is_dir():
            errors.append(f"Attachment is a directory, not a file: {attachment}")

    if len(to_list) + len(as_list(payload.get("cc"))) + len(as_list(payload.get("bcc"))) > 10:
        warnings.append("Large recipient list. Reconfirm before sending.")

    print("Email payload validation")
    print(f"To: {len(to_list)}")
    print(f"Cc: {len(as_list(payload.get('cc')))}")
    print(f"Bcc: {len(as_list(payload.get('bcc')))}")
    print(f"Attachments: {len(attachments)}")
    if args.self_only:
        print("Mode: self-only")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Result: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
