# Showcase README Patterns

Use this reference when the user points to a polished public README as inspiration, or when creating a GitHub-facing project homepage.

The target feel is a project page that is useful immediately and credible at a glance: clear positioning, proof, install path, visuals, and deeper technical explanation.

## Front Door Pattern

Top section:

1. Project name
2. Short product promise in one or two lines
3. Platform or audience support line
4. Hero image, screenshot, demo GIF, trend image, or SVG/product diagram
5. Language switch links
6. Badges and action links
7. Primary community/demo/docs callout

Good action links include:

- Quick Start
- License
- Docs
- Homepage
- Live Demo
- Discord / community
- Supported platforms
- Package / marketplace

Only add links that are real or created in the task.

## Narrative Pattern

After the top rail, explain the project through a concrete situation:

- "When you join a new team..."
- "When your codebase grows..."
- "When you need to understand..."

Then explain the project as the answer to that situation in one tight paragraph.

An optional quote-style sentence can help if it clarifies the product philosophy. Keep it specific and avoid inflated marketing language.

## Feature Pattern

Use feature sections with descriptive headings and short explanations.

Prefer:

```markdown
### Explore the System Graph
Turn project files, functions, classes, and dependencies into a navigable map.
```

Avoid:

```markdown
- Feature 1
- Feature 2
- Feature 3
```

For apps and tools, include a note/callout near features when a live demo, homepage, or quick trial exists.

## Quick Start Pattern

Use numbered steps:

```markdown
## Quick Start

### 1. Install

```bash
...
```

### 2. Run

```bash
...
```

### 3. Open or Verify

```bash
...
```
```

Add a "Deep Usage" or "More Commands" section when there are many useful commands.

## Multi-Platform Pattern

For tools that support multiple hosts, editors, CLIs, deployment targets, or operating systems:

- Give the primary/native path first.
- Add one-line install commands for broad platforms.
- Use a compatibility table.
- Keep platform names in the original official spelling.

## Technical Credibility Pattern

Public READMEs can include technical principles after usage:

- Architecture overview
- Deterministic vs AI-assisted steps
- Data flow
- Agent/module responsibilities
- Incremental update strategy
- Performance or scalability notes, only when verified

This section should make the project feel inspectable, not mysterious.

## Community And Proof

Add community/tutorial sections only when real assets exist:

- Discord/community
- YouTube/tutorial
- Example repos
- Star history
- Case studies

If there is no real community/proof yet, omit this rather than inventing it.
