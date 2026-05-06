# Knowledge Base Buildout Plan

**Goal:** Take the knowledge base from "static archive" to "living, reviewable, public-facing learning hub."

**Scope:** 6 phases covering cleanup, plagiarism rewrite, tagging, digests, learning paths, and "living document" features.

**Approach:** Phases are sequenced so earlier work feeds later work. Within phases, mark tasks parallelizable (P) — those can be dispatched to multiple agents simultaneously.

---

## Phase 1 — Cleanup (1–2 hours)

Quick wins that close open loops from the migration.

### Task 1.1 — Build `midjourney-keywords.md`

**File:** `docs/tech/ai-prompts/midjourney-keywords.md` (create)

The original docx was just hyperlinks to Artsy.net. Build it from scratch as a real keyword vocabulary reference.

**Sections to include:**
- Style keywords (cinematic, surreal, hyperrealistic, etc.) grouped by category
- Lighting (golden hour, rim light, volumetric, etc.)
- Camera (35mm, fisheye, macro, drone, etc.)
- Color palettes (muted, vivid, monochrome, pastel)
- Mood descriptors
- Artist references (use category, not specific names — avoids style-mimicry issues)

Frontmatter: `tags: [ai, midjourney, prompts, reference]`

**Done when:** `mkdocs build` no longer warns about a missing nav entry.

### Task 1.2 — Add WTE posts to nav

**File:** `mkdocs.yml`

Currently the 155 blog posts only reach via the index page. Sub-group them by year so they're discoverable.

```yaml
- Tech:
    - Slam OG Tech Blogs:
        - Overview: tech/slam-og-tech-blogs/index.md
        - 2026 Posts: tech/slam-og-tech-blogs/2026.md   # new index page per year
        - 2025 Posts: tech/slam-og-tech-blogs/2025.md
        - 2024 Posts: tech/slam-og-tech-blogs/2024.md
        - 2023 Posts: tech/slam-og-tech-blogs/2023.md
        - 2022 Posts: tech/slam-og-tech-blogs/2022.md
```

**Sub-task:** Create `docs/tech/slam-og-tech-blogs/{year}.md` for each year — each lists posts from that year only.

**Done when:** Posts are reachable via sidebar without depending on the main index.

---

## Phase 2 — Plagiarism Rewrite (4–6 hours, parallelizable)

The WTE posts are someone else's words. Rewrite into your voice before this site goes more public.

### Task 2.1 — Voice/style guide ✅ DONE

**File:** `STYLE.md` (repo root, not published)

Voice locked in: smooth, educational, motivational without being corny. High accessibility. See `STYLE.md` for full rules, banned phrases, and on-voice/off-voice examples.

This is the prompt input for Task 2.2.

### Task 2.2 — Batch rewrite WTE posts (P — 10 agents)

**Files:** `docs/tech/slam-og-tech-blogs/*.md` (excluding `index.md` and year pages)

Dispatch 10 parallel agents, each handling ~15 posts. Each agent:
1. Reads the post
2. Rewrites prose preserving facts/structure but in the voice from STYLE.md
3. Preserves frontmatter (tags, date, source URL — keep the source URL as attribution)
4. Adds frontmatter field `rewritten: true`
5. Writes back to the same file

**Done when:** All 155 posts have `rewritten: true` and have been processed.

### Task 2.3 — Spot-check sample

**Files:** Random sample of 10 rewritten posts.

Read 10 across different years. Confirm voice is consistent and facts weren't drifted. Flag any that need a redo.

**Done when:** You've personally read 10 and signed off.

---

## Phase 3 — Tag the Backlog (3–4 hours, parallelizable)

`tech, blog, wte` tells you nothing. Topic tags turn the archive into a real index.

### Task 3.1 — Topic taxonomy (proposed)

**File:** `TAGS.md` (repo root, internal reference — to be created in execution)

Based on scanning all 155 WTE post titles, here's the proposed taxonomy:

**Topic tags (apply 2–3 per post):**

