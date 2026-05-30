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
