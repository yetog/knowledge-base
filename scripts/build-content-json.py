#!/usr/bin/env python3
"""Parse system-design topic .md files and emit content.json for the SLAM OG app.

Usage: python scripts/build-content-json.py

Output: docs/courses/system-design/content.json
"""

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
COURSE_DIR = ROOT / "docs" / "courses" / "system-design"
OUT_FILE = COURSE_DIR / "content.json"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_md(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fm = yaml.safe_load(match.group(1)) or {}
    body = text[match.end():].strip()
    return {**fm, "body_md": body, "file": str(path.relative_to(ROOT)).replace("\\", "/")}


def main() -> None:
    if not COURSE_DIR.exists():
        sys.exit(f"course dir not found: {COURSE_DIR}")

    topics = []
    for md_path in sorted(COURSE_DIR.glob("*.md")):
        if md_path.name == "index.md":
            continue
        topic = parse_md(md_path)
        if topic and topic.get("slug"):
            topics.append(topic)

    by_tier: dict[str, int] = {}
    for t in topics:
        tier = t.get("tier", "unsorted")
        by_tier[tier] = by_tier.get(tier, 0) + 1

    output = {
        "course": "system-design",
        "topic_count": len(topics),
        "by_tier": by_tier,
        "topics": topics,
    }
    OUT_FILE.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT_FILE.relative_to(ROOT)} ({len(topics)} topics: {by_tier})")


if __name__ == "__main__":
    main()
