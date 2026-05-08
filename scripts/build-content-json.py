#!/usr/bin/env python3
"""Parse SLAM OG course topic .md files and emit content.json per course.

Usage:
    python scripts/build-content-json.py              # all courses
    python scripts/build-content-json.py system-design  # one course

Output: docs/courses/{course}/content.json for each course found.
"""

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
COURSES_ROOT = ROOT / "docs" / "courses"

# Courses that participate in the SLAM OG app (have structured topic frontmatter)
SLAM_OG_COURSES = ["system-design", "cloud-computing"]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_md(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fm = yaml.safe_load(match.group(1)) or {}
    body = text[match.end():].strip()
    return {**fm, "body_md": body, "file": str(path.relative_to(ROOT)).replace("\\", "/")}


def build_course(course: str) -> bool:
    course_dir = COURSES_ROOT / course
    out_file = course_dir / "content.json"
    if not course_dir.exists():
        print(f"  skip {course}: directory not found", file=sys.stderr)
        return False

    topics = []
    for md_path in sorted(course_dir.glob("*.md")):
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
        "course": course,
        "topic_count": len(topics),
        "by_tier": by_tier,
        "topics": topics,
    }
    out_file.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {out_file.relative_to(ROOT)} ({len(topics)} topics: {by_tier})")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("course", nargs="?", help="course slug (default: all SLAM OG courses)")
    args = parser.parse_args()

    courses = [args.course] if args.course else SLAM_OG_COURSES
    for course in courses:
        build_course(course)


if __name__ == "__main__":
    main()
