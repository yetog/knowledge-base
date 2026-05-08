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

The ~15 things every backend engineer should be able to explain in their sleep. The order matters — networking before load balancers, caching before CDNs, SQL before sharding.

**Networking & protocols**

- [Networking Fundamentals](networking-fundamentals.md) — *The internet is just envelopes inside envelopes. Learn the stack, see the system.*
- [HTTP Fundamentals](http-fundamentals.md) — *The vocabulary of the web. Verbs, codes, and headers — that's the whole game.*
- [URLs, URIs, URNs](urls-uris-urns.md) — *Everyone uses these three letters wrong. Here's the actual hierarchy.*
- [DNS & Internet Traffic Routing](dns-routing.md) — *DNS is the phonebook for the internet — except no one's in charge, and somehow it still works.*
- [Latency Numbers Every Engineer Should Know](latency-numbers.md) — *L1 cache: 0.5ns. Cross-continent: 150ms. Same factor that makes your code fast or slow.*

**Speed & distribution layer**

- [Load Balancers](load-balancers.md) — *Traffic cop for your servers. No load balancer, no scale.*

*More foundation topics ship in the next batches — proxy/CDN, caching, Redis, then the data layer (SQL, database types, ACID/CAP, sharding, object storage).*

---

## Patterns tier *(coming soon)*

Microservices, message queues, pub/sub, API gateway, event sourcing, CQRS, sagas, circuit breakers, rate limiting, idempotency.

---

## Real systems tier *(coming soon)*

The case studies — design Twitter, design Uber, design Netflix, design Stripe. Where the gamified app gets fun.

---

## How this is built

Source PDFs are extracted to a private `study/` folder (gitignored), read for context, then rewritten in SLAM OG voice with new diagrams. Original figures are never republished. See [STUDY.md](https://github.com/yetog/knowledge-base/blob/main/STUDY.md) for the workflow.
