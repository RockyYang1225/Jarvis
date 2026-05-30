# Jarvis Public Repo Design

Date: 2026-05-30

## Goal

Turn the existing `<jarvis-root>` directory into a public GitHub project that others can reuse as a personal work-system template, while Rocky can keep using the same directory as the single source of truth.

The repo should publish the reusable Jarvis system:

- directory structure
- session routing rules
- indexes
- workflows
- agents
- prompts
- templates
- custom skills
- installation scripts
- usage documentation

The repo should not publish private runtime content such as real project status, career documents, personal reviews, or private knowledge notes.

## Chosen Approach

Use the existing `<jarvis-root>` directory as the public repo.

This avoids a second template repo that would have to be manually synchronized. Jarvis itself remains the maintained source. Public/private boundaries are handled with `.gitignore`, placeholder files, and documentation.

## Public Boundary

Files that should be versioned:

- `AGENTS.md`
- `README.md`
- `.gitignore`
- `scripts/install.sh`
- `scripts/sync-skills.sh` if split from the installer
- `00_Home/` generic operating guide files
- `90_System/Agents/`
- `90_System/Workflows/`
- `90_System/Templates/`
- `90_System/Prompts/`
- `90_System/Rules/`
- `90_System/Tools/`
- `90_System/Skills/`
- `90_System/Indexes/`
- top-level layer index files such as `10_Workspace/Projects.md`, `30_Ideas/Ideas.md`, `40_Knowledge/Knowledge.md`, and `50_Reviews/Reviews.md`
- empty directory placeholders such as `.gitkeep` for required folders

Files that should be excluded or handled cautiously:

- real project cards under `10_Workspace/Active Projects/`
- personal career assets under `20_Career/`
- private knowledge notes under `40_Knowledge/`
- personal reviews under `50_Reviews/`
- local automation state, logs, caches, temporary exports, and machine-specific files
- any file containing accounts, email workflows, private project status, resumes, interview material, or private notes

System files under `90_System/` can be versioned, but they must pass a public-readiness scan before the first public commit. Personal emails, machine-specific paths that do not belong in a reusable template, private automation targets, or real project state should be sanitized or moved to local-only notes.

## Repo Structure

The public repo keeps Jarvis's current layer model:

```text
00_Home/
10_Workspace/
20_Career/
30_Ideas/
40_Knowledge/
50_Reviews/
90_System/
docs/
scripts/
AGENTS.md
README.md
```

Each layer should keep a stable index file. Subdirectories that are part of the standard structure should be retained with `.gitkeep` if their contents are local-only.

## Installation Design

The installation script should support a cloned checkout on another machine.

Primary command:

```bash
./scripts/install.sh
```

Installer responsibilities:

- verify it is run from the Jarvis repo root, or resolve the repo root
- create required layer directories if they are missing
- create `.gitkeep` placeholders for empty standard directories
- create local skill discovery links from `~/.agents/skills/<skill>` to `Jarvis/90_System/Skills/<skill>`
- preserve existing files and never delete local content
- print next steps for opening Codex from the Jarvis root

The installer should be idempotent: running it multiple times should be safe.

## Skills And Workflows

Rocky-owned custom skills should live in:

```text
90_System/Skills/<skill-name>/
```

The installer should expose them through symlinks:

```text
~/.agents/skills/<skill-name> -> <repo>/90_System/Skills/<skill-name>
```

Workflows, agents, prompts, and templates should stay under `90_System/` and be versioned with the repo.

## README Requirements

The README should explain:

- what Jarvis is
- who it is for
- what gets versioned
- what should stay local
- quick start
- installation command
- how to use with Codex
- how to add new workflows, templates, agents, and skills
- recommended GitHub setup
- privacy cautions before publishing

The README should be useful to both Rocky and outside users.

## Git Ignore Strategy

The `.gitignore` should protect private or runtime content by default while still allowing public index files and system assets.

Expected behavior:

- keep public index files
- ignore private contents of active project, career, review, and private knowledge subfolders
- keep `.gitkeep` placeholders
- ignore caches, logs, exports, OS files, editor files, and local environment files

If a private section needs a public example, add a sanitized example or template instead of committing the real note.

## Implementation Plan Preview

After this design is approved, implementation should:

1. initialize git in `<jarvis-root>` if it is still not a repo
2. run a public-readiness scan for obvious private data
3. add `.gitignore`
4. add `README.md`
5. add `scripts/install.sh`
6. add required `.gitkeep` placeholders
7. verify skill directories are versionable
8. run the installer locally
9. inspect `git status --short` before any commit
10. commit the public repo setup only if the staged file list looks safe

## Verification

Minimum verification:

- `./scripts/install.sh` completes successfully
- required directories exist after install
- `~/.agents/skills` links point to the repo skill directories
- `git status --short` does not include private runtime content
- README instructions match actual commands
- public-readiness scan does not show obvious private email, token, secret, or resume/interview content in tracked files

## Open Decisions

None. The user approved using the current Jarvis directory as the public repo with explicit public boundaries.
