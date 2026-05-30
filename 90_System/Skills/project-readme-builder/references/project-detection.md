# Project Detection

Inspect project facts before writing.

## Files To Check

- `README.md`
- `AGENTS.md`
- `agents/README.md`
- `docs/project-home.md`
- `package.json`
- `pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`
- `pyproject.toml`, `requirements.txt`, `uv.lock`
- `Cargo.toml`
- `go.mod`
- `Dockerfile`, `docker-compose.yml`, compose files
- `.env.example`
- `public/`, `assets/`, `docs/assets/`
- `src/`, `app/`, `pages/`, `server/`, `api/`, `backend/`, `frontend/`

## Detection Hints

- React / Vite: `vite`, `react`, `src/main.*`
- Next.js: `next`, `app/`, `pages/`, `next.config.*`
- Node API: `express`, `fastify`, `hono`, route files, `server.*`
- Python app: `fastapi`, `flask`, `django`, `streamlit`
- CLI: bin entries, command modules, argument parsers
- Library/package: exported modules, package metadata, tests, examples
- Static site: docs framework, markdown content, build config

## Command Extraction

Use actual scripts when present. For JavaScript projects, read `package.json` scripts and package manager lockfile.

Examples:

```markdown
| Command | Description |
|---|---|
| `pnpm install` | Install dependencies |
| `pnpm dev` | Start local development |
| `pnpm build` | Build for production |
```

Do not add commands that are not supported by the project.

## Missing Facts

If important information is missing, add an "Assumptions / Missing Information" note in the final response rather than inventing content.
