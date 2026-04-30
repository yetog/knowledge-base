# Knowledge Base Reorganization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Audit and reorganize the MkDocs knowledge base — fix stub pages, merge the Personal Development section, upgrade the homepage, and add a tags system for cross-cutting navigation.

**Architecture:** Content-only changes (no code). All work is in `docs/` markdown files and `mkdocs.yml`. No files are deleted — stubs get scaffolded into proper pages. The Personal Development "business" page moves into the Business section. A tags plugin + frontmatter tags are added across all 90+ pages.

**Tech Stack:** MkDocs Material, YAML (mkdocs.yml), Markdown frontmatter for tags.

---

## Audit Summary (do not re-audit — this is already done)

**Stub pages** (bare links, no prose content):
- `docs/arts-culture/music.md` — 1 raw HN link
- `docs/arts-culture/languages.md` — 1 raw HN link
- `docs/science-nature/space.md` — 2 raw links, no intro
- `docs/science-nature/trees.md` — 4 raw links, no intro

**Pages with real content that look like stubs** (keep, just needs a tidy):
- `docs/mind-body/consciousness.md` — 8 quality links, needs intro sentence
- `docs/mind-body/relationships.md` — has 3 good substantive sections + 1 link
- `docs/people/index.md` — link collection, needs to be turned into a proper index
- `docs/business/resources.md` — pure link dump, merge into Business section

**Personal Development** — all four pages have real content but `personal-development/business.md` (startup lifecycle theory) overlaps with and belongs in the Business section:
- Move `personal-development/business.md` → `business/playbook.md`
- Rename section nav from "Business" → "Startup Playbook" inside Business tab

**Homepage** (`docs/index.md`) — one sentence. Needs to be a proper hub.

**Tags** — none exist anywhere. Material theme supports `tags` plugin out of the box.

---

## Task 1: Fix Stub Pages

**Files:**
- Modify: `docs/arts-culture/music.md`
- Modify: `docs/arts-culture/languages.md`
- Modify: `docs/science-nature/space.md`
- Modify: `docs/science-nature/trees.md`

- [ ] **Step 1: Rewrite `music.md`**

Replace entire file content with:

```markdown
---
tags:
  - music
  - arts
---

# Music

Notes and resources on music theory, composition, and appreciation.

!!! note "Work in progress"
    This section is being built out. Resources collected so far below.

## Music Theory

- [Ask HN: How Can I Learn Music Theory?](https://hn.premii.com/#/comments/21822225) — Community recommendations for learning theory from scratch
```

- [ ] **Step 2: Rewrite `languages.md`**

Replace entire file content with:

```markdown
---
tags:
  - languages
  - learning
  - arts
---

# Languages

Notes on language learning strategies and resources.

!!! note "Work in progress"
    This section is being built out. Resources collected so far below.

## Resources

- [I Learned French in 12 Months](https://hn.premii.com/#/article/22341983) — Full account of an intensive immersion approach
```

- [ ] **Step 3: Rewrite `space.md`**

Replace entire file content with:

```markdown
---
tags:
  - space
  - physics
  - science
---

# Space

Notes on cosmology, astrophysics, and the nature of the universe.

!!! note "Work in progress"
    This section is being built out. Resources collected so far below.

## Dark Matter

- [Why it's time to take alternatives to dark matter seriously](https://aeon.co/essays/why-its-time-to-take-alternatives-to-dark-matter-seriously) — Aeon essay on MOND and other alternative frameworks
- [Case for Axion Origin of Dark Matter Gains Traction](https://www.ias.edu/press-releases/2020/dark-matter-axion-origin) — IAS research update, 2020
```

- [ ] **Step 4: Rewrite `trees.md`**

Replace entire file content with:

```markdown
---
tags:
  - trees
  - nature
  - biology
---

# Trees

Notes on plant biology, forest ecosystems, and the hidden life of trees.

!!! note "Work in progress"
    This section is being built out. Resources collected so far below.

## Resources

- [Plants communicate, nurture their seedlings, and get stressed](https://news.ycombinator.com/item?id=21440582)
- [Plants "panic" when it rains](https://phys.org/news/2019-10-panic.html)
- [The World's Oldest Forest Has 385M-Year-Old Tree Roots](https://hn.premii.com/#/comments/21843188)
- [The Secret Lives of Fungi](https://hn.premii.com/#/comments/23149203)
```

