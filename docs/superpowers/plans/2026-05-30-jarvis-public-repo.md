# Jarvis Public Repo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the existing `<jarvis-root>` directory into a maintainable public GitHub-ready Jarvis template repo with installable skills and documented public/private boundaries.

**Architecture:** Keep `<jarvis-root>` as the single source of truth. Add repo infrastructure around the current Markdown vault: conservative ignore rules, an idempotent installer, smoke tests, and public documentation. The installer links skills from `90_System/Skills` into `~/.agents/skills` without deleting or overwriting unrelated local files.

**Tech Stack:** Markdown, Bash, Git, symlinks, Codex/Jarvis workflow docs.

---

### Task 1: Initialize Git Boundary And Safety Checks

**Files:**
- Create: `<jarvis-root>/.gitignore`
- Create: `<jarvis-root>/scripts/public-readiness-scan.sh`
- Create: `<jarvis-root>/scripts/test-public-readiness-scan.sh`

- [ ] **Step 1: Initialize Git if needed**

Run:

```bash
rtk git rev-parse --show-toplevel || rtk git init -b main
```

Expected: either prints the repo root or initializes an empty Git repo on `main`.

- [ ] **Step 2: Write the public-readiness scan test**

Create `<jarvis-root>/scripts/test-public-readiness-scan.sh`:

```bash
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
```

- [ ] **Step 3: Run the scan test and confirm it fails before implementation**

Run:

```bash
rtk bash scripts/test-public-readiness-scan.sh
```

Expected: FAIL because `scripts/public-readiness-scan.sh` does not exist yet.

- [ ] **Step 4: Add `.gitignore`**

Create `<jarvis-root>/.gitignore` with conservative public/private defaults:

```gitignore
# OS and editor noise
.DS_Store
Thumbs.db
.idea/
.vscode/
*.swp
*.swo

# Local environment and runtime output
.env
.env.*
*.log
*.tmp
tmp/
temp/
cache/
exports/
dist/
build/
.obsidian/

# Keep project indexes, ignore real project cards by default.
/10_Workspace/Active Projects/*
!/10_Workspace/Active Projects/Active Projects.md
!/10_Workspace/Active Projects/.gitkeep
/10_Workspace/Archived Projects/*
!/10_Workspace/Archived Projects/Archived Projects.md
!/10_Workspace/Archived Projects/.gitkeep
/10_Workspace/Incubating Projects/*
!/10_Workspace/Incubating Projects/Incubating Projects.md
!/10_Workspace/Incubating Projects/.gitkeep
/10_Workspace/Paused Projects/*
!/10_Workspace/Paused Projects/Paused Projects.md
!/10_Workspace/Paused Projects/.gitkeep

# Career content is local by default; keep only section indexes.
/20_Career/Interviews/*
!/20_Career/Interviews/Interviews.md
!/20_Career/Interviews/.gitkeep
/20_Career/Job Market/*
!/20_Career/Job Market/Job Market.md
!/20_Career/Job Market/.gitkeep
/20_Career/Portfolio/*
!/20_Career/Portfolio/Portfolio.md
!/20_Career/Portfolio/.gitkeep
/20_Career/Resume/*
!/20_Career/Resume/Resume.md
!/20_Career/Resume/.gitkeep
/20_Career/Stories/*
!/20_Career/Stories/Stories.md
!/20_Career/Stories/.gitkeep

# Reviews are local by default; keep only section indexes.
/50_Reviews/Daily/*
!/50_Reviews/Daily/Daily.md
!/50_Reviews/Daily/.gitkeep
/50_Reviews/Weekly/*
!/50_Reviews/Weekly/Weekly.md
!/50_Reviews/Weekly/.gitkeep
/50_Reviews/Monthly/*
!/50_Reviews/Monthly/Monthly.md
!/50_Reviews/Monthly/.gitkeep
/50_Reviews/Project Retros/*
!/50_Reviews/Project Retros/Project Retros.md
!/50_Reviews/Project Retros/.gitkeep
/50_Reviews/Interview Retros/*
!/50_Reviews/Interview Retros/Interview Retros.md
!/50_Reviews/Interview Retros/.gitkeep

# Private knowledge notes are local unless explicitly promoted to reusable system knowledge.
/40_Knowledge/Notes/*
!/40_Knowledge/Notes/Notes.md
!/40_Knowledge/Notes/.gitkeep
/40_Knowledge/Sources/*
!/40_Knowledge/Sources/Sources.md
!/40_Knowledge/Sources/.gitkeep

# Preserve standard empty directories.
!.gitkeep
```

- [ ] **Step 5: Implement public-readiness scan**

Create `<jarvis-root>/scripts/public-readiness-scan.sh`:

