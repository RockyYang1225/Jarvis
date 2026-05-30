#!/usr/bin/env python3
"""Search a github-daily-report markdown archive for relevant entries."""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path


DEFAULT_REPO = Path(os.environ.get("GITHUB_DAILY_REPORT_REPO", "~/Workspace/github-daily-report")).expanduser()
ENTRY_RE = re.compile(r"^- \[(?P<title>[^\]]+)\]\((?P<url>[^)]+)\)(?P<meta>.*)$")
SECTION_RE = re.compile(r"^##\s+(?P<section>.+?)\s*$")
CAPABILITY_KEYWORDS = [
    "skill",
    "skills",
    "plugin",
    "plugins",
    "mcp",
    "agent",
    "agents",
    "extension",
    "extensions",
    "framework",
    "frameworks",
    "tool",
    "tools",
    "toolkit",
    "cli",
    "workflow",
    "workflows",
    "automation",
    "integration",
    "server",
    "servers",
    "插件",
    "扩展",
    "工具",
    "框架",
    "工作流",
    "自动化",
    "集成",
    "代理",
    "服务器",
]


@dataclass
class Entry:
    date: str
    section: str
    title: str
    url: str
    tags: list[str]
    source: str
    summary: str
    why: str
    suggestion: str
    score: int
    file: str


def normalize(text: str) -> str:
    return text.lower()


def query_terms(query: str, extra_terms: list[str]) -> list[str]:
    terms = [query.strip()]
    terms.extend(extra_terms)
    terms.extend(re.findall(r"[a-zA-Z0-9][a-zA-Z0-9_.+-]{1,}", query.lower()))
    terms.extend(re.findall(r"[\u4e00-\u9fff]{2,}", query))
    seen: set[str] = set()
    result: list[str] = []
    for term in terms:
        term = term.strip().lower()
        if term and term not in seen:
            seen.add(term)
            result.append(term)
    return result


def clean_value(line: str, label: str) -> str:
    marker = f"{label}："
    if marker in line:
        return line.split(marker, 1)[1].strip()
    return ""


def parse_entries(report_file: Path) -> list[dict]:
    lines = report_file.read_text(encoding="utf-8", errors="ignore").splitlines()
    current_section = ""
    entries: list[dict] = []
    current: dict | None = None
    block: list[str] = []

    def flush() -> None:
        nonlocal current, block
        if current is None:
            return
        current["block"] = "\n".join(block).strip()
        entries.append(current)
        current = None
        block = []

    for line in lines:
        section_match = SECTION_RE.match(line)
        if section_match:
            flush()
            current_section = section_match.group("section")
            continue

        entry_match = ENTRY_RE.match(line)
        if entry_match:
            flush()
            title = entry_match.group("title").strip()
            url = entry_match.group("url").strip()
            meta = entry_match.group("meta").strip()
            tags = re.findall(r"`([^`]+)`", meta)
            current = {
                "date": report_file.stem,
                "section": current_section,
                "title": title,
                "url": url,
                "meta": meta,
                "tags": tags,
                "file": str(report_file),
            }
            block = []
            continue

        if current is not None:
            block.append(line)

    flush()
    return entries


def summarize(raw_entry: dict, score: int) -> Entry:
    source = ""
    summary = ""
    why = ""
    suggestion = ""

    for raw_line in raw_entry.get("block", "").splitlines():
        line = raw_line.strip()
        source = source or clean_value(line, "来源")
        summary = summary or clean_value(line, "中文介绍")
        why = why or clean_value(line, "值得关注")
        suggestion = suggestion or clean_value(line, "建议")

    return Entry(
        date=raw_entry["date"],
        section=raw_entry["section"],
        title=raw_entry["title"],
        url=raw_entry["url"],
        tags=raw_entry["tags"],
        source=source,
        summary=summary,
        why=why,
        suggestion=suggestion,
        score=score,
        file=raw_entry["file"],
    )


def score_entry(raw_entry: dict, terms: list[str]) -> int:
    title_text = normalize(raw_entry["title"])
    tags_text = normalize(" ".join(raw_entry.get("tags", [])))
    url_text = normalize(raw_entry["url"])
    section_text = normalize(raw_entry.get("section", ""))
    block_text = normalize(raw_entry.get("block", ""))
    all_text = " ".join([title_text, tags_text, url_text, section_text, block_text])

    score = 0
    for term in terms:
        if not term:
            continue
        count = all_text.count(term)
        if count:
            score += min(count, 6)
            if term in title_text or term in tags_text or term in url_text:
                score += 4
            if term in section_text:
                score += 2

    if any(keyword in all_text for keyword in CAPABILITY_KEYWORDS):
        score += 1
    if any(key in section_text for key in ["skills", "agent", "工具", "插件", "mcp"]):
        score += 3
    if "github.com" in url_text:
        score += 1

    return score


def search(repo: Path, query: str, extra_terms: list[str], max_results: int) -> list[Entry]:
    reports_dir = repo / "reports"
    if not reports_dir.exists():
        raise FileNotFoundError(f"Reports directory not found: {reports_dir}")

    terms = query_terms(query, extra_terms)
    matches_by_url: dict[str, Entry] = {}
    for report_file in sorted(reports_dir.glob("*.md"), reverse=True):
        for raw_entry in parse_entries(report_file):
            score = score_entry(raw_entry, terms)
            if score > 0:
                entry = summarize(raw_entry, score)
                key = entry.url.lower()
                previous = matches_by_url.get(key)
                if previous is None or (entry.score, entry.date) > (previous.score, previous.date):
                    matches_by_url[key] = entry

    matches = list(matches_by_url.values())
    matches.sort(key=lambda item: (item.score, item.date), reverse=True)
    return matches[:max_results]


def markdown(results: list[Entry], query: str) -> str:
    if not results:
        return f"No local daily report matches for: {query}"

    lines = [f"Local daily report matches for: {query}", ""]
    for index, item in enumerate(results, 1):
        tags = ", ".join(item.tags)
        lines.append(f"{index}. [{item.title}]({item.url})")
        lines.append(f"   date: {item.date} | section: {item.section} | score: {item.score}")
        if tags:
            lines.append(f"   tags: {tags}")
        if item.source:
            lines.append(f"   source: {item.source}")
        if item.summary:
            lines.append(f"   summary: {item.summary}")
        if item.suggestion:
            lines.append(f"   suggestion: {item.suggestion}")
        lines.append("")
    return "\n".join(lines).rstrip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Search query")
    parser.add_argument("--repo", default=str(DEFAULT_REPO), help="github-daily-report path")
    parser.add_argument("--term", action="append", default=[], help="Extra search term")
    parser.add_argument("--max-results", type=int, default=8)
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    repo = Path(args.repo).expanduser()
    results = search(repo, args.query, args.term, args.max_results)

    if args.format == "json":
        print(json.dumps({"query": args.query, "results": [asdict(r) for r in results]}, ensure_ascii=False, indent=2))
    else:
        print(markdown(results, args.query))


if __name__ == "__main__":
    main()
