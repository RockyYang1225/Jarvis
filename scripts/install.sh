#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)
      ROOT="$2"
      shift 2
      ;;
    -h|--help)
      cat <<'USAGE'
Usage: scripts/install.sh [--root /path/to/Jarvis]

Installs local Jarvis support files for this checkout.
The installer is idempotent and never deletes local content.
USAGE
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

ROOT="$(cd "$ROOT" && pwd)"

if [[ ! -f "$ROOT/AGENTS.md" || ! -d "$ROOT/90_System" ]]; then
  echo "This does not look like a Jarvis repo root: $ROOT" >&2
  exit 2
fi

standard_dirs=(
  "00_Home"
  "10_Workspace/Active Projects"
  "10_Workspace/Archived Projects"
  "10_Workspace/Incubating Projects"
  "10_Workspace/Paused Projects"
  "20_Career/Interviews"
  "20_Career/Job Market"
  "20_Career/Portfolio"
  "20_Career/Resume"
  "20_Career/Stories"
  "30_Ideas/Categories"
  "30_Ideas/Idea Briefs"
  "30_Ideas/Inbox"
  "30_Ideas/Incubation"
  "30_Ideas/Parked"
  "30_Ideas/Promoted"
  "40_Knowledge/Glossary"
  "40_Knowledge/Notes"
  "40_Knowledge/Patterns"
  "40_Knowledge/Sources"
  "40_Knowledge/Topics"
  "50_Reviews/Daily"
  "50_Reviews/Interview Retros"
  "50_Reviews/Monthly"
  "50_Reviews/Project Retros"
  "50_Reviews/Weekly"
  "90_System/Agents"
  "90_System/Automation"
  "90_System/Indexes"
  "90_System/Prompts"
  "90_System/Rules"
  "90_System/Skills"
  "90_System/Templates"
  "90_System/Tools"
  "90_System/Workflows"
)

for dir in "${standard_dirs[@]}"; do
  mkdir -p "$ROOT/$dir"
  if [[ ! -e "$ROOT/$dir/.gitkeep" ]]; then
    printf 'Keep this standard Jarvis directory in Git.\n' > "$ROOT/$dir/.gitkeep"
  fi
done

skills_source="$ROOT/90_System/Skills"
skills_target="$HOME/.agents/skills"
mkdir -p "$skills_target"

if [[ -d "$skills_source" ]]; then
  for skill_dir in "$skills_source"/*; do
    [[ -d "$skill_dir" ]] || continue
    [[ -f "$skill_dir/SKILL.md" ]] || continue
    skill_name="$(basename "$skill_dir")"
    link_path="$skills_target/$skill_name"

    if [[ -L "$link_path" ]]; then
      current_target="$(readlink "$link_path")"
      if [[ "$current_target" == "$skill_dir" ]]; then
        echo "Skill already linked: $skill_name"
      else
        echo "Skill link exists with a different target, leaving unchanged: $link_path -> $current_target" >&2
      fi
    elif [[ -e "$link_path" ]]; then
      echo "Skill path exists and is not a symlink, leaving unchanged: $link_path" >&2
    else
      ln -s "$skill_dir" "$link_path"
      echo "Linked skill: $skill_name"
    fi
  done
fi

echo "Jarvis install complete"
echo "Repo root: $ROOT"
echo "Skills target: $skills_target"
echo "Open Codex from the Jarvis repo root so AGENTS.md is loaded first."
