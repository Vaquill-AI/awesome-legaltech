# Contribution Guidelines

Thank you for your interest in contributing to **Awesome Legaltech**! This document outlines the process for submitting contributions and the standards we hold entries to.

## The Pull Request Process

1. **Fork** this repository and create your branch from `main`.
2. Make your additions to `README.md`.
3. Ensure your PR has a **clear title** and **description** explaining what was added and why it belongs.
4. Fill in the PR template completely, including the inclusion criterion and the evidence (stars, last commit date, link).
5. Submit the pull request.

### One PR, one entry, one line

- Add **one entry per PR**, unless the entries are two parts of the same project (for example a server and its client).
- Touch **only the lines you are adding**. Do not reformat, reorder or reword existing entries.
- Add the entry to the **single most fitting section**, in the same order the section already uses (alphabetical where the section is alphabetical).
- Do not add the same project in several sections.

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
- **At least 5 GitHub stars** - every open-source project, and every entry whose primary link is a GitHub repository, must have 5 or more stars at the time the PR is opened. Stars must be organic: a repo whose stars come from the submitter's own accounts or from star-swapping will be declined. Commercial products with no public repo are exempt from this rule and are judged on the other criteria below.
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
- Open-source projects with fewer than **5 GitHub stars**, brand-new repos with no history of commits or releases, and repos with no README or no license
- Entries whose repo has been archived, or has had no commits in the past 18 months
- Pure landing pages, waitlists, "coming soon" sites, or products that require a sales call to see anything real
- Thin wrappers around a general-purpose LLM or a public API with no legal-specific data or logic of its own
- Entries that exist mainly to carry a backlink, referral link or tracking parameters (strip UTM and referral parameters from every link)
- Self-promotional PRs that bundle several of the submitter's projects at once; submit the strongest one first, and add others only after it has been merged and the project has earned its place

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
- Link directly to the project, with no UTM or referral parameters and no URL shorteners.
- Do not use all caps, exclamation marks, emoji or words such as "best", "leading", "revolutionary", "AI-powered" or "all-in-one".
- State what the tool does and, for data tools, what jurisdiction and sources it covers.

### What reviewers check

Maintainers will verify the following before merging, and a PR that fails any of them is asked to fix it or is closed:

1. The project has **5 or more GitHub stars** (open source) or is a live, publicly accessible product (commercial).
2. The last commit or release is within **18 months**, and the repo is not archived.
3. The link works, and the repo has a README that explains what the project does.
4. The entry is not a duplicate and is in the right section.
5. The diff adds only the new line(s).
6. The description is neutral and factual.

A PR that is waiting on the contributor for **14 days** with no reply may be closed. You can reopen it once the feedback is addressed.

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
