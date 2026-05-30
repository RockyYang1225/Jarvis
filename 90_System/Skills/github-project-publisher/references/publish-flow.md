# Publish Flow

Use this flow for local projects and existing repositories.

## 1. Identify Intent

Ask or infer whether the user wants:

- New GitHub repo from local project
- Existing GitHub repo connected as remote
- Push existing local git repo
- Create release only
- Publish static site through GitHub Pages
- Prepare public repo without publishing yet

If "GitHub Project" could mean a GitHub Projects board, clarify before acting. This skill focuses on repositories and releases unless the user explicitly asks for a Projects board.

## 2. Inspect State

Run the inspection script and relevant read-only commands:

```bash
rtk git status --short
rtk git remote -v
rtk git branch --show-current
rtk gh auth status
rtk python3 90_System/Skills/github-project-publisher/scripts/inspect_github_publish_state.py <repo>
```

Check:

- Is this a git repo?
- Is there a remote?
- Is the working tree dirty?
- Does `README.md` exist?
- Does `LICENSE` exist?
- Are build/test scripts present?
- Are risky files present?
- Is GitHub CLI authenticated?

## 3. Prepare Repo

Before publishing, recommend fixes for:

- Missing README
- Missing license for public repos
- Missing `.gitignore`
- Sensitive files
- Broken build or tests
- Uncommitted changes

Only create or edit files if the user asked for that. For README generation, use `project-readme-builder` when available.

## 4. Confirm Write Plan

Before write operations, present:

```text
Planned GitHub actions:
- ...

Repo visibility:
- public/private

Local git actions:
- ...

Risks / blockers:
- ...

Please confirm before I continue.
```

## 5. Publish

Common paths:

- New repo: `gh repo create`, then push.
- Existing remote: verify remote URL, then push.
- Existing GitHub repo URL from user: add or update remote only after confirmation.
- Release: create tag and `gh release create`.
- Pages: configure Pages source or guide user through repo settings if CLI/API support is insufficient.

## 6. Verify

Use read-only commands:

```bash
rtk gh repo view <owner>/<repo> --web=false
rtk git ls-remote --heads origin
rtk gh release view <tag>
```

Return links and any manual follow-up.
