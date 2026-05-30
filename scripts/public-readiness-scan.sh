#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

if [[ ! -d "$ROOT" ]]; then
  echo "Jarvis root does not exist: $ROOT" >&2
  exit 2
fi

openai_key_marker='OPENAI_API_''KEY'
personal_email='[A-Za-z0-9._%+-]+@(gmail|icloud|qq|outlook|hotmail)\.[A-Za-z]{2,}'
PATTERN="(AKIA[0-9A-Z]{16}|${openai_key_marker}|s[k]-[A-Za-z0-9_-]{10,}|g[h]p_[A-Za-z0-9_]{20,}|github_p[a]t_[A-Za-z0-9_]+|BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY|password[[:space:]]*[:=]|token[[:space:]]*[:=]|${personal_email})"

SCAN_PATHS=(
  "$ROOT/AGENTS.md"
  "$ROOT/README.md"
  "$ROOT/READMEs"
  "$ROOT/00_Home"
  "$ROOT/30_Ideas"
  "$ROOT/90_System"
  "$ROOT/docs"
  "$ROOT/scripts"
)

existing_paths=()
for path in "${SCAN_PATHS[@]}"; do
  if [[ -e "$path" ]]; then
    existing_paths+=("$path")
  fi
done

if [[ ${#existing_paths[@]} -eq 0 ]]; then
  echo "No public paths found to scan under $ROOT" >&2
  exit 2
fi

if grep -REIn --exclude-dir='.git' --exclude='*.png' --exclude='*.jpg' --exclude='*.jpeg' --exclude='*.webp' --exclude='*.pdf' "$PATTERN" "${existing_paths[@]}"; then
  echo "Public-readiness scan found secret-like content. Review the matches above." >&2
  exit 1
fi

echo "Public-readiness scan passed for $ROOT"
