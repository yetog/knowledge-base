---
tags:
  - system-design
  - course
---

# System Design — SLAM OG

> The OG's guide to building systems that actually scale.

This course rebuilds system design from first principles, in plain language. No buzzword bingo. No corporate hand-waving. Real engineering decisions and the trade-offs they cost.

Each topic delivers:

- A 1-line hook — *why this matters*
- The core concept in 8 minutes or less
- A diagram you can sketch on a napkin
- A real-world example (Netflix, Twitter, Stripe — wherever the pattern actually shows up)
- A "test yourself" quiz embedded in the page metadata

The same content powers the **SLAM OG System Design app** — one source, two consumers.

---

## Foundation tier

The ~12 things every backend engineer should be able to explain in their sleep.

- [Load Balancers](load-balancers.md) — *Traffic cop for your servers. No load balancer, no scale.*

*More foundation topics ship as we expand the pilot — caching, CDNs, databases, replication, sharding, consistency.*

---

## Patterns tier *(coming soon)*

Microservices, message queues, pub/sub, API gateway, event sourcing, CQRS, sagas, circuit breakers, rate limiting, idempotency.

---

## Real systems tier *(coming soon)*

The case studies — design Twitter, design Uber, design Netflix, design Stripe. Where the gamified app gets fun.

---

## How this is built

Source PDFs are extracted to a private `study/` folder (gitignored), read for context, then rewritten in SLAM OG voice with new diagrams. Original figures are never republished. See [STUDY.md](https://github.com/yetog/knowledge-base/blob/main/STUDY.md) for the workflow.
