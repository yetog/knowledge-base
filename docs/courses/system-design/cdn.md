---
slug: cdn
title: Content Delivery Network (CDN)
tagline: "Move the content closer to the user. Latency drops. Origin breathes."
tier: foundation
difficulty: beginner
estimated_minutes: 9
prerequisites: [networking-fundamentals, dns-routing]
related: [caching-strategies, dns-routing, load-balancers, latency-numbers]
tags:
  - system-design
  - course
  - networking
  - performance
  - foundation
quiz:
  - q: "A user in Tokyo loads your site. The CDN edge in Tokyo has the asset cached. Roughly how long does that request take vs. a round-trip to your origin in Virginia?"
    options:
      - "Same speed — CDN is just a backup"
      - "~10ms cached vs. ~250ms to origin"
      - "Slower — extra hop through the CDN"
      - "Depends entirely on the user's ISP"
    answer: 1
    explain: "Light through fiber takes real time. Tokyo to Virginia is roughly 125ms one way. A cache hit at a local edge avoids that round trip entirely. Cache hit ~10ms is realistic; ~250ms to a transcontinental origin is too."
  - q: "What's the difference between push and pull CDN?"
    options:
      - "Push uses HTTP, pull uses HTTPS"
      - "Push pre-deploys content to edges; pull caches lazily on first request"
      - "Push is for video, pull is for images"
      - "They're the same — different vendors call it different things"
    answer: 1
    explain: "Push CDN means you upload assets to the CDN ahead of time. Pull CDN means the edge fetches from origin the first time someone asks, then caches it. Pull is the default for most sites — easier, but the first user in a region eats the cache miss."
  - q: "Your app serves heavily personalized dashboards — different content per user. Should you put it all behind a CDN?"
    options:
      - "Yes — CDNs cache everything"
      - "No — never use a CDN for dynamic content"
      - "Partially — CDN the static assets (CSS, JS, images); be careful with personalized HTML"
      - "Only if you use Cloudflare"
    answer: 2
    explain: "Static assets (CSS, JS, fonts, images) belong on a CDN no matter what. Personalized HTML is the trap — cache it wrong and User A sees User B's dashboard. Edge compute (Workers, Lambda@Edge) and surrogate keys can help, but the default is: cache the assets, leave the personalized parts dynamic."
---

# Content Delivery Network (CDN)

> Move the content closer to the user. Latency drops. Origin breathes.

## The hook

You're in Sydney. Netflix loads instantly. Your buddy in Los Angeles loads it just as fast. The Netflix origin servers aren't in either of those cities — but the experience feels local to both of you.

That's not magic. That's a CDN.

Without one, every image, video segment, CSS file, and JavaScript bundle would have to travel from a single origin to every user on the planet. Tokyo to Virginia is roughly 125ms one-way at the speed of light through fiber — and that's *before* the server does any work. Multiply that by every asset on the page and your site feels broken.

Move the content closer to the user. That's the whole game.

## The concept

A CDN is a globally distributed cache for content. Hundreds of edge locations spread across the world, each holding copies of your stuff so users hit the nearest one instead of the origin.

Three layers in the typical setup:

1. **Edge nodes** — closest to the user, in major cities. First place a request lands.
2. **Regional caches** — bigger boxes behind the edges. Catch what individual edges miss.
3. **Origin** — your actual server. Source of truth. Should rarely get touched.

Two ways content gets to the edge:

| Mode | How it works | Trade-off |
|---|---|---|
| **Pull** | Edge fetches from origin on first miss, then caches | Easy — first user in a region eats the latency |
| **Push** | You upload assets to the CDN ahead of time | More control, more work — good for big launches and video |

Most sites run pull by default. Push shows up for predictable, high-volume drops (a movie release, a software update).

Beyond static files, modern CDNs cache *and* compute. We'll get to that.

## Diagram

```mermaid
flowchart LR
    U[User in Tokyo] --> E[Edge Node — Tokyo]
    E -->|cache hit ~10ms| U
    E -.miss.-> R[Regional Cache — Asia]
    R -.miss.-> O[Origin — Virginia]
    O --> R
    R --> E
    style E fill:#cfc,stroke:#3a3
    style O fill:#fcc,stroke:#a33
```

The fast path is short: user → edge → user. A miss walks back through regional → origin and pays the full latency tax. Hit rates of 90%+ are normal for a well-tuned CDN.

## Example — Cloudflare serving a real site

Cloudflare runs in **300+ cities across 100+ countries**. They claim ~50ms latency to roughly 95% of the internet's users. Disney+, Stack Overflow, Discord, and a long list of others sit behind it.

Trace a request to a Cloudflare-fronted site from Tokyo:

**Cache hit (the common case):**

1. Browser does DNS lookup → gets a Cloudflare anycast IP
2. Anycast routing sends the packet to the **Tokyo edge** (closest PoP)
3. Edge has the JS bundle cached → returns it
4. Total: **~10–20ms**

**Cache miss (cold asset, new region):**

1. Browser → DNS → Cloudflare anycast → Tokyo edge
2. Tokyo edge: miss. Asks the **regional tier** in Asia.
3. Regional tier: also miss. Goes to **origin in Virginia**.
4. Round trip Tokyo → Virginia → Tokyo: **~250ms** plus origin processing time.
5. Edge stores the response. Next user from Tokyo gets the 10ms version.

