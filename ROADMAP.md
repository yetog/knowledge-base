# Knowledge Base Roadmap

This document tracks the planned evolution of the knowledge base — from the current pre-built HTML setup to a Markdown-first workflow where writing a new page is as simple as creating a `.md` file and pushing to GitHub.

---

## Current State

The site is served by nginx at `https://zaylegend.com/knowledge-base/`. The deploy pipeline works: push to `main` → GitHub Actions → SSH pull on the server → nginx serves static files.

**The problem:** The repo only contains pre-built VuePress 1.x HTML output. There are no Markdown source files. Adding or editing content requires modifying large, complex HTML files by hand — which is fragile and time-consuming.

---

## Phase 1 — Repository Cleanup ✅ Complete

**Goal:** Get the repo into a clean, maintainable state without changing how the site looks or works.

- [x] Delete all 52 `.html.bak` backup files
- [x] Remove `ethics-maci.html` stub (real content lives at `philosophy/ethics.html`)
- [x] Remove `.DS_Store` from git tracking
- [x] Update `.gitignore` to exclude `.DS_Store`, `*.bak`, and future MkDocs `site/` build output
- [ ] Link `infrastructure/` pages in the sidebar (or merge into `tech/`)
  - Currently orphaned: `ci-cd-pipeline.html`, `deployment-process.html`, `docker-strategy.html`, `orchestration-guide.html`, `overview.html`, `server-configuration.html`

---

## Phase 2 — Migrate to Markdown (MkDocs Material)

**Goal:** Write content in plain Markdown. One file = one page. No HTML editing required.

### Why MkDocs Material

- Write pages as `.md` files — no HTML knowledge needed
- Navigation defined in a single `mkdocs.yml` config file
- Adding a new page = create the file + one line in the config
- Built-in full-text search, syntax highlighting, mobile-responsive
- GitHub Actions builds the site automatically on every push

### Proposed folder structure

```
knowledge-base/
  mkdocs.yml              ← all navigation config lives here
  docs/
    index.md
    tech/
      ai-development.md
      automation-tools.md
      development-workflows.md
      session-recaps.md
      today-i-learned.md
      docker.md
      postgresql.md
      bash-profile.md
      macos-tips.md
      regex.md
      html-cheatsheet.md
      vscode-snippets.md
      seo.md
      webhook.md
      secrets-management-sops.md
      mental-models.md
      awesome-list.md
    infrastructure/         ← currently orphaned, will be linked
      overview.md
      docker-strategy.md
      ci-cd-pipeline.md
      deployment-process.md
      orchestration-guide.md
      server-configuration.md
    business/
      hiring.md
      management.md
      sales.md
      marketing.md
      fundraising.md
      resources.md
    philosophy/
      ethics.md
      buddhism.md
      stoicism.md
      desire.md
    people/
      index.md
      lee-kuan-yew.md
      jensen-huang.md
      elon-musk.md
      marlon-brando.md
      nelson-mandela.md
    personal-development/   ← replaces vague "Levels" label
      business.md
      life.md
      leadership.md
      learning.md
    science-nature/         ← pulled out of "Miscellaneous"
      space.md
      soil.md
      trees.md
      zoology.md
      pyrolysis.md
      physics.md
      mathematics.md
    arts-culture/           ← pulled out of "Miscellaneous"
      music.md
      chess.md
      climbing.md
      languages.md
      writing.md
      public-speaking.md
    mind-body/              ← pulled out of "Miscellaneous"
      meditation.md
      consciousness.md
      relationships.md
      mimetic-theory.md
    courses/
      ai-engineering/
        index.md
        syllabus.md
        foundations.md
        core-applications.md
        advanced-techniques.md
        capstone-advanced.md
      mindfulness.md
  site/                     ← built output, gitignored
```

### Steps

1. **Install MkDocs Material locally**
   ```bash
   pip install mkdocs-material
   ```

2. **Create `mkdocs.yml`** with navigation matching the structure above

3. **Convert HTML → Markdown** — extract the content from each page's `content__default` div and convert to `.md`

4. **Test locally**
   ```bash
   mkdocs serve   # live preview at localhost:8000
   ```

5. **Update GitHub Actions** (`production-deploy.yml`) to build then rsync

---

## Phase 3 — Updated Deploy Pipeline

**Goal:** Replace the current `git pull` on the server with a proper build-then-deploy step.

### New workflow (on push to `main`)

```yaml
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install MkDocs Material
        run: pip install mkdocs-material

      - name: Build site
        run: mkdocs build

      - name: Deploy to server
        uses: appleboy/ssh-action@v0.1.7
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            rsync -avz --delete site/ /var/www/zaylegend/apps/knowledge-base/
            sudo systemctl reload nginx
```

**What changes on the server:** Instead of the server running `git pull` and serving raw HTML, GitHub Actions builds the site and rsyncs the output. The server just serves static files — no git, no Python, no build dependencies needed there.

---

## Adding New Content (after Phase 2)

Once the migration is complete, the workflow for adding a new page is:

```bash
# 1. Create the markdown file
echo "# My New Topic\n\nContent here..." > docs/tech/my-new-topic.md

# 2. Add it to mkdocs.yml nav (one line)
# - My New Topic: tech/my-new-topic.md

# 3. Push
git add .
git commit -m "add: my new topic"
git push
```

That's it. GitHub Actions builds and deploys automatically.

---

## Open Questions

- **Theme:** Keep current blue/green color scheme? MkDocs Material supports full color customization via `mkdocs.yml`.
- **Domain:** Does `knowledge-base/` path need to stay the same? (It can — MkDocs supports subdirectory serving.)
- **Infrastructure pages:** Merge into `tech/` or keep as a separate section?
