# Quality Check

Before finishing, verify the README as an artifact.

## Checklist

- The README matches the actual project.
- Setup commands exist and match the detected package manager.
- All local markdown links resolve.
- All local image links resolve.
- External links are either known official links or were verified when current accuracy matters.
- Visual assets are stored in the repo and referenced with relative paths.
- Badge/action links point to real anchors, files, or URLs.
- Language switch links work.
- If using `READMEs/`, links work from both root `README.md` and files inside `READMEs/`.
- Public README top section has clear positioning, proof/visuals, and a runnable path.
- The README does not claim unsupported features, deployments, screenshots, licenses, or production readiness.
- Long READMEs include a table of contents.
- Public READMEs include license information only when a license file or user instruction exists.

## Link Checker

Run:

```bash
rtk python3 90_System/Skills/project-readme-builder/scripts/check_readme_links.py <repo> [README.md]
```

For multiple localized READMEs, run the script once per file.

If the script cannot run, manually inspect markdown links and image paths.

## Final Response

Keep the handoff short:

```text
Updated README files:
- ...

Visual assets:
- ...

Validation:
- Link check: passed / failed / not run

Notes:
- ...
```
