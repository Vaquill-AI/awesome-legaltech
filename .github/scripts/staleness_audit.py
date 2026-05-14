#!/usr/bin/env python3
"""Flag github.com entries in README.md whose repo is archived or has had no
pushes within STALE_MONTHS (default 18). Writes a Markdown report and sets the
GitHub Actions output `stale_count`."""

from __future__ import annotations

import os
import re
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

GITHUB_REPO_RE = re.compile(
    r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)(?:[/#?][^\s)\"']*)?",
    re.IGNORECASE,
)


def normalize_repo(owner: str, name: str) -> tuple[str, str]:
    name = re.sub(r"\.git$", "", name)
    return owner, name


def extract_repos(readme_text: str) -> list[tuple[str, str]]:
    seen: set[tuple[str, str]] = set()
    repos: list[tuple[str, str]] = []
    for match in GITHUB_REPO_RE.finditer(readme_text):
        owner, name = normalize_repo(match.group(1), match.group(2))
        if name.lower() in {"topics", "search", "marketplace", "settings", "sponsors", "orgs"}:
            continue
        key = (owner.lower(), name.lower())
        if key in seen:
            continue
        seen.add(key)
        repos.append((owner, name))
    return repos


def fetch_repo(owner: str, name: str, token: str | None) -> dict | None:
    req = urllib.request.Request(f"https://api.github.com/repos/{owner}/{name}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "awesome-legaltech-staleness-audit")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"_error": f"HTTP {e.code}"}
    except urllib.error.URLError as e:
        return {"_error": f"URL error: {e.reason}"}
    except Exception as e:  # pragma: no cover
        return {"_error": f"{type(e).__name__}: {e}"}


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: staleness_audit.py <readme-path> <report-path>", file=sys.stderr)
        return 2

    readme_path, report_path = sys.argv[1], sys.argv[2]
    stale_months = int(os.environ.get("STALE_MONTHS", "18"))
    token = os.environ.get("GITHUB_TOKEN")
    cutoff = datetime.now(timezone.utc) - timedelta(days=stale_months * 30)

    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

    repos = extract_repos(readme)
    archived: list[tuple[str, str, str]] = []
    stale: list[tuple[str, str, str]] = []
    errors: list[tuple[str, str, str]] = []

    for owner, name in repos:
        data = fetch_repo(owner, name, token)
        if data is None or "_error" in (data or {}):
            errors.append((owner, name, (data or {}).get("_error", "unknown")))
            continue
        slug = f"{owner}/{name}"
        if data.get("archived"):
            archived.append((slug, data.get("html_url", ""), data.get("pushed_at", "")))
            continue
        pushed_at = data.get("pushed_at")
        if not pushed_at:
            continue
        try:
            pushed_dt = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
        except ValueError:
            continue
        if pushed_dt < cutoff:
            stale.append((slug, data.get("html_url", ""), pushed_at))

    total = len(archived) + len(stale)
    lines: list[str] = []
    lines.append(f"Monthly staleness audit. Cutoff: no push within **{stale_months} months** "
                 f"(before {cutoff.date().isoformat()}).")
    lines.append("")
    lines.append(f"Checked **{len(repos)}** unique github.com entries. "
                 f"**{len(archived)}** archived, **{len(stale)}** stale, **{len(errors)}** errored.")
    lines.append("")

    if archived:
        lines.append("## Archived by owner")
        lines.append("")
        for slug, url, pushed in archived:
            lines.append(f"- [{slug}]({url}) - last push {pushed or 'unknown'}")
        lines.append("")

    if stale:
        lines.append(f"## No push within {stale_months} months")
        lines.append("")
        for slug, url, pushed in stale:
            lines.append(f"- [{slug}]({url}) - last push {pushed}")
        lines.append("")

    if errors:
        lines.append("## Errored (could not check)")
        lines.append("")
        for owner, name, msg in errors:
            lines.append(f"- `{owner}/{name}` - {msg}")
        lines.append("")

    if total == 0 and not errors:
        lines.append("All checked repos have recent activity. No action needed.")

    lines.append("")
    lines.append("---")
    lines.append("Per CONTRIBUTING.md, archived repos and projects with no commits for 2+ years "
                 "should be moved to the `Deprecated / Archived` section in README.md. "
                 "The 18-month cutoff used here is intentionally tighter so candidates are flagged "
                 "before they cross the 2-year deletion threshold.")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write(f"stale_count={total}\n")

    print(f"archived={len(archived)} stale={len(stale)} errors={len(errors)} total_flagged={total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
