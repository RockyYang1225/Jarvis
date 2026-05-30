#!/usr/bin/env python3
"""Inspect local repository state before GitHub publishing."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


SENSITIVE_FILE_PATTERNS = [
    ".env",
    ".env.local",
    ".env.production",
    ".npmrc",
    ".pypirc",
    "id_rsa",
    "id_ed25519",
    "credentials.json",
    "service-account.json",
    "service_account.json",
    "firebase-adminsdk",
]

SECRET_VALUE_RE = re.compile(
    r"(api[_-]?key|secret|token|password|private[_-]?key|access[_-]?key)\s*[:=]",
    re.IGNORECASE,
)
GH_TOKEN_LINE_RE = re.compile(r"^(\s*-\s*T" r"oken:\s*).*$", re.MULTILINE)

TEXT_SUFFIXES = {
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".py",
    ".go",
    ".rs",
    ".java",
    ".rb",
    ".php",
    ".md",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".ini",
    ".conf",
    ".env",
    ".sh",
}


def run(repo: Path, *cmd: str) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            cmd,
            cwd=repo,
            text=True,
            capture_output=True,
            timeout=10,
            check=False,
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 127, "", str(exc)


def sanitize_cli_output(text: str) -> str:
    return GH_TOKEN_LINE_RE.sub(r"\1[redacted]", text)


def find_files(repo: Path, names: set[str]) -> list[str]:
    matches: list[str] = []
    for name in names:
        path = repo / name
        if path.exists():
            matches.append(name)
    return sorted(matches)


def detect_sensitive_files(repo: Path) -> list[str]:
    findings: list[str] = []
    ignored_dirs = {".git", "node_modules", ".next", "dist", "build", ".venv", "venv"}

    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        root_path = Path(root)
        for filename in files:
            lowered = filename.lower()
            rel = str((root_path / filename).relative_to(repo))
            if any(pattern in lowered for pattern in SENSITIVE_FILE_PATTERNS):
                findings.append(rel)

    return sorted(set(findings))


def scan_secret_patterns(repo: Path, limit: int = 20) -> list[str]:
    findings: list[str] = []
    ignored_dirs = {".git", "node_modules", ".next", "dist", "build", ".venv", "venv"}

    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        root_path = Path(root)
        for filename in files:
            path = root_path / filename
            if path.suffix.lower() not in TEXT_SUFFIXES and not filename.startswith(".env"):
                continue
            rel = str(path.relative_to(repo))
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if SECRET_VALUE_RE.search(text):
                findings.append(rel)
                if len(findings) >= limit:
                    return sorted(set(findings))

    return sorted(set(findings))


def detect_package_manager(repo: Path) -> str | None:
    if (repo / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (repo / "yarn.lock").exists():
        return "yarn"
    if (repo / "package-lock.json").exists():
        return "npm"
    if (repo / "uv.lock").exists():
        return "uv"
    if (repo / "poetry.lock").exists():
        return "poetry"
    return None


def read_package_scripts(repo: Path) -> dict[str, str]:
    package_json = repo / "package.json"
    if not package_json.exists():
        return {}
    try:
        data = json.loads(package_json.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    scripts = data.get("scripts")
    return scripts if isinstance(scripts, dict) else {}


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect repo before GitHub publishing.")
    parser.add_argument("repo", help="Repository root")
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    if not repo.exists() or not repo.is_dir():
        print(f"Repo directory does not exist: {repo}", file=sys.stderr)
        return 2

    result: dict[str, object] = {"repo": str(repo)}

    code, out, err = run(repo, "git", "rev-parse", "--is-inside-work-tree")
    is_git_repo = code == 0 and out == "true"
    result["is_git_repo"] = is_git_repo

    if is_git_repo:
        result["branch"] = run(repo, "git", "branch", "--show-current")[1]
        result["status_short"] = run(repo, "git", "status", "--short")[1].splitlines()
        result["remotes"] = run(repo, "git", "remote", "-v")[1].splitlines()
    else:
        result["branch"] = None
        result["status_short"] = []
        result["remotes"] = []

    result["gh_available"] = shutil.which("gh") is not None
    if result["gh_available"]:
        code, out, err = run(repo, "gh", "auth", "status")
        result["gh_auth_ok"] = code == 0
        result["gh_auth_message"] = sanitize_cli_output(out or err)
    else:
        result["gh_auth_ok"] = False
        result["gh_auth_message"] = "gh CLI not found"

    result["important_files"] = find_files(
        repo,
        {
            "README.md",
            "LICENSE",
            "LICENSE.md",
            ".gitignore",
            ".env.example",
            "package.json",
            "pyproject.toml",
            "Dockerfile",
            "docker-compose.yml",
        },
    )
    result["package_manager"] = detect_package_manager(repo)
    result["package_scripts"] = read_package_scripts(repo)
    result["sensitive_file_candidates"] = detect_sensitive_files(repo)
    result["secret_pattern_candidates"] = scan_secret_patterns(repo)

    blockers: list[str] = []
    warnings: list[str] = []

    if not is_git_repo:
        blockers.append("Not a git repository.")
    if result["gh_available"] is False:
        blockers.append("GitHub CLI is not installed or not on PATH.")
    elif result["gh_auth_ok"] is False:
        blockers.append("GitHub CLI is not authenticated.")
    if result["sensitive_file_candidates"]:
        blockers.append("Potential sensitive files detected.")
    if result["secret_pattern_candidates"]:
        blockers.append("Potential secret-like assignments detected.")
    if "README.md" not in result["important_files"]:
        warnings.append("README.md is missing.")
    if not any(name in result["important_files"] for name in ("LICENSE", "LICENSE.md")):
        warnings.append("LICENSE is missing.")
    if ".gitignore" not in result["important_files"]:
        warnings.append(".gitignore is missing.")
    if result["status_short"]:
        warnings.append("Working tree has uncommitted changes.")

    result["blockers"] = blockers
    result["warnings"] = warnings

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())
