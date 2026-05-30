# Release Checklist

Use when the user asks to publish a release, tag a version, or create a downloadable GitHub release.

## Pre-Release Checks

- Working tree status is understood.
- Version/tag name is confirmed.
- README is accurate.
- Tests/build were run or explicitly skipped.
- Changelog or release notes are available.
- No secrets or private files are included.

## Tag Policy

Do not create or move tags without confirmation.

Recommended tag format:

```text
v0.1.0
v1.0.0
```

Create tag:

```bash
rtk git tag -a v0.1.0 -m "v0.1.0"
rtk git push origin v0.1.0
```

## Create Release

```bash
rtk gh release create v0.1.0 --title "v0.1.0" --notes-file RELEASE_NOTES.md
```

If no release notes file exists, draft concise notes from commits or ask the user for release highlights.

## Verify Release

```bash
rtk gh release view v0.1.0
```

Report the release URL.
