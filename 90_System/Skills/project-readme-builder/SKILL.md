---
name: project-readme-builder
description: Generate or refresh project-level README files with accurate project overview, polished open-source showcase structure, setup instructions, internal links, multilingual variants, badges, calls to action, and visual assets. Use when the user asks to create, improve, translate, localize, or audit a repository README, project homepage README, GitHub README, screenshots, SVG diagrams, badges, hero images, or README images.
---

# Project README Builder

Use this skill to create a repository's global `README.md` as a clear project homepage.

## Quick Start

1. Inspect the project before writing:
   - `README.md`
   - package or build files such as `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`
   - `AGENTS.md`, `agents/README.md`, `docs/project-home.md` when present
   - source folders, public assets, examples, deployment config, and test commands
2. Determine target language mode:
   - If the user specifies a language, use it.
   - If not specified, infer from existing docs and audience.
   - For public repos, prefer English as primary unless the user says otherwise.
3. Choose README output mode:
   - Single language: `README.md`
   - Single file with language anchors: one `README.md`
   - Multi-file localized docs: `README.md`, `README.zh-CN.md`, `README.ja.md`, `README.ko.md`, etc.
4. Choose presentation mode:
   - Practical/internal README for private or early projects.
   - Showcase README for public repos, plugins, apps, and portfolio projects.
5. Write or update the README with truthful project details only.
6. Add visual assets, badges, and calls to action when useful.
7. Validate local links and image paths with:

```bash
rtk python3 90_System/Skills/project-readme-builder/scripts/check_readme_links.py <repo> [README.md]
```

## Required README Sections

Use the project's needs to choose sections, but usually include:

- Title and concise one-sentence positioning
- Hero image, screenshot, SVG diagram, or badge block when appropriate
- Language switch links for multilingual projects
- Badge and action link rail for public projects
- Overview
- Feature highlights
- Tech stack
- Quick start
- Environment variables
- Common scripts / commands
- Project structure
- Usage examples
- Deployment notes
- Roadmap or project status
- Related docs
- License when known

Do not invent unavailable features, URLs, screenshots, deployments, tests, or license terms.

## References

Load only what you need:

- For README structure and section rules, read [references/readme-structure.md](references/readme-structure.md).
- For polished public/open-source README patterns, read [references/showcase-patterns.md](references/showcase-patterns.md).
- For language selection, localization, and multilingual links, read [references/localization.md](references/localization.md).
- For screenshots, SVG diagrams, generated images, and asset paths, read [references/visual-assets.md](references/visual-assets.md).
- For project inspection heuristics, read [references/project-detection.md](references/project-detection.md).
- For final checks and output format, read [references/quality-check.md](references/quality-check.md).

## Visual Asset Rules

- Prefer existing real screenshots or product images when available.
- Public README top sections may include a compact badge rail and action links.
- Use SVG for architecture diagrams, flows, simple product diagrams, badges, and lightweight illustrations.
- Use image generation for product cover art, editorial hero images, mockups, or visual scenes that benefit from raster imagery.
- Store project-owned assets under `docs/assets/`, `public/`, or the repo's existing asset convention.
- Ensure every README image link resolves from the README location.

## Link Rules

- Use relative links for repo files.
- Use verified absolute URLs for external links.
- Add a table of contents for long README files.
- Add language switch links for multilingual READMEs.
- Before finishing, run the link checker or manually verify every local link if the script cannot run.

## Output

When done, report:

- README files changed or created
- Visual assets changed or created
- Language mode used
- Link validation result
- Any project facts that could not be verified