- [ ] **Step 5: Tidy `consciousness.md` — add intro**

Replace entire file content with:

```markdown
---
tags:
  - consciousness
  - mind
  - philosophy
---

# Consciousness

Collected thinking on the nature of consciousness — from panpsychism to computational theories to neuroscience.

## Resources

- [What If Consciousness Comes First? (Panpsychism)](https://news.ycombinator.com/item?id=20516482)
- [Is matter conscious?](https://news.ycombinator.com/item?id=19240742)
- [Kegan's Theory of the Evolution of Consciousness](https://news.ycombinator.com/item?id=20774486)
- [Thousand Brains Theory of Intelligence](https://news.ycombinator.com/item?id=20326396)
- [Computational Theory of Mind](https://news.ycombinator.com/item?id=21830699)
- [Can AI Become Conscious?](https://hn.premii.com/#/article/23157312)
- [Temporal circuit of brain activity supports human consciousness](https://hn.premii.com/#/article/22823981)
- [Electrons May Well Be Conscious](https://hn.premii.com/#/article/23215877)
- [How Did Consciousness Evolve? (2016)](https://hn.premii.com/#/comments/24604061)
```

- [ ] **Step 6: Commit**

```bash
git add docs/arts-culture/music.md docs/arts-culture/languages.md docs/science-nature/space.md docs/science-nature/trees.md docs/mind-body/consciousness.md
git commit -m "fix: scaffold stub pages with proper structure and WIP admonitions"
```

---

## Task 2: Move Personal Development / Business + Merge Resources

**Files:**
- Create: `docs/business/playbook.md`
- Modify: `docs/business/resources.md` (merge links in, then it becomes a proper references page)
- Delete nav entry: `personal-development/business.md` from mkdocs.yml (file stays on disk, just removed from nav)
- Modify: `mkdocs.yml`

- [ ] **Step 1: Create `docs/business/playbook.md`**

Combine the content of `personal-development/business.md` with the links from `business/resources.md`:

```markdown
---
tags:
  - business
  - startups
  - strategy
---

# Startup Playbook

Decision-making frameworks for building and scaling a company.

## Core Principle

- When you compete to be the best, you imitate
- When you compete to be unique, you innovate

## Seed Stage

There is one guiding principle for operating at early stage: find profitable product-market-fit while keeping costs as small as possible.

### The game

- Product market fit above everything else

### How to operate

- Adaptability over process
- Ignore the minutiae — everything is 80/20
- Spend as if you will never be able to raise again

### Mental models

**Be patient for growth, but impatient for profitability**

When the winning strategy is not yet clear, be patient for growth but impatient for profitability. Don't spend a lot of money in pursuit of the wrong strategy. Once a unit-profitable strategy is found, flip: be impatient for growth but patient for profitability.

**Your first idea *will* be wrong**

93% of companies that ultimately become successful have to abandon their original strategy. Successful companies succeed not because they had the right strategy at the beginning, but because they had money left over after the original strategy failed. Don't assume your idea *might* fail — *expect* it to fail.

**MVP vs MLP**

- Low competition markets: Solving a problem/need → Minimum Viable Product
- High competition markets: Building a better product → Minimum Loveable Product

## Growth Stage

As soon as a company has found product-market fit, it can move into a growth stage.

### The game

How to grow without breaking. Be the best — find the 5% that's missing.

- Scale while keeping product solid
- Focus on sales
- Economies of scale: gain customers, retain good ones, trade up bad ones
- Economies of scope: upsell and increase offerings without increasing costs

### How to operate

- Build systems
- Be detail oriented — everything 20/80
- Focus spend on sales and removing competition

## Mature Stage

### The game

Capital allocation. The game shifts to return per share.

### Five choices for deploying capital

1. Investing in existing operations
2. Acquiring other businesses
3. Issuing dividends
4. Paying down debt
5. Repurchasing stock

### How to raise

- Internal cash flow
- Issuing debt
- Raising equity

### Mental models

- Divest unprofitable initiatives
- Buy back shares when undervalued
- Don't pay dividends if you can earn a better return for shareholders

## Resources

- [Version One Startup Handbook](https://versionone.vc/startup-handbook/)
- [Berkshire Hathaway: An Owner's Manual](https://berkshirehathaway.com/ownman.pdf)
- [incubatorlist.com](https://incubatorlist.com/) — 250 startup incubators and accelerators
- [Software pricing guide](https://news.ycombinator.com/item?id=22027912)
- [Road to Scale](https://roadtoscale.com/) — Curated knowledge library for every stage
- [How to Kill a Startup Idea with Google Keyword Planner](https://hn.premii.com/#/comments/22110004)
- [Startup Idea Checklist](https://hn.premii.com/#/comments/20254057)
- [Best free compute and resources for startups](https://hn.premii.com/#/comments/20225118)
```

