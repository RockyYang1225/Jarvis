# GitHub Pages Publishing

Use when the user asks to publish a static site, docs site, demo, portfolio, or web app through GitHub Pages.

## Fit Check

GitHub Pages is best for:

- Static HTML/CSS/JS
- Vite/React static build
- Documentation sites
- Portfolio pages
- Storybook/static demos

It is not suitable for:

- Long-running backend servers
- Private API services
- Apps requiring server-side secrets at runtime
- Databases or background jobs

## Build Output

Identify build command and output directory:

- Vite: often `npm run build`, output `dist/`
- Next.js static export: project-specific
- Docs sites: framework-specific

Do not assume output directory; inspect config and package scripts.

## Publishing Options

Common options:

- GitHub Actions workflow deploys build output
- `docs/` folder served from default branch
- `gh-pages` branch

Recommend GitHub Actions for modern frontend apps when a build step is required.

## Confirmation

Before enabling Pages, confirm:

- Source branch/folder
- Build command
- Output directory
- Public URL expectations

## Verification

After publish, report:

- Pages URL
- Build workflow URL, if applicable
- Any DNS or cache delay

If CLI support is insufficient for the exact configuration, provide the GitHub Settings path and keep changes local.
