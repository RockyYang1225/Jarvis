# Visual Assets

README visuals should clarify the project and make the repository easier to understand.

## Asset Types

- Existing screenshots: best for UI projects.
- SVG diagrams: best for architecture, data flow, feature maps, lightweight illustrations, and project structure.
- Generated raster images: best for product covers, hero images, concept scenes, or polished showcase graphics.
- Badges: useful for package, CI, license, and version status when sources are real.
- Action badges: useful for quick start, homepage, docs, live demo, platform support, and community links.

## Storage

Prefer the existing project convention. If none exists, use:

```text
docs/assets/
```

Common examples:

```text
docs/assets/readme-hero.svg
docs/assets/screenshot-main.png
docs/assets/architecture.svg
public/readme-cover.png
```

## SVG Guidance

Use SVG when the image should remain editable, small, sharp, and repo-native.

Good SVG candidates:

- README hero / cover diagram
- Architecture overview
- Request flow
- User journey
- Module relationship map
- CLI workflow
- App feature diagram
- Platform compatibility strip

Keep SVG readable in GitHub Markdown:

- Include a `viewBox`.
- Avoid external fonts.
- Use accessible contrast.
- Keep text short.
- Use `role="img"` and a `<title>` when appropriate.

## Generated Image Guidance

Use image generation only when a bitmap adds real value:

- Product hero / cover
- App promo image
- Concept art
- Domain-specific scene
- Polished visual identity

Do not use generated images to fake screenshots or product states that do not exist. Label conceptual images as such if ambiguity matters.

## README Embedding

Use relative paths:

```markdown
![App screenshot](docs/assets/screenshot-main.png)
```

For SVG diagrams:

```markdown
![Architecture diagram](docs/assets/architecture.svg)
```

After adding assets, verify paths from the README file location.

## Badge And Action Rail

For public READMEs, a compact badge rail can make key links scannable.

Use badges only when they point to real targets:

- Quick Start anchor
- License file
- Homepage
- Live demo
- Documentation
- Supported platform
- Community
- Package or marketplace

Prefer durable badge sources or local SVG badges. Do not add CI/package/version badges unless the underlying service or package exists.
