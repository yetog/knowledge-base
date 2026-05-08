#!/usr/bin/env python3
"""Extract structured markdown from a PDF for study/rewriting.

Usage: python scripts/extract-pdf.py path/to/book.pdf

Output goes to study/{slug}/ (gitignored). Read the chapters, then write
your own SLAM OG version in docs/courses/.
"""

import argparse
import re
import sys
from pathlib import Path

import pymupdf


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60] or "untitled"


def detect_heading_sizes(doc: pymupdf.Document) -> set[float]:
    sizes: dict[float, int] = {}
    for page in doc:
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    size = round(span["size"], 1)
                    sizes[size] = sizes.get(size, 0) + 1
    if not sizes:
        return set()
    body_size = max(sizes.items(), key=lambda x: x[1])[0]
    sorted_sizes = sorted(sizes.items(), key=lambda x: -x[0])
    return {size for size, _ in sorted_sizes[:3] if size > body_size + 1}


def extract_chapters_from_toc(doc: pymupdf.Document):
    """Use the PDF's bookmark-based TOC if available. Filter to top-level chapters."""
    toc = doc.get_toc()
    if not toc:
        return None
    # Take level-1 entries (chapters) — fall back to level 2 if level 1 is too coarse
    level1 = [(t, p) for lvl, t, p in toc if lvl == 1]
    if len(level1) < 3:
        # Too few chapters at level 1 — go one deeper
        level1 = [(t, p) for lvl, t, p in toc if lvl <= 2]
    chapters = []
    for idx, (title, start_page) in enumerate(level1):
        end_page = level1[idx + 1][1] - 1 if idx + 1 < len(level1) else len(doc)
        text = []
        for page_num in range(max(start_page, 1), min(end_page + 1, len(doc) + 1)):
            text.append(doc[page_num - 1].get_text())
        chapters.append({
            "title": title.strip(),
            "text": [t for t in text if t.strip()],
            "page_start": start_page,
            "page_end": end_page,
        })
    return chapters


def extract_chapters_by_font(doc: pymupdf.Document, heading_sizes: set[float]):
    chapters = []
    current = {"title": "Front Matter", "text": [], "page_start": 1}
    for page_num, page in enumerate(doc, 1):
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                line_text = "".join(s["text"] for s in line["spans"]).strip()
                if not line_text:
                    continue
                line_size = max((round(s["size"], 1) for s in line["spans"]), default=0)
                if line_size in heading_sizes and len(line_text) < 120:
                    if current["text"]:
                        current["page_end"] = page_num
                        chapters.append(current)
                    current = {"title": line_text, "text": [], "page_start": page_num}
                else:
                    current["text"].append(line_text)
    if current["text"]:
        current["page_end"] = len(doc)
        chapters.append(current)
    return chapters


def write_chapter(chapter, idx: int, out_dir: Path) -> str:
    slug = slugify(chapter["title"])
    filename = f"{idx:02d}-{slug}.md"
    body = "\n\n".join(chapter["text"])
    content = (
        f"# {chapter['title']}\n\n"
        f"**Pages:** {chapter['page_start']}–{chapter.get('page_end', '?')}\n\n"
        f"---\n\n{body}\n"
    )
    (out_dir / filename).write_text(content, encoding="utf-8")
    return filename


def write_toc(chapters, out_dir: Path, source_name: str) -> None:
    lines = [
        f"# Study TOC — {source_name}",
        "",
        f"**{len(chapters)} chapters extracted.** Read a chapter, then write your own SLAM OG version in `docs/courses/`.",
        "",
        "---",
        "",
    ]
    for idx, chapter in enumerate(chapters, 1):
        slug = slugify(chapter["title"])
        filename = f"{idx:02d}-{slug}.md"
        word_count = sum(len(t.split()) for t in chapter["text"])
        lines.append(
            f"{idx}. [{chapter['title']}](chapters/{filename}) — "
            f"pp. {chapter['page_start']}–{chapter.get('page_end', '?')} "
            f"({word_count} words)"
        )
    (out_dir / "TOC.md").write_text("\n".join(lines), encoding="utf-8")


def extract_images(doc: pymupdf.Document, out_dir: Path) -> int:
    images_dir = out_dir / "images"
    images_dir.mkdir(exist_ok=True)
    count = 0
    for page_num, page in enumerate(doc, 1):
        for img_idx, img in enumerate(page.get_images(full=True), 1):
            xref = img[0]
            try:
                pix = pymupdf.Pixmap(doc, xref)
                if pix.n - pix.alpha >= 4:
                    pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
                pix.save(images_dir / f"page-{page_num:03d}-img-{img_idx}.png")
                count += 1
                pix = None
            except Exception as e:
                print(f"  skip image on page {page_num}: {e}", file=sys.stderr)
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="Path to PDF file")
    parser.add_argument("--out", type=Path, default=Path("study"), help="Output base dir (default: study/)")
    parser.add_argument("--no-images", action="store_true", help="Skip image extraction")
    args = parser.parse_args()

    if not args.pdf.exists():
        sys.exit(f"PDF not found: {args.pdf}")

    slug = slugify(args.pdf.stem)
    out_dir = args.out / slug
    chapters_dir = out_dir / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)

    print(f"Opening {args.pdf}...")
    doc = pymupdf.open(args.pdf)
    print(f"  {len(doc)} pages")

    chapters = extract_chapters_from_toc(doc)
    if chapters and len(chapters) >= 3:
        print(f"  using PDF bookmarks: {len(chapters)} chapters")
    else:
        print("  no usable PDF bookmarks — falling back to font-size heuristic")
        heading_sizes = detect_heading_sizes(doc)
        print(f"  heading sizes detected: {sorted(heading_sizes, reverse=True)}")
        chapters = extract_chapters_by_font(doc, heading_sizes)
        print(f"  {len(chapters)} chapters")

    for idx, chapter in enumerate(chapters, 1):
        write_chapter(chapter, idx, chapters_dir)
    write_toc(chapters, out_dir, args.pdf.stem)

    if not args.no_images:
        n = extract_images(doc, out_dir)
        print(f"  {n} images extracted")

    print(f"\nDone. See {out_dir}/TOC.md")


if __name__ == "__main__":
    main()
