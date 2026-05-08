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
- [Proxy vs Reverse Proxy](proxy-vs-reverse-proxy.md) — *A proxy hides clients. A reverse proxy hides servers. Same trick, opposite direction.*
- [Content Delivery Network (CDN)](cdn.md) — *Move the content closer to the user. Latency drops. Origin breathes.*
- [Caching Strategies](caching-strategies.md) — *Why ask twice? Caching is the laziness that makes systems fast.*
- [Redis & In-Memory Data Stores](redis-in-memory-stores.md) — *RAM speed, with a knob for how much durability you can afford to lose.*

**Data layer**

- [SQL Fundamentals](sql-fundamentals.md) — *Sixty years in, still the lingua franca of data.*
- [Database Types (SQL, NoSQL, and Beyond)](database-types.md) — *Fit, not religion. Pick the database that matches how you read and write.*
- [ACID, CAP, and BASE](acid-cap-base.md) — *Three acronyms decide what your database can actually promise.*
- [Database Sharding](database-sharding.md) — *When one DB isn't enough, split it — carefully. You don't get to undo this.*
- [Object Storage](object-storage.md) — *Cheap, durable, infinite — and the wrong tool for half the things people use it for.*

**Foundation tier complete.**

---

## Patterns tier

The composable building blocks — auth, API design, distributed coordination, cloud infrastructure.

**Auth & security**

- [Cookies, Sessions, and Tokens](cookies-sessions-tokens.md) — *Three ways to remember who you are. Pick by who holds the state.*
- [OAuth 2.0 and JWT](oauth-jwt.md) — *Delegation plus signed receipts. One app acting for a user, with proof.*
- [HTTPS, SSL/TLS, and Encryption](https-ssl-encryption.md) — *Identity and secrecy, agreed in one handshake.*

**API design**

- [REST API Design & Authentication](rest-api.md) — *REST isn't a spec, it's a vibe. Predictable conventions are the product.*
- [API Styles Compared](api-styles-compared.md) — *Different tools for different conversations. Match the style to the call pattern, not the hype.*
- [GraphQL Deep Dive](graphql.md) — *Ask for exactly what you need. Get exactly that. One round trip.*
- [gRPC Deep Dive](grpc.md) — *HTTP/2 plus Protobuf plus codegen. The trifecta that owns the data center.*
- [Webhooks vs Polling](webhooks.md) — *Stop asking. Get called back.*
- [API Gateway](api-gateway.md) — *One front door. Many backends. Cross-cutting concerns handled once.*

**Distributed patterns**

- [Microservices Architecture](microservices.md) — *An org problem, not a tech problem. Don't take the trade until you have the problem.*
- [Message Queues & Brokers](message-queues.md) — *Drop the message, walk away. The broker delivers — eventually.*
- [Event Sourcing & Event-Driven Architecture](event-sourcing.md) — *Don't store what is. Store what happened. State becomes a function of history.*
- [Distributed System Patterns](distributed-patterns.md) — *Survival tools for the chaos. Distributed systems lie — these patterns are how you survive the lies.*
- [Observability — Logs, Metrics, Traces](observability.md) — *Three pillars turn 'it's broken' into 'here's why' — without SSH-ing into 30 boxes.*

**Cloud & infrastructure**

- [Containers & Docker](containers-docker.md) — *Package the app and its world. Same image, anywhere.*
- [Kubernetes](kubernetes.md) — *Declarative orchestration. You describe the cluster you want; k8s makes it real.*
- [Cloud-Native Architecture](cloud-native.md) — *Design for the cloud, not in spite of it.*
- [CI/CD Pipelines](ci-cd.md) — *Small changes, automated safety, ship daily. The big-batch release is dead for a reason.*

**Patterns tier complete.** Next: real systems case studies.

---

## Patterns tier *(coming soon)*

Microservices, message queues, pub/sub, API gateway, event sourcing, CQRS, sagas, circuit breakers, rate limiting, idempotency.

---

## Real systems tier *(coming soon)*

The case studies — design Twitter, design Uber, design Netflix, design Stripe. Where the gamified app gets fun.

---

## How this is built

Source PDFs are extracted to a private `study/` folder (gitignored), read for context, then rewritten in SLAM OG voice with new diagrams. Original figures are never republished. See [STUDY.md](https://github.com/yetog/knowledge-base/blob/main/STUDY.md) for the workflow.
