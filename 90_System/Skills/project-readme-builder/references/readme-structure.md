# README Structure

Build the README as the project's front door, not as an exhaustive internal manual.

## Recommended Order

Use this default order for most projects:

1. Project title
2. One-sentence positioning
3. Visual hero, screenshot, SVG diagram, or badge group
4. Language switch links, if multilingual
5. Table of contents, if long
6. Overview
7. Features
8. Tech stack
9. Quick start
10. Configuration / environment variables
11. Common commands
12. Usage
13. Project structure
14. Deployment
15. Documentation links
16. Roadmap / status
17. Contributing, if public
18. License, if known

## Showcase Order For Public Projects

For public repos, plugins, apps, portfolio projects, and tools meant to be shared, prefer a stronger homepage-style opening:

1. Project title
2. Two-line positioning: what it does and which platforms/users it supports
3. Hero visual, product screenshot, demo GIF, or generated/SVG cover
4. Language switch rail
5. Badge/action rail: quick start, license, platform support, homepage, live demo, docs, community
6. Community or support callout, if real
7. Problem hook: a concrete user situation or pain point
8. Short explanation of the product's core idea
9. Optional quote-style value statement
10. Core features
11. Quick start
12. Deeper usage examples
13. Platform support or compatibility matrix, if relevant
14. Sharing/team workflow, if relevant
15. Technical principles or architecture
16. Community/tutorials
17. Contributing
18. Star history or project status, if useful
19. License

Do not force every section. The goal is a repo homepage with momentum, not a bloated brochure.

## Section Guidance

- Keep the opening crisp: what it is, who it is for, and what it does.
- For public projects, put the most compelling proof near the top: demo, screenshot, supported platforms, install path, or community link.
- Use a problem hook when the project solves a recognizable pain.
- Put runnable commands near the top.
- Prefer numbered quick starts for tools and plugins.
- Prefer capability-oriented feature sections over generic feature lists.
- Prefer tables for command lists, environment variables, and tech stack summaries.
- Use compatibility matrices for multi-platform tools.
- Keep implementation details in linked docs when they already exist.
- If the README set has multiple languages or variants, keep root `README.md` as the landing page and store companion files under `READMEs/`. Do not place localized README files directly in the repo root.
- For demo projects, label status honestly and explain what is production-ready versus experimental.
- For private projects, do not add public contribution instructions unless requested.
- For public projects, include installation, usage, license, and support/contact expectations when known.

## Accuracy Rules

- Derive commands from actual project files.
- Derive tech stack from dependencies and source files.
- Link to existing docs instead of duplicating long content.
- If a likely section cannot be verified, either omit it or add a short "Not documented yet" note only when useful.
- Do not claim deployments, APIs, platforms, benchmarks, or screenshots that are not present or generated in this task.
