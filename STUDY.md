# Study & Rewrite Workflow

How to turn a PDF into SLAM OG branded knowledge base content.

## Setup (once)

```bash
pip install -r requirements.txt
```

## Extract a PDF

```bash
python scripts/extract-pdf.py "path/to/book.pdf"
```

Output lands in `study/{book-slug}/`:

- `TOC.md` — chapter list with word counts (start here)
- `chapters/01-*.md` ... `chapters/NN-*.md` — one file per detected chapter
- `images/` — embedded figures (if any)

`study/` is gitignored. Extracted text never gets published.

## Write a topic page

For each topic you want to cover:

1. Read the relevant chapter(s) in `study/`
2. Pick a slug (e.g., `load-balancers`, `caching-strategies`)
3. Create `docs/courses/system-design/{slug}.md`
4. Use `load-balancers.md` as the template — copy, then replace
5. Fill out frontmatter (slug, title, tagline, tier, difficulty, prereqs, related, quiz)
6. Write the body in SLAM OG voice: hook → concept → diagram → example → key takeaway

## Build the content JSON (for the app)

```bash
python scripts/build-content-json.py
```

Outputs `docs/courses/system-design/content.json` — every topic's frontmatter + body. The SLAM OG app consumes this at build time.

## Diagram conventions

| Choice | When |
|---|---|
| Mermaid (preferred) | Flowcharts, sequence, state, ER diagrams. Renders inline in MkDocs and the app. |
| Excalidraw + SVG | When Mermaid can't capture the visual. Save to `docs/courses/system-design/diagrams/{slug}.svg`, embed via `![](diagrams/foo.svg)`. |

**Never** republish PDF figures. Recreate everything.

## Voice

See `STYLE.md` at repo root. SLAM OG voice = smooth, educational, motivational without corny.

Each topic page opens with a tagline:

```yaml
tagline: "Traffic cop for your servers. No load balancer, no scale."
```

Punchy. Memorable. Captures *why this matters* in one breath.

## Coverage strategy

ByteByteGo Big Archive has roughly 50+ topics. Don't try to cover everything at once.

**Phased:**

| Tier | Topics | Why |
|---|---|---|
| Foundation | Networking, HTTP, DNS, load balancers, caching, CDN, databases (SQL/NoSQL), indexing, replication, sharding, consistency | The ~12 things every backend engineer should know cold |
| Patterns | Microservices, message queues, pub/sub, API gateway, event sourcing, CQRS, sagas, circuit breakers, rate limiting, idempotency | The composable building blocks |
| Real Systems | Design Twitter, Uber, Netflix, YouTube, Stripe | Case studies — where it gets fun in the gamified app |

Foundation tier alone = ~3-week MVP for the app.
