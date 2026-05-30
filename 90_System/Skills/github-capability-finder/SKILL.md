---
name: github-capability-finder
description: Find GitHub-hosted capability extensions including skills, plugins, MCP servers, agents, agent frameworks, CLIs, workflow templates, integrations, and developer tools by checking a local github-daily-report archive first, then searching GitHub only when local daily picks do not contain a good match. Use when the user asks to find, search, recommend, install, compare, or look up any plugin, skill, agent, MCP tool/server, Codex/Claude/Cursor extension, workflow helper, automation, or GitHub project that extends an AI/developer workflow.
---

# GitHub Capability Finder

## Overview

Use this skill to find GitHub-hosted capability extensions with a local curated GitHub daily report archive as the first search layer. A capability extension can be a skill, plugin, MCP server, agent, agent framework, CLI, workflow template, integration, or developer tool.

Only search public GitHub after checking the local archive.

Canonical local report repo:

```text
~/Workspace/github-daily-report
```

GitHub repo:

```text
RockyYang1225/github-daily-report
```

## Workflow

1. Parse the user's need into 3-8 search terms.
   - Include Chinese and English terms when useful.
   - Include ecosystem terms such as `skill`, `plugin`, `agent`, `mcp`, `server`, `extension`, `workflow`, `automation`, `cli`, `tool`, `framework`, `codex`, `claude`, `cursor` when relevant.
2. Search local daily reports first:

```bash
rtk python3 90_System/Skills/github-capability-finder/scripts/search_daily_reports.py "<query>"
```

3. If local matches are relevant, inspect the linked GitHub repos or report snippets before recommending.
4. If local matches are weak or empty, search GitHub directly.
   - Prefer `gh search repos "<query>" --limit 10 --json fullName,description,url,stargazersCount,updatedAt,language`
   - If `gh` is unavailable or insufficient, use web search restricted to GitHub when possible.
5. Evaluate candidates before recommending.
6. Present 2-5 options, clearly separating:
   - Personal daily report matches
   - Fresh GitHub search matches
   - Best recommendation
   - Install or trial command, if known

## Local Search Rules

Always search the report archive before external GitHub search unless the user explicitly says not to.

Use multiple local searches when the first query is too narrow:

```bash
rtk python3 90_System/Skills/github-capability-finder/scripts/search_daily_reports.py "react testing skill plugin"
rtk python3 90_System/Skills/github-capability-finder/scripts/search_daily_reports.py "playwright browser automation agent plugin mcp"
rtk python3 90_System/Skills/github-capability-finder/scripts/search_daily_reports.py "claude codex extension workflow tool"
```

If the local repo is missing, try the canonical Workspace path first, then tell the user if it needs to be cloned.

Do not treat a daily report mention as enough evidence. Open the repo README or official docs when recommending installation or adoption.

## Capability Types

Consider all of these in scope:

- Agent skills
- Codex / Claude Code / Cursor / Gemini skills
- Plugins and extensions
- MCP servers and MCP management tools
- Agent frameworks and multi-agent platforms
- CLI tools that improve AI/developer workflows
- Workflow templates and prompt packs
- Automation helpers
- Browser, IDE, terminal, GitHub, testing, deployment, documentation, and code-review integrations

## Candidate Evaluation

Check:

- Fit to the user's exact task
- Source reputation
- GitHub stars and recent activity
- README quality and install instructions
- Compatibility with Codex, Claude Code, Cursor, MCP, or the user's stack
- Maintenance risk and security sensitivity

Prefer official or widely used sources for plugins, MCP servers, and developer extensions.

## Output Format

Respond in Chinese by default.

Use this structure:

```markdown
我先查了你的 github-daily-report：

1. ...

如果本地日报没有合适结果，我又查了 GitHub：

1. ...

我的建议：
...

安装 / 试用：
...
```

If no good candidate exists, say so and suggest whether to create a custom skill instead.

## Boundaries

- Do not install plugins or skills without user confirmation.
- Do not recommend a repo solely because it matched keywords.
- Do not skip the personal daily report archive unless explicitly requested.
- If current information matters, verify fresh GitHub data before final recommendation.