```bash
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
```

- [ ] **Step 6: Make scripts executable and run the scan test**

Run:

```bash
rtk chmod +x scripts/public-readiness-scan.sh scripts/test-public-readiness-scan.sh
rtk bash scripts/test-public-readiness-scan.sh
```

Expected: PASS with no output from the test script.

### Task 2: Add Installer And Smoke Test

**Files:**
- Create: `<jarvis-root>/scripts/install.sh`
- Create: `<jarvis-root>/scripts/test-install.sh`

- [ ] **Step 1: Write the installer smoke test**

Create `<jarvis-root>/scripts/test-install.sh`:

```bash
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
```

- [ ] **Step 2: Run the installer test and confirm it fails before implementation**

Run:

```bash
rtk bash scripts/test-install.sh
```

Expected: FAIL because `scripts/install.sh` does not exist yet.

- [ ] **Step 3: Implement installer**

Create `<jarvis-root>/scripts/install.sh`:

```bash
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
```

- [ ] **Step 4: Make installer executable and run smoke test**

Run:

```bash
rtk chmod +x scripts/install.sh scripts/test-install.sh
rtk bash scripts/test-install.sh
```

Expected: PASS with no output from the test script.

### Task 3: Add Public Documentation

**Files:**
- Create: `<jarvis-root>/README.md`

- [ ] **Step 1: Add README**

Create `<jarvis-root>/README.md`:

```markdown
# Jarvis

Jarvis is a Markdown-based personal work system for Codex-assisted thinking, project routing, workflows, agents, templates, skills, knowledge capture, and review loops.

It is designed to be cloned as a reusable operating system for personal work. The repo contains the system skeleton and reusable capabilities; private project state and personal notes should stay local unless you intentionally publish sanitized examples.

## What Jarvis Manages

- Home dashboard and session guide
- Workspace/project indexes
- Idea capture and classification
- Knowledge indexes
- Review indexes
- System rules, templates, prompts, workflows, agents, and skills

Jarvis is not where real application source code lives. Project source code should live in a separate workspace such as `~/Workspace/<repo>`.

## Quick Start

```bash
git clone <your-jarvis-repo-url> Jarvis
cd Jarvis
./scripts/install.sh
```

Then open Codex from the Jarvis repo root so `AGENTS.md` is loaded first.

## Installation

The installer is safe to run repeatedly:

```bash
./scripts/install.sh
```

It will:

- create standard Jarvis directories when missing
- preserve existing local content
- add `.gitkeep` placeholders for empty standard directories
- link skills from `90_System/Skills` into `~/.agents/skills`

It will not delete files or overwrite unrelated local skill directories.

## Public And Local Boundaries

Good candidates for Git:

- `AGENTS.md`
- `README.md`
- `00_Home/` generic operating guides
- `30_Ideas/` category and workflow indexes
- `90_System/` agents, workflows, templates, prompts, rules, tools, and skills
- top-level layer index files
- sanitized examples and templates

Keep local by default:

- real active project cards
- resumes and interview notes
- private knowledge notes
- daily, weekly, monthly, and project retros
- secrets, tokens, local automation state, exports, caches, and logs

Run the public-readiness scan before publishing:

```bash
./scripts/public-readiness-scan.sh
```

## Directory Map

```text
00_Home/       Dashboard, current focus, operating guide
10_Workspace/  Project indexes and project cards, not source code
20_Career/     Resume, interview, and portfolio assets
30_Ideas/      Idea inbox, briefs, categories, incubation
40_Knowledge/  Stable reusable knowledge indexes and notes
50_Reviews/    Daily, weekly, monthly, project, and interview reviews
90_System/     Jarvis rules, templates, agents, workflows, prompts, skills
docs/          Design docs, implementation plans, and project notes
scripts/       Installers, checks, and maintenance helpers
```

## Using With Codex

Start Codex from the Jarvis root. The top-level `AGENTS.md` tells Codex how to route work:

- project code belongs in `~/Workspace/<repo>`
- Jarvis stores thinking, indexing, reusable knowledge, workflows, prompts, templates, and skills
- long-term knowledge writes should be confirmed before they are committed
- user-facing Jarvis notes are Chinese by default

## Adding Skills

Put repo-owned skills under:

```text
90_System/Skills/<skill-name>/SKILL.md
```

Run:

```bash
./scripts/install.sh
```

The installer links each skill into:

```text
~/.agents/skills/<skill-name>
```

## Adding Workflows, Agents, And Templates

Use these system folders:

- `90_System/Workflows/`
- `90_System/Agents/`
- `90_System/Templates/`
- `90_System/Prompts/`
- `90_System/Rules/`
- `90_System/Tools/`

Update the corresponding registry or index when adding a new reusable capability.

## Publishing Checklist

Before making the repo public:

```bash
./scripts/public-readiness-scan.sh
git status --short
```

Review the changed and tracked file list. Do not publish private project cards, resumes, interview notes, secrets, or personal retros unless they have been intentionally sanitized.
```

