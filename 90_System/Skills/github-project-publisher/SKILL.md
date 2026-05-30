---
name: github-project-publisher
description: Prepare and publish local projects or existing repositories to GitHub or a remote git repository using GitHub CLI and git, including repo creation, remote setup, push, release creation, and optional GitHub Pages publishing. Use when the user asks to publish to a remote git repo, 发布到远程 git 仓库, push to remote, create a GitHub repo, publish a project to GitHub, connect a local project to a GitHub repository, create a GitHub release, publish GitHub Pages, or prepare a repo for public sharing.
---

# GitHub Project Publisher

Use this skill to safely publish a local project or existing repository to GitHub or a remote git repository.

## Quick Start

1. Clarify the user's intent:
   - Create a new GitHub repository
   - Connect local project to an existing GitHub repository
   - Publish to a remote git repository
   - 发布到远程 git 仓库
   - Push current project to GitHub
   - Create a GitHub Release
   - Enable or update GitHub Pages
   - Prepare a repo for public sharing
2. Inspect current publish state:

```bash
rtk python3 90_System/Skills/github-project-publisher/scripts/inspect_github_publish_state.py <repo>
```

3. Read the relevant references:
   - For the end-to-end flow, read [references/publish-flow.md](references/publish-flow.md).
   - For `gh` commands, read [references/github-cli.md](references/github-cli.md).
   - For releases and tags, read [references/release-checklist.md](references/release-checklist.md).
   - For GitHub Pages, read [references/pages-publishing.md](references/pages-publishing.md).
   - For secrets, destructive actions, and confirmation boundaries, read [references/safety-rules.md](references/safety-rules.md).
4. Before any write operation to GitHub, summarize the planned action and ask for confirmation.
5. Execute using `gh` CLI and `git` when confirmed.
6. Verify the result with read-only commands and return the GitHub URLs.

## Required Safety Rules

- Do not publish, push, create a public repo, create a release, enable Pages, or change remotes without explicit user confirmation.
- Do not delete branches, tags, releases, remotes, or repositories unless the user explicitly asks and reconfirms.
- If secrets, `.env`, private configs, credentials, or suspicious tokens are detected, stop and report the risk before publishing.
- If `gh auth status` fails, ask the user to authenticate with GitHub CLI.
- Preserve existing user changes; do not rewrite history unless the user explicitly requests it.

## Output

When finished, report:

- Repository URL
- Default branch
- Push result
- Release URL, if created
- Pages URL, if enabled
- Safety checks performed
- Any blocked or manual follow-up items
