"""
Convert existing VuePress HTML pages to MkDocs Markdown source files.
Extracts content from the .theme-default-content div and writes clean .md files.
Run once from the knowledge-base root directory.
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"

# Map: source HTML path (relative to ROOT) -> dest .md path (relative to DOCS)
PAGE_MAP = {
    # Root
    "index.html": "index.md",

    # Tech - AI & Automation
    "tech/ai-development.html":      "tech/ai-automation/ai-development.md",
    "tech/automation-tools.html":    "tech/ai-automation/automation-tools.md",
    "tech/development-workflows.html": "tech/ai-automation/development-workflows.md",

    # Tech - Infrastructure (orphaned pages now included)
    "infrastructure/overview.html":          "tech/infrastructure/overview.md",
    "infrastructure/docker-strategy.html":   "tech/infrastructure/docker-strategy.md",
    "infrastructure/ci-cd-pipeline.html":    "tech/infrastructure/ci-cd-pipeline.md",
    "infrastructure/deployment-process.html":"tech/infrastructure/deployment-process.md",
    "infrastructure/orchestration-guide.html":"tech/infrastructure/orchestration-guide.md",
    "infrastructure/server-configuration.html":"tech/infrastructure/server-configuration.md",

    # Tech - Cheatsheets
    "tech/docker.html":                 "tech/cheatsheets/docker.md",
    "tech/postgresql.html":             "tech/cheatsheets/postgresql.md",
    "tech/postgres-data.html":          "tech/cheatsheets/postgres-data.md",
    "tech/regex.html":                  "tech/cheatsheets/regex.md",
    "tech/bash-profile.html":           "tech/cheatsheets/bash-profile.md",
    "tech/macos-tips.html":             "tech/cheatsheets/macos-tips.md",
    "tech/html-cheatsheet.html":        "tech/cheatsheets/html-cheatsheet.md",
    "tech/vscode-snippets.html":        "tech/cheatsheets/vscode-snippets.md",
    "tech/seo.html":                    "tech/cheatsheets/seo.md",
    "tech/webhook.html":                "tech/cheatsheets/webhook.md",
    "tech/secrets-management-sops.html":"tech/cheatsheets/secrets-management-sops.md",

    # Tech - Reference
    "tech/session-recaps.html":   "tech/reference/session-recaps.md",
    "tech/today-i-learned.html":  "tech/reference/today-i-learned.md",
    "tech/mental-models.html":    "tech/reference/mental-models.md",
    "tech/awesome-list.html":     "tech/reference/awesome-list.md",

    # Business
    "business/hiring.html":      "business/hiring.md",
    "business/management.html":  "business/management.md",
    "business/sales.html":       "business/sales.md",
    "business/marketing.html":   "business/marketing.md",
    "business/fundraising.html": "business/fundraising.md",
    "business/resources.html":   "business/resources.md",

    # Philosophy
    "philosophy/ethics.html":    "philosophy/ethics.md",
    "philosophy/buddhism.html":  "philosophy/buddhism.md",
    "philosophy/stoicism.html":  "philosophy/stoicism.md",
    "philosophy/desire.html":    "philosophy/desire.md",

    # People
    "people.html":                    "people/index.md",
    "people/lee-kuan-yew.html":       "people/lee-kuan-yew.md",
    "people/jensen-huang.html":       "people/jensen-huang.md",
    "people/elon-musk.html":          "people/elon-musk.md",
    "people/marlon-brando.html":      "people/marlon-brando.md",
    "people/nelson-mandela.html":     "people/nelson-mandela.md",

    # Personal Development (was "Levels")
    "levels/business.html":    "personal-development/business.md",
    "levels/life.html":        "personal-development/life.md",
    "levels/leadership.html":  "personal-development/leadership.md",
    "levels/learning.html":    "personal-development/learning.md",

    # Science & Nature
    "space.html":    "science-nature/space.md",
    "soil.html":     "science-nature/soil.md",
    "trees.html":    "science-nature/trees.md",
    "zoology.html":  "science-nature/zoology.md",
    "pyrolysis.html":"science-nature/pyrolysis.md",
    "physics.html":  "science-nature/physics.md",
    "mathematics.html": "science-nature/mathematics.md",

    # Arts & Culture
    "music.html":          "arts-culture/music.md",
    "chess.html":          "arts-culture/chess.md",
    "climbing.html":       "arts-culture/climbing.md",
    "languages.html":      "arts-culture/languages.md",
    "writing.html":        "arts-culture/writing.md",
    "public-speaking.html":"arts-culture/public-speaking.md",

    # Mind & Body
    "meditation.html":    "mind-body/meditation.md",
    "consciousness.html": "mind-body/consciousness.md",
    "relationships.html": "mind-body/relationships.md",
    "mimetic-theory.html":"mind-body/mimetic-theory.md",

    # Courses
    "ai-engineering/index.html":           "courses/ai-engineering/index.md",
    "ai-engineering/syllabus.html":        "courses/ai-engineering/syllabus.md",
    "ai-engineering/foundations.html":     "courses/ai-engineering/foundations.md",
    "ai-engineering/core-applications.html":"courses/ai-engineering/core-applications.md",
    "ai-engineering/advanced-techniques.html":"courses/ai-engineering/advanced-techniques.md",
    "ai-engineering/capstone-advanced.html":"courses/ai-engineering/capstone-advanced.md",
    "courses/mindfulness.html":            "courses/mindfulness.md",
}


def extract_content(html_path: Path) -> str:
    """Extract the main content div from a VuePress HTML file."""
    text = html_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(text, "html.parser")

    # VuePress wraps page content in this div
    content = soup.find("div", class_="theme-default-content")
    if not content:
        # Fallback: grab the <main> tag
        content = soup.find("main")
    if not content:
        print(f"  WARNING: no content found in {html_path.name}")
        return f"# {html_path.stem.replace('-', ' ').title()}\n\n*(Content not found — please add manually.)*\n"

    # Remove the header anchor links VuePress adds (#)
    for a in content.find_all("a", class_="header-anchor"):
        a.decompose()

    # Remove table-of-contents divs (MkDocs generates its own)
    for toc in content.find_all("div", class_="table-of-contents"):
        toc.decompose()

    raw_md = md(
        str(content),
        heading_style="ATX",
        bullets="-",
        code_language_callback=lambda el: el.get("class", [""])[0].replace("language-", "") if el.get("class") else "",
    )

    # Clean up excessive blank lines
    raw_md = re.sub(r'\n{3,}', '\n\n', raw_md)
    return raw_md.strip() + "\n"


def convert_all():
    converted = 0
    skipped = 0

    for src_rel, dest_rel in PAGE_MAP.items():
        src = ROOT / src_rel
        dest = DOCS / dest_rel

        if not src.exists():
            print(f"  SKIP (missing): {src_rel}")
            skipped += 1
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)
        content = extract_content(src)
        dest.write_text(content, encoding="utf-8")
        print(f"  OK  {src_rel} -> docs/{dest_rel}")
        converted += 1

    print(f"\nDone: {converted} converted, {skipped} skipped.")


if __name__ == "__main__":
    convert_all()