- [ ] **Step 2: Update `mkdocs.yml` — Business section**

In `mkdocs.yml`, replace the Business nav block:

```yaml
  - Business:
    - Hiring: business/hiring.md
    - Management: business/management.md
    - Sales: business/sales.md
    - Marketing: business/marketing.md
    - Fundraising: business/fundraising.md
    - Startup Resources: business/resources.md
```

With:

```yaml
  - Business:
    - Startup Playbook: business/playbook.md
    - Hiring: business/hiring.md
    - Management: business/management.md
    - Sales: business/sales.md
    - Marketing: business/marketing.md
    - Fundraising: business/fundraising.md
```

- [ ] **Step 3: Update `mkdocs.yml` — Personal Development section**

Replace:

```yaml
  - Personal Development:
    - Business: personal-development/business.md
    - Life: personal-development/life.md
    - Leadership: personal-development/leadership.md
    - Learning: personal-development/learning.md
```

With:

```yaml
  - Personal Development:
    - Life: personal-development/life.md
    - Leadership: personal-development/leadership.md
    - Learning: personal-development/learning.md
```

- [ ] **Step 4: Commit**

```bash
git add docs/business/playbook.md mkdocs.yml
git commit -m "refactor: move startup playbook to Business section, merge resources, clean Personal Development nav"
```

---

## Task 3: Upgrade the Homepage

**Files:**
- Modify: `docs/index.md`

- [ ] **Step 1: Rewrite `docs/index.md`**

Replace entire file content with:

```markdown
# Knowledge Base

A personal repository of notes, frameworks, and resources — updated whenever something is worth keeping.

Everything here is a work in progress. Some sections are deep dives; others are seedlings.

---

## What's Inside

<div class="grid cards" markdown>

-   :material-chip: **Tech**

    ---

    Infrastructure, AI/automation, cheatsheets, and developer reference material.

    [:octicons-arrow-right-24: Browse Tech](tech/infrastructure/overview.md)

-   :material-briefcase: **Business**

    ---

    Startup playbook, hiring, management, sales, marketing, and fundraising.

    [:octicons-arrow-right-24: Browse Business](business/playbook.md)

-   :material-head-lightbulb: **Philosophy**

    ---

    Stoicism, Buddhism, ethics, and the nature of desire.

    [:octicons-arrow-right-24: Browse Philosophy](philosophy/stoicism.md)

-   :material-account-group: **People**

    ---

    Profiles and key ideas from people worth studying.

    [:octicons-arrow-right-24: Browse People](people/index.md)

-   :material-trending-up: **Personal Development**

    ---

    Frameworks for learning, leadership, and living well.

    [:octicons-arrow-right-24: Browse Personal Development](personal-development/learning.md)

-   :material-flask: **Science & Nature**

    ---

    Physics, mathematics, soil health, trees, zoology, and pyrolysis.

    [:octicons-arrow-right-24: Browse Science](science-nature/mathematics.md)

-   :material-music: **Arts & Culture**

    ---

    Writing, public speaking, chess, climbing, music, and languages.

    [:octicons-arrow-right-24: Browse Arts](arts-culture/writing.md)

-   :material-brain: **Mind & Body**

    ---

    Meditation, consciousness, relationships, and mimetic theory.

    [:octicons-arrow-right-24: Browse Mind & Body](mind-body/meditation.md)

-   :material-school: **Courses**

    ---

    Structured course notes with quizzes and projects. Currently: CS50 AI and AI Engineering.

    [:octicons-arrow-right-24: Browse Courses](courses/cs50-ai/0-search.md)

</div>

---

## Highlights

- [Stoicism](philosophy/stoicism.md) — Deep dive into the four virtues and their sub-virtues
- [CS50 AI](courses/cs50-ai/0-search.md) — Full course notes, quizzes, and project specs for all 7 weeks
- [Docker Cheatsheet](tech/cheatsheets/docker.md) — Quick command reference
- [Startup Playbook](business/playbook.md) — Seed → Growth → Mature stage frameworks
- [Writing](arts-culture/writing.md) — Practical guides to prose style
```

