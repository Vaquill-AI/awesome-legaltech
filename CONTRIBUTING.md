# Contribution Guidelines

Thank you for your interest in contributing to **Awesome Legaltech**! This document outlines the process for submitting contributions and the standards we hold entries to.

## The Pull Request Process

1. **Fork** this repository and create your branch from `main`.
2. Make your additions to `README.md`.
3. Ensure your PR has a **clear title** and **description** explaining what was added and why it belongs.
4. Submit the pull request.

### Review SLA

Maintainers aim to triage every PR and issue within **7 days** - either with a merge, a request for changes, a deferral with reason, or a close. If your submission has been open longer than that without a response, feel free to leave a comment to bump it.

The link-checker runs automatically on every PR and must pass before merge. If it fails on a target site that is only transiently down, a maintainer may add the host to the workflow's exclude list rather than block your contribution.

## What We Look For

### The core principle

This is a **curated list**, not a comprehensive directory. There are thousands of legaltech companies doing meaningful work. Platforms like [Legaltech Hub](https://legaltechnologyhub.com) and [LawNext](https://www.lawnext.com/legal-tech-directory) are better suited for exhaustive listings. Our goal is to surface the most notable, distinctive, and educationally valuable entries within each category.

### Inclusion criteria

An entry should meet **at least one** of the following:

| Criterion | What it means |
|---|---|
| **Category-defining** | First-mover or widely credited with inventing/popularizing a category (e.g., Ironclad for CLM, Harvey for legal AI agents) |
| **Open source** | Has a public repo with meaningful code that the community can build on |
| **Significant scale** | $100M+ funding, or widely adopted at major law firms / courts / institutions |
| **Unique technical approach** | Does something meaningfully different from other listed tools in the same category |
| **Regional representation** | Best or most prominent tool for a geography or language not yet covered |
| **Academic / research value** | Peer-reviewed dataset, model, or benchmark that enables further research |

### Minimum bar for all entries

Regardless of the above, every entry must be:
- **Actively maintained** - open-source projects: meaningful activity in the past 18 months; commercial products: active and publicly accessible.
- **Factually verifiable** - must have a real website, repo, or publication. No vaporware.
- **Described neutrally** - no promotional language, no superlatives, no vendor marketing copy.
- **Distinct** - not already covered by an existing entry.

### Not accepted

- Generic tools with no legal-specific application (e.g., general-purpose cloud storage, office suites)
- Abandoned open-source projects (no activity in 2+ years)
- Landing pages with no verifiable product behind them
- Companies that are simply resellers or white-labels of already-listed platforms
- Personal projects, blog posts, or opinion pieces

## Formatting Guidelines

Please match the existing formatting style:

### For a simple list entry:
```markdown
- [Tool Name](https://tool-url.com) - One-sentence description of what it does and why it's notable.
```

### For a table entry:
```markdown
| [Tool Name](https://url.com) | Category | Key feature | Region/HQ |
```

### Rules:
- Descriptions should be **neutral and factual** - not promotional.
- Keep descriptions **concise** (one sentence preferred, two max).
- Use the **em dash** (`-`) as a separator in list entries.
- Add the country/region for companies where relevant.
- For open-source projects, link to the GitHub repo when possible.

## Adding a New Section

If you believe a new top-level section is needed:
- Open an **Issue** first to discuss it before submitting a PR.
- A section needs at least **5 distinct entries** to warrant its own heading.
- The section must not overlap substantially with existing sections.

## Deprecation Policy

When an entry becomes unmaintained, we **move** it rather than delete it. This keeps the historical record honest and prevents the same dead project from being re-submitted later.

An entry moves to the `## Deprecated / Archived` section in `README.md` when any of the following is true:

- The upstream GitHub repo has been **archived** by its owner.
- The company has **shut down**, been acquired and the product discontinued, or the product page returns a permanent error.
- An open-source project has had **no meaningful commits for 2+ years** (the staleness-audit workflow flags candidates monthly).
- The project's stated functionality is no longer available (API decommissioned, dataset taken down, etc.).

When moving an entry, keep the original link and add a short note: what it was, what happened, and a pointer to a successor if one exists.

## Reporting Issues

If you find:

- A broken link → Use the **Broken link** issue template.
- An outdated entry → Use the **Outdated entry** issue template.
- A deprecated/archived project still listed in the main sections → Use the **Deprecated entry** issue template.
- A duplicate entry → Open an issue with `[duplicate]` in the title.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).