| Tag | Scope | Est. count |
|---|---|---|
| `ai` | AI tools, LLMs, ChatGPT, Claude, GitHub Copilot, AI workflows | ~50 |
| `cybersecurity` | Breaches, threats, MFA, SSL, sextortion, data leaks | ~15 |
| `marketing` | SEO, content marketing, email, branding, influencer | ~25 |
| `web-development` | Web design, hosting, UX/CX, sites that work | ~20 |
| `ecommerce` | Online stores, AOV, B2B/B2C, checkout | ~8 |
| `cloud` | Cloud backup, NaaS, hosting infrastructure | ~6 |
| `data-protection` | Backups, air-gap, privacy, compliance | ~8 |
| `hardware` | Gadgets, CES, AirTags, consumer tech | ~10 |
| `business-strategy` | AI adoption, productivity, leadership, SaaS | ~20 |
| `industry-commentary` | "Future of," trend pieces, state-of analysis | ~15 |

**Series tags (apply when applicable):**

| Tag | Scope |
|---|---|
| `flipboard-friday` | The weekly Flipboard Friday series (~25 posts) |
| `holiday-guides` | Annual gift guide series (~6 posts) |

**Existing tags retained:** `tech`, `blog`, `wte` (provenance markers — keep on every WTE post)

**Tagging rule:** every post gets the 3 provenance tags + 2–3 topic tags + optional series tag. Range: 5–7 tags per post.

### Task 3.2 — Tag all 155 posts (P — 10 agents)

**Files:** `docs/tech/slam-og-tech-blogs/*.md`

Each agent handles ~15 posts:
1. Reads post content
2. Adds 2–4 topic tags from the taxonomy to the existing `tags:` frontmatter array
3. Writes back

**Done when:** Every post has at least 2 topic tags beyond `tech, blog, wte`.

### Task 3.3 — Audit tags page

**File:** `docs/tags.md`

Read the rendered tags page. Check that each tag in the taxonomy has reasonable post count (> 3). Merge tags that ended up sparse.

**Done when:** Tags page reads as a useful topic index, not noise.

---

## Phase 4 — Key-Insight Digests (3–4 hours)

155 long posts is unreviewable. Surfacing one-line takeaways turns it into a flip-through.

### Task 4.1 — Add `summary` frontmatter (P — 10 agents)

**Files:** `docs/tech/slam-og-tech-blogs/*.md`

Each agent reads ~15 posts and adds a `summary:` field — one sentence, the single most useful takeaway.

```yaml
---
tags: [...]
summary: "MFA stops 99% of automated credential-stuffing attacks; cost is 5 minutes per user to enable."
---
```

**Done when:** Every post has a `summary` field.

### Task 4.2 — Build per-topic digest pages

**Files:** `docs/tech/slam-og-tech-blogs/digests/{topic}.md` (create one per major tag)

Each digest page is a list of post titles + their `summary` lines, grouped by topic. Reading the digest gives you the gist of 15+ posts in 5 minutes.

Auto-generate this from the frontmatter (write a Python script in `scripts/build-digests.py` that reads frontmatter and outputs the digest md files).

**Done when:** Each major tag has a digest page; digests rebuild from a single command.

### Task 4.3 — Update WTE index to surface digests

**File:** `docs/tech/slam-og-tech-blogs/index.md`

Add a "Browse by topic" section at the top linking to each digest page. The year-based listing stays below.

**Done when:** Landing on the WTE index, "topic digests" is the first thing a reader sees.

---

## Phase 5 — Learning Paths (2 hours)

Your courses (GMAT, Coding Bootcamp, CS50 AI, AI Engineering, Processing, Mindfulness) are siloed. A path turns them into a curriculum.

### Task 5.1 — Create `docs/learning-paths.md`

**File:** `docs/learning-paths.md` (create)

Define 3–5 named paths. Examples:
- **AI Engineer Path:** Coding Bootcamp (Java + web) → CS50 AI → AI Engineering → Prompt Engineering
- **Generalist Path:** GMAT → Startup Playbook → Sales/Marketing/Hiring
- **Creative Path:** Processing → MidJourney Guide → Writing → Public Speaking

Each path: prerequisites, ordered course list, estimated hours, what you'll be able to do at the end.

### Task 5.2 — Add path callouts to course index pages

**Files:** Each `docs/courses/*/index.md`

At the top of each course index, add: "Part of: [AI Engineer Path](../../learning-paths.md#ai-engineer-path)"

### Task 5.3 — Add to nav and homepage

