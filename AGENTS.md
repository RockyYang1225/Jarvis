# Jarvis Session Guide

This directory is a Jarvis top-level personal work system. When a Codex session starts from the Jarvis repo root, use this file as the first routing guide.

Also follow `/Users/rockyyang/.codex/RTK.md`: prefix shell commands with `rtk` unless a raw command is explicitly required through `rtk proxy`.

## Start Here

Read these files before making structural decisions:

- `00_Home/Jarvis Guide.md`
- `00_Home/Dashboard.md`
- `90_System/System.md`
- `90_System/Indexes/Layer Index.md`
- `90_System/Indexes/Jarvis Session Index.md`
- `90_System/Tools/Tools.md`

For agent and workflow work, also read:

- `90_System/Agents/Agent Registry.md`
- `90_System/Agents/Workflow Registry.md`
- `90_System/Agents/Repo Agent Index.md`

## Layer Responsibilities

| Layer | Purpose | Main path |
|---|---|---|
| Home | Dashboard, current focus, operating guide | `00_Home/` |
| Workspace Index | Project cards and project status, not source code | `10_Workspace/` |
| Career | Resume, interview, portfolio assets | `20_Career/` |
| Ideas | Raw ideas, idea briefs, incubation | `30_Ideas/` |
| Knowledge | Stable reusable knowledge | `40_Knowledge/` |
| Reviews | Daily, weekly, project, interview retros | `50_Reviews/` |
| System | Jarvis rules, templates, agents, workflows, prompts | `90_System/` |
| Code Repos | Actual project source code | `~/Workspace/<repo>/` |

Every layer must have a stable index file. The canonical map is `90_System/Indexes/Layer Index.md`.

## Routing Rules

- If the user asks to edit code, work in the real repo under `~/Workspace/<repo>`, not inside Jarvis.
- If the user asks about project status, start from `10_Workspace/Active Projects/`, then follow the repo's `docs/project-home.md`.
- If the user shares a new idea, classify it first with `90_System/Workflows/Classify New Idea.md`; do not assume it is a code project.
- If the user wants to turn an idea into an executable project, use `90_System/Workflows/Idea to Project.md`.
- If the user wants continuous development plus acceptance, use `90_System/Workflows/Project Development Acceptance.md`.
- If the user asks about agents, start from `90_System/Agents/Agent Registry.md`.
- If the user asks about workflows, start from `90_System/Agents/Workflow Registry.md`.
- If the user asks what tools are available, start from `90_System/Tools/Tools.md` and then verify the current session's actual tool list.
- If the user asks to preserve knowledge, prepare a draft first. Do not write long-term Jarvis knowledge without confirmation.
- If creating a new Jarvis directory or layer, create or update that layer's index and update `90_System/Indexes/Layer Index.md`.

## Project Repo Entry

When entering a project repo:

1. Read the repo `AGENTS.md`.
2. Read the repo `agents/README.md`.
3. Read `docs/project-home.md`.
4. Follow repo-local docs in `docs/`, `tasks/`, `decisions/`, `knowledge/`, and `reviews/`.
5. At the end of a meaningful coding session, ask:

```text
本次会话可能产生了值得沉淀的知识，要我准备一份知识沉淀草稿吗？
```

## Boundaries

- Jarvis stores the system of record for thinking, indexing, workflows, and reusable knowledge.
- `~/Workspace` stores real project source code.
- Repo-owned custom skills live under `90_System/Skills`; discovery paths under `~/.agents/skills` should be symlinks when needed.
- Do not move project repos into Jarvis.
- Do not silently archive, delete, rename, or rewrite long-term Jarvis files.
- Do not send emails automatically unless an explicit email automation has been connected and the user confirms.
- User-facing Jarvis notes should be Chinese by default.
- Agent prompts and execution rules may be English when that makes execution clearer.
