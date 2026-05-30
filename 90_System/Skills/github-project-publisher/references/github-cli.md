# GitHub CLI

Prefer GitHub CLI (`gh`) for GitHub operations.

## Authentication

Check:

```bash
rtk gh auth status
```

If not authenticated, ask the user to run:

```bash
gh auth login
```

Do not request or handle raw GitHub tokens in chat.

## Create Repository

Use after confirmation:

```bash
rtk gh repo create <owner>/<repo> --private --source=. --remote=origin --push
```

For public repos, use `--public` only after explicit confirmation.

Useful variations:

```bash
rtk gh repo create <repo> --private --source=. --remote=origin
rtk git push -u origin <branch>
```

## Connect Existing Repo

Read-only check:

```bash
rtk git remote -v
```

After confirmation:

```bash
rtk git remote add origin <url>
rtk git push -u origin <branch>
```

If `origin` exists, do not overwrite it automatically. Ask whether to keep, rename, or update it.

## Repo Metadata

Read:

```bash
rtk gh repo view <owner>/<repo> --web=false
```

Set description/homepage only if user asks:

```bash
rtk gh repo edit <owner>/<repo> --description "<description>"
rtk gh repo edit <owner>/<repo> --homepage "<url>"
```

## Safe Defaults

- Default visibility is private unless the user explicitly asks for public.
- Default branch is the current local branch.
- Use non-interactive commands where possible.
- If `gh` prompts unexpectedly, stop and explain what manual input is needed.