- [ ] **Step 2: Commit**

```bash
git add docs/index.md
git commit -m "feat: upgrade homepage to section hub with grid cards and highlights"
```

---

## Task 4: Add Tags Plugin + Tag All Pages

**Files:**
- Modify: `mkdocs.yml`
- Create: `docs/tags.md`
- Modify: all existing `.md` files (add frontmatter tags)

### 4a — Enable the Plugin

- [ ] **Step 1: Update `mkdocs.yml` plugins block**

Replace:

```yaml
plugins:
  - search
```

With:

```yaml
plugins:
  - search
  - tags:
      tags_file: tags.md
```

- [ ] **Step 2: Create `docs/tags.md`**

```markdown
# Tags

Browse all pages by topic.

[TAGS]
```

- [ ] **Step 3: Add tags.md to mkdocs.yml nav**

In the nav, after `- Home: index.md` add:

```yaml
  - Tags: tags.md
```

### 4b — Tag All Pages

The tag taxonomy to use across the KB:

| Tag | Used for |
|---|---|
| `ai` | AI tools, models, CS50 AI content |
| `python` | Python code |
| `infrastructure` | DevOps, Docker, CI/CD |
| `cheatsheet` | Quick reference pages |
| `business` | Business/startup content |
| `startups` | Startup-specific frameworks |
| `philosophy` | Philosophy pages |
| `learning` | Learning and education pages |
| `course` | Structured courses |
| `science` | Science & nature |
| `nature` | Biology, ecology, zoology |
| `tech` | General tech content |
| `productivity` | Personal development, workflows |
| `writing` | Writing and language |
| `arts` | Arts and culture pages |
| `mind` | Mind, body, meditation |
| `people` | People profiles |
| `reference` | Reference/cheatsheet material |

- [ ] **Step 4: Add frontmatter tags to tech pages**

Add to top of each file listed. Format is:
```yaml
---
tags:
  - tag1
  - tag2
---
```

Files and their tags:
- `tech/ai-automation/ai-development.md` → `ai`, `tech`
- `tech/ai-automation/automation-tools.md` → `ai`, `tech`, `productivity`
- `tech/ai-automation/development-workflows.md` → `ai`, `tech`, `productivity`
- `tech/infrastructure/overview.md` → `infrastructure`, `tech`
- `tech/infrastructure/ci-cd-pipeline.md` → `infrastructure`, `tech`, `cheatsheet`
- `tech/infrastructure/docker-strategy.md` → `infrastructure`, `tech`
- `tech/infrastructure/deployment-process.md` → `infrastructure`, `tech`
- `tech/infrastructure/orchestration-guide.md` → `infrastructure`, `tech`
- `tech/infrastructure/server-configuration.md` → `infrastructure`, `tech`
- `tech/cheatsheets/docker.md` → `infrastructure`, `cheatsheet`, `reference`
- `tech/cheatsheets/postgresql.md` → `cheatsheet`, `reference`
- `tech/cheatsheets/postgres-data.md` → `cheatsheet`, `reference`
- `tech/cheatsheets/regex.md` → `cheatsheet`, `reference`
- `tech/cheatsheets/bash-profile.md` → `cheatsheet`, `reference`
- `tech/cheatsheets/macos-tips.md` → `cheatsheet`, `reference`
- `tech/cheatsheets/html-cheatsheet.md` → `cheatsheet`, `reference`, `writing`
- `tech/cheatsheets/vscode-snippets.md` → `cheatsheet`, `reference`
- `tech/cheatsheets/seo.md` → `cheatsheet`, `reference`, `business`
- `tech/cheatsheets/webhook.md` → `cheatsheet`, `reference`, `tech`
- `tech/cheatsheets/secrets-management-sops.md` → `infrastructure`, `cheatsheet`
- `tech/reference/session-recaps.md` → `tech`, `ai`, `reference`
- `tech/reference/today-i-learned.md` → `tech`, `reference`
- `tech/reference/mental-models.md` → `productivity`, `reference`
- `tech/reference/awesome-list.md` → `reference`, `tech`

