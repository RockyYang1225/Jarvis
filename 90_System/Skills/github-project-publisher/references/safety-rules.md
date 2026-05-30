# Safety Rules

Publishing to GitHub can expose private work. Use conservative defaults.

## Stop Before Publishing If Detected

- `.env`
- `.env.local`
- private keys
- tokens
- credentials
- service account files
- local database dumps
- user data exports
- private notes
- API keys in source files

Do not print secret values. Report only filenames or redacted patterns.

## Confirmation Required

Ask before:

- Creating a GitHub repo
- Making a repo public
- Adding or changing remotes
- Pushing branches
- Creating tags
- Creating releases
- Enabling GitHub Pages
- Editing repo metadata
- Creating GitHub Actions workflows

Ask for a stronger confirmation before:

- Force pushing
- Deleting a branch
- Deleting a tag
- Deleting or replacing a release
- Making a private repo public

## Public Repo Checklist

Before public release, check:

- README exists and is accurate.
- LICENSE exists or user confirms no license.
- `.gitignore` exists and covers local/env files.
- No secrets or private data are staged/tracked.
- Build/test status is known.
- Project status is honestly described.

## Dirty Working Tree

Do not commit user changes unless asked.

If there are uncommitted changes, summarize them and ask whether to:

- commit them
- push existing commits only
- pause publishing

## Existing Remote

If `origin` exists, do not overwrite it automatically.

Ask whether to:

- use existing origin
- add a new remote name
- update origin URL
- stop
