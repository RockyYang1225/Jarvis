#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_HOME="$(mktemp -d)"
trap 'rm -rf "$TMP_HOME"' EXIT

HOME="$TMP_HOME" "$ROOT/scripts/install.sh" --root "$ROOT"

test -d "$ROOT/00_Home"
test -d "$ROOT/90_System/Skills"
test -d "$TMP_HOME/.agents/skills"

for skill_dir in "$ROOT"/90_System/Skills/*; do
  [[ -d "$skill_dir" ]] || continue
  [[ -f "$skill_dir/SKILL.md" ]] || continue
  skill_name="$(basename "$skill_dir")"
  link_path="$TMP_HOME/.agents/skills/$skill_name"
  test -L "$link_path"
  test "$(readlink "$link_path")" = "$skill_dir"
done

HOME="$TMP_HOME" "$ROOT/scripts/install.sh" --root "$ROOT" >/tmp/jarvis-install-test.log
grep -q "Jarvis install complete" /tmp/jarvis-install-test.log