That's the asymmetry that makes CDNs worth it. The first user in a region pays. Everyone after is fast. At Disney+ scale — millions of concurrent streams during a Marvel release — that ratio is what keeps the origin from melting.

Stack Overflow uses the same pattern: Cloudflare in front, the actual servers in two data centers in New York and Colorado. A developer in Berlin asking a question hits Cloudflare Frankfurt, gets the cached page, and never knows the origin is across an ocean.

## Mechanics — what CDNs do beyond caching

Caching was the original job. Modern CDNs are closer to "programmable edge networks." Here's what's actually on the menu:

| Feature | What it does | Why it matters |
|---|---|---|
| **TLS termination** | CDN handles HTTPS handshakes at the edge | Faster connections (closer = fewer round trips); origin doesn't burn CPU on TLS |
| **DDoS protection** | Absorbs and filters attack traffic across the global network | Cloudflare can swallow multi-Tbps attacks that would crush any single origin |
| **Image optimization** | On-the-fly resize, format conversion (WebP, AVIF), compression | One image source, dozens of variants — without your team building a pipeline |
| **Edge compute** | Run code at the edge (Cloudflare Workers, Lambda@Edge, Fastly Compute) | Personalize, A/B test, auth — all without going to origin |
| **Bot detection** | Identify and block scrapers, credential stuffers, scalpers | Fewer junk requests reaching your app |
| **WAF (Web Application Firewall)** | Block SQL injection, XSS, common exploits at the edge | Defense in depth — bad requests don't even hit your servers |
| **Smart routing** | Pick faster network paths than the public internet would by default | Argo, Fastly's routing — meaningful for global apps |

Edge compute is the one to watch. Cloudflare Workers can run JavaScript or WASM at every edge location with sub-millisecond cold starts. You can rewrite responses, do auth, run A/B tests, and serve whole APIs without ever hitting your origin.

## Related concepts

| Concept | What it is | How it relates to CDNs |
|---|---|---|
| **Caching strategies** | TTL, cache invalidation, write-through, write-back patterns | A CDN is a giant distributed cache. Same trade-offs apply, just at network scale. |
| **DNS routing** | Mapping a hostname to the right IP based on geography or latency | The routing primitive a CDN uses — Cloudflare, Route 53, NS1 all do geo/latency-based DNS. |
| **Anycast** | One IP advertised from many physical locations; the network picks the closest | How Cloudflare and most modern CDNs route users to the nearest edge with no DNS games. |
| **Load balancers** | Spread traffic across backends; health-check them | CDN is load balancing across the planet. The L4/L7 LB lives behind it at the origin. |
| **Edge compute** | Running application code at CDN PoPs | Cloudflare Workers, Lambda@Edge, Fastly Compute — the new layer between CDN and origin. |
| **HTTP caching headers** | `Cache-Control`, `ETag`, `Last-Modified`, `Vary` | The contract between your origin and the CDN. Get these wrong and the CDN caches the wrong thing. |
| **Origin shield** | An extra cache layer between regional caches and origin | Concentrates misses through one node so origin sees fewer requests during a stampede. |
| **Cache invalidation** | Telling edges that a cached asset is stale | The hardest problem. Purge by URL, by tag, or by wildcard — every CDN solves it differently. |

Each is a topic on its own. CDNs sit on top of all of them.

## When (and when not) to use it

**Use a CDN when:**

- You have **users in more than one region** and any meaningful amount of static content (images, video, CSS, JS, fonts)
- You serve **video or large downloads** — bandwidth at origin gets expensive fast
- You need **DDoS protection** without building it yourself
- You want **TLS termination, image optimization, or a WAF** as a managed service
- You're deploying anything that might **trend or get linked** — a CDN is the cheapest insurance against a traffic spike

**Skip it (or be careful) when:**

- Your audience is **single-region and small** — a CDN adds a hop and a vendor for users who'd hit your origin in 20ms anyway
- You serve **highly personalized dynamic content** (per-user dashboards, real-time feeds) — caching is a footgun unless you've designed for it with edge compute or smart cache keys
- You need **strict data residency** — content cached in 300 cities means data physically lives in 300 jurisdictions. Some compliance regimes care.
- Your budget is **zero** — most CDNs have free tiers (Cloudflare especially), but enterprise pricing scales with bandwidth and can surprise you

The default for any public-facing site with global users and static assets is *yes, put it behind a CDN.* The interesting trade-offs show up around dynamic content, cache invalidation, and cost at scale.

## Key takeaway

- **CDN = global distributed cache.** Edges near users, regional caches behind, origin as source of truth.
- **Cache hits are 10–50ms.** Cache misses pay the full origin round-trip — sometimes 200ms+.
- **Pull by default, push for predictable big drops.** Most sites never need push.
- **Modern CDNs do more than cache** — TLS, DDoS, image optimization, edge compute, WAF. Use them.
- **Cache invalidation and personalized content are the traps.** Get the headers right, and don't cache what shouldn't be cached.

---

*Quiz available in the SLAM OG app — three questions on edge latency, push vs. pull, and what to do with personalized content.*