**Files:** `mkdocs.yml`, `docs/index.md`

Add `Learning Paths: learning-paths.md` to the top of nav. Feature it on the homepage.

**Done when:** A new visitor can land on the homepage and find a sequenced path in two clicks.

---

## Phase 6 — Living Document Features (2 hours)

The site reads as static. Dated activity makes it feel alive.

### Task 6.1 — Create `docs/now.md` (semi-auto)

**File:** `docs/now.md` (create — inspired by https://nownownow.com)

Two sections, both prepended (newest first):

**Section 1 — Currently focused on (manual, weekly)**
```markdown
## Week of 2026-05-04
- CS50 AI Week 6 — Language (parsing, BERT attention)
- GMAT prep — Quantitative section
- Knowledge base buildout — executing the comprehensive plan
```

**Section 2 — Recent updates (auto-generated by Python script)**

A second Python script: `scripts/build-now.py`. Runs as part of CI before `mkdocs build`.

What it does:
1. Reads `git log` for the last 14 days
2. Filters to commits touching `docs/`
3. Groups by week
4. For each week, lists files changed with their page titles (read from frontmatter)
5. Writes to a markdown block in `docs/now.md` between `<!-- AUTO-START -->` and `<!-- AUTO-END -->` markers (so the manual section is preserved)

This way you only manually update the "focused on" section; "recent updates" populates itself every push.

### Task 6.2 — Add "Active Now" block to homepage

**File:** `docs/index.md`

Above the section grid, add a 3-line block:
> **Active now:** CS50 AI · GMAT prep · Knowledge base buildout. [Full now page →](now.md)

### Task 6.3 — Add to nav

**File:** `mkdocs.yml`

Add `Now: now.md` near the top of nav (after Home, before Tags).

**Done when:** Homepage signals current activity; visitors can tell what's actively being worked on without reading commit history.

---

## Execution order & parallelism

```
Phase 1 ──> Phase 2 ──> Phase 3 ──┐
   (fast)    (parallel) (parallel)│
                                  ├──> Phase 4 (parallel)
                                  │
                                  └──> Phase 5 ──> Phase 6
                                       (sequential, fast)
```

- **Phase 1** unblocks everything else (clean foundation)
- **Phase 2** must precede Phase 3 (don't tag plagiarized content)
- **Phase 3** must precede Phase 4 (digests pull from tags)
- **Phases 5 and 6** are independent of WTE work — can happen any time after Phase 1

**Total estimated time:** 15–22 hours of work, ~half of which is parallelizable agent dispatch.

---

## Per-phase commit strategy

One commit at the end of each phase. Conventional commit prefix:

- Phase 1: `chore: cleanup nav and missing pages`
- Phase 2: `refactor: rewrite WTE blog posts in own voice`
- Phase 3: `feat: tag WTE backlog by topic`
- Phase 4: `feat: add per-topic digest pages and post summaries`
- Phase 5: `feat: add learning paths`
- Phase 6: `feat: add now page and active-now homepage block`

Push after each commit so CI deploys incrementally.

---

## Decisions locked in

1. **Voice** — smooth, educational, motivational without being corny. See `STYLE.md`.
2. **Taxonomy** — 10 topic tags + 2 series tags + 3 provenance tags. Defined in Phase 3.1 above.
3. **Digest auto-gen** — Python script (`scripts/build-digests.py`) reads frontmatter, outputs digest pages.
4. **Now page** — semi-auto. Manual "currently focused on" updated weekly + auto-generated "recent updates" from git log via `scripts/build-now.py` running in CI.

## Scripts to build

Three Python scripts go in `scripts/`:

| Script | Purpose | When it runs |
|---|---|---|
| `build-digests.py` | Reads frontmatter `summary` from WTE posts, outputs per-topic digest pages | Pre-build in CI |
| `build-now.py` | Reads git log + frontmatter, fills auto section of `now.md` | Pre-build in CI |
| `update-frontmatter.py` | Helper for batch frontmatter ops (used by Phase 2/3/4 agents) | Manual |

Update `production-deploy.yml` to run scripts before `mkdocs build`:

```yaml
- name: Build dynamic pages
  run: |
    python scripts/build-digests.py
    python scripts/build-now.py

- name: Build site
  run: mkdocs build
```
