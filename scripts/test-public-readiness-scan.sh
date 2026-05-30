#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCAN_SCRIPT="$SCRIPT_DIR/public-readiness-scan.sh"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

mkdir -p "$TMP_DIR/90_System" "$TMP_DIR/10_Workspace/Active Projects"

cat > "$TMP_DIR/90_System/Public.md" <<'SCAN_OK'
# Public

This file is safe.
SCAN_OK

cat > "$TMP_DIR/10_Workspace/Active Projects/Private.md" <<'SCAN_IGNORED'
email@example.com
SCAN_IGNORED

"$SCAN_SCRIPT" "$TMP_DIR"

printf 'OPENAI_API_%s=s%s\n' "KEY" "k-test-value" > "$TMP_DIR/90_System/Secret.md"

if "$SCAN_SCRIPT" "$TMP_DIR" >/tmp/jarvis-scan-test.log 2>&1; then
  echo "Expected public-readiness scan to fail for secret-like content" >&2
  exit 1
fi

grep -q "Secret.md" /tmp/jarvis-scan-test.log
