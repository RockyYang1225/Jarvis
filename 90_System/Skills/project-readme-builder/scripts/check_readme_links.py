#!/usr/bin/env python3
"""Check local Markdown links and image paths in README files."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


INLINE_LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
REF_DEF_RE = re.compile(r"^\s*\[([^\]]+)\]:\s*(\S+)", re.MULTILINE)


def is_external(target: str) -> bool:
    parsed = urlparse(target)
    return parsed.scheme in {"http", "https", "mailto", "tel"}


def is_anchor_only(target: str) -> bool:
    return target.startswith("#")


def strip_fragment(target: str) -> str:
    return target.split("#", 1)[0]


def normalize_target(target: str) -> str:
    target = target.strip().strip("<>")
    return unquote(strip_fragment(target))


def check_target(readme_path: Path, target: str) -> tuple[bool, str]:
    if is_external(target) or is_anchor_only(target):
        return True, "skipped"

    normalized = normalize_target(target)
    if not normalized:
        return True, "anchor"

    target_path = (readme_path.parent / normalized).resolve()
    if target_path.exists():
        return True, "exists"

    return False, str(target_path)


def collect_links(markdown: str) -> list[tuple[str, str, str]]:
    links: list[tuple[str, str, str]] = []

    for match in INLINE_LINK_RE.finditer(markdown):
        kind = "image" if match.group(1) == "!" else "link"
        label = match.group(2)
        target = match.group(3)
        links.append((kind, label, target))

    for match in REF_DEF_RE.finditer(markdown):
        label = match.group(1)
        target = match.group(2)
        links.append(("reference", label, target))

    return links


def main() -> int:
    parser = argparse.ArgumentParser(description="Check local README links and image paths.")
    parser.add_argument("repo", help="Repository root")
    parser.add_argument("readme", nargs="?", default="README.md", help="README path relative to repo")
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    readme_path = (repo / args.readme).resolve()

    if not repo.exists():
        print(f"Repo does not exist: {repo}", file=sys.stderr)
        return 2

    try:
        readme_path.relative_to(repo)
    except ValueError:
        print(f"README must be inside repo: {readme_path}", file=sys.stderr)
        return 2

    if not readme_path.exists():
        print(f"README does not exist: {readme_path}", file=sys.stderr)
        return 2

    markdown = readme_path.read_text(encoding="utf-8")
    links = collect_links(markdown)
    failures: list[tuple[str, str, str, str]] = []
    checked = 0

    for kind, label, target in links:
        ok, detail = check_target(readme_path, target)
        if detail not in {"skipped", "anchor"}:
            checked += 1
        if not ok:
            failures.append((kind, label, target, detail))

    print(f"README: {os.path.relpath(readme_path, repo)}")
    print(f"Links found: {len(links)}")
    print(f"Local targets checked: {checked}")

    if failures:
        print(f"Broken local targets: {len(failures)}")
        for kind, label, target, detail in failures:
            label_display = label or "(empty label)"
            print(f"- {kind}: {label_display} -> {target}")
            print(f"  missing: {detail}")
        return 1

    print("Broken local targets: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