- [ ] **Step 2: Verify README command references exist**

Run:

```bash
rtk proxy /bin/test -x scripts/install.sh
rtk proxy /bin/test -x scripts/public-readiness-scan.sh
```

Expected: both commands exit 0.

### Task 4: Add Directory Placeholders And Run Installer

**Files:**
- Create: `.gitkeep` files in standard Jarvis directories where needed

- [ ] **Step 1: Run installer on the real checkout**

Run:

```bash
rtk ./scripts/install.sh
```

Expected: prints linked or existing skills, then `Jarvis install complete`.

- [ ] **Step 2: Verify standard directories exist**

Run:

```bash
rtk test -d 90_System/Skills
rtk test -d 10_Workspace/Active\\ Projects
rtk test -d 50_Reviews/Weekly
```

Expected: all commands exit 0.

### Task 5: Verify Public Repo State And Create Development Handoff

**Files:**
- Create: `<jarvis-root>/reviews/acceptance/2026-05-30-jarvis-public-repo-acceptance.md` if the public setup is accepted

- [ ] **Step 1: Run all verification commands**

Run:

```bash
rtk bash scripts/test-public-readiness-scan.sh
rtk bash scripts/test-install.sh
rtk ./scripts/public-readiness-scan.sh
rtk git status --short
```

Expected: tests pass, scan passes, and status does not show private runtime content that should be committed.

- [ ] **Step 2: Inspect Git ignored files**

Run:

```bash
rtk git status --short --ignored
```

Expected: ignored real project cards and private review files appear as ignored, while system files, scripts, README, and indexes are visible for tracking.

- [ ] **Step 3: Create acceptance report**

Create `<jarvis-root>/reviews/acceptance/2026-05-30-jarvis-public-repo-acceptance.md` with:

```markdown
# Jarvis Public Repo Acceptance

项目：Jarvis
任务：现有 Jarvis 目录公开 repo 化
版本类型：小改动
验收日期：2026-05-30
验收 Agent：Codex
结论：通过

## 产品验收

- 产品目标：Jarvis 可以作为公开 GitHub 项目维护，同时保留本机作为唯一维护源。
- 核心用户流程：clone repo 后运行 `./scripts/install.sh`，获得标准目录和 repo-owned skills 链接。
- 体验与文案：README 覆盖快速开始、安装、Codex 使用、公开/本地边界、skills/workflows 维护。
- 边界情况：安装脚本重复运行安全；已有 skill 链接或非 symlink 路径不会被覆盖。

## 测试验收

- 已运行验证：`scripts/test-public-readiness-scan.sh`、`scripts/test-install.sh`、`scripts/public-readiness-scan.sh`、`git status --short --ignored`。
- 未覆盖范围：未实际 push 到 GitHub；远端创建和 GitHub 可见性设置需要人工确认。
- 失败或异常：无。
- 证据位置：本报告和命令输出。

## 证据

- 命令：见开发交接摘要。
- 截图：无。
- 日志：无持久日志。
- 文档：`README.md`、`docs/superpowers/specs/2026-05-30-jarvis-public-repo-design.md`、`docs/superpowers/plans/2026-05-30-jarvis-public-repo.md`。

## 缺口

- GitHub remote 尚未创建。
- 首次公开前仍建议人工 review `git status --short` 和 staged 文件列表。

## 风险

- 后续新增个人内容时可能误提交，需要继续依赖 `.gitignore` 和公开前扫描。

## 下一步

- 人工确认 GitHub repo 名称和可见性。
- 创建 remote 后执行首次 push。
```

- [ ] **Step 4: Stage only safe public files and commit**

Run:

```bash
rtk git add AGENTS.md README.md .gitignore 00_Home 10_Workspace/Projects.md 10_Workspace/*/*.md 20_Career/Career.md 20_Career/*/*.md 30_Ideas 40_Knowledge/Knowledge.md 40_Knowledge/Glossary 40_Knowledge/Patterns 40_Knowledge/Topics 50_Reviews/Reviews.md 50_Reviews/*/*.md 90_System docs scripts reviews/acceptance
rtk git status --short
```

Expected: staged files do not include ignored private project cards, private review files, secrets, caches, or logs.

If the staged list is safe, run:

```bash
rtk git commit -m "chore: prepare Jarvis public repo"
```

Expected: commit succeeds. If Git identity is missing, stop and report the exact Git error.