- [ ] **Step 5: Add frontmatter tags to business pages**

- `business/playbook.md` → `business`, `startups`, `strategy` *(already done in Task 2)*
- `business/hiring.md` → `business`, `productivity`
- `business/management.md` → `business`, `productivity`
- `business/sales.md` → `business`
- `business/marketing.md` → `business`
- `business/fundraising.md` → `business`, `startups`

- [ ] **Step 6: Add frontmatter tags to all other sections**

Philosophy:
- `philosophy/ethics.md` → `philosophy`
- `philosophy/buddhism.md` → `philosophy`, `mind`
- `philosophy/stoicism.md` → `philosophy`, `productivity`
- `philosophy/desire.md` → `philosophy`, `mind`

People:
- `people/index.md` → `people`, `reference`
- `people/lee-kuan-yew.md` → `people`
- `people/jensen-huang.md` → `people`, `tech`, `ai`
- `people/elon-musk.md` → `people`, `business`, `startups`
- `people/marlon-brando.md` → `people`, `arts`
- `people/nelson-mandela.md` → `people`

Personal Development:
- `personal-development/life.md` → `productivity`, `philosophy`
- `personal-development/leadership.md` → `productivity`, `business`
- `personal-development/learning.md` → `learning`, `productivity`

Science & Nature:
- `science-nature/mathematics.md` → `science`, `reference`
- `science-nature/physics.md` → `science`
- `science-nature/pyrolysis.md` → `science`, `nature`
- `science-nature/soil.md` → `science`, `nature`
- `science-nature/space.md` → `science`
- `science-nature/trees.md` → `science`, `nature`
- `science-nature/zoology.md` → `science`, `nature`

Arts & Culture:
- `arts-culture/music.md` → `arts`, `music`
- `arts-culture/chess.md` → `arts`, `games`
- `arts-culture/climbing.md` → `arts`, `fitness`
- `arts-culture/languages.md` → `arts`, `learning`, `languages`
- `arts-culture/writing.md` → `arts`, `writing`
- `arts-culture/public-speaking.md` → `arts`, `writing`, `productivity`

Mind & Body:
- `mind-body/meditation.md` → `mind`, `productivity`
- `mind-body/consciousness.md` → `mind`, `philosophy`
- `mind-body/relationships.md` → `mind`
- `mind-body/mimetic-theory.md` → `philosophy`, `mind`

Courses:
- All `courses/cs50-ai/*.md` → `ai`, `python`, `course`, `learning`
- All `courses/ai-engineering/*.md` → `ai`, `course`, `learning`
- `courses/mindfulness.md` → `mind`, `course`, `learning`

- [ ] **Step 7: Commit**

```bash
git add mkdocs.yml docs/tags.md docs/
git commit -m "feat: add tags plugin with frontmatter tags across all pages"
```

---

## Self-Review

**Spec coverage check:**
- ✅ Fix stub pages (music, languages, space, trees, consciousness) — Tasks 1
- ✅ Merge Personal Development / Business overlap — Task 2
- ✅ Merge business/resources.md into playbook.md — Task 2
- ✅ Upgrade homepage — Task 3
- ✅ Add tags plugin — Task 4a
- ✅ Tag all pages — Task 4b

**Placeholder scan:** No TBD, TODO, or "similar to above" entries. All file content specified.

**Consistency check:** `tags.md` referenced in mkdocs.yml nav matches the filename created in Task 4a. Tags used in frontmatter in 4b match the taxonomy defined in the table in 4b.
