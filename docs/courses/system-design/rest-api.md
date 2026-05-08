---
slug: rest-api
title: REST API Design & Authentication
tagline: "REST isn't a spec, it's a vibe. Predictable conventions are the product."
tier: patterns
difficulty: intermediate
estimated_minutes: 11
prerequisites: [http-fundamentals]
related: [api-styles-compared, oauth-jwt, api-gateway, http-fundamentals]
tags:
  - system-design
  - course
  - api
  - rest
  - patterns
quiz:
  - q: "You design `POST /getUserOrders?id=42` to fetch a user's orders. What's the REST violation?"
    options:
      - "POST should be GET, and the URL should be `/users/42/orders`"
      - "Nothing — it works fine"
      - "You forgot to add a version number"
      - "You should use PUT instead"
    answer: 0
    explain: "REST treats URLs as resource paths (nouns) and HTTP verbs as actions. Fetching is a GET, the resource is `/users/42/orders`. `getUserOrders` is RPC-style thinking — the verb is in the path instead of the method. Consumers expect the convention."
  - q: "Why does Stripe ask clients to send an `Idempotency-Key` header on POST `/charges`?"
    options:
      - "To rate-limit the client"
      - "So the client can retry safely without double-charging"
      - "To authenticate the request"
      - "To version the API"
    answer: 1
    explain: "POST is not idempotent by default — fire it twice, you create two charges. An idempotency key lets the server recognize the retry and return the same response without re-running the work. This is the Stripe quality bar for any non-idempotent operation."
  - q: "Your API returns `429 Too Many Requests`. What should the client do?"
    options:
      - "Retry immediately in a tight loop"
      - "Crash and report a bug"
      - "Back off, ideally honoring a `Retry-After` header"
      - "Switch to a different endpoint"
    answer: 2
    explain: "429 means rate-limited. The polite client backs off — exponential backoff with jitter, or honoring `Retry-After` if the server provides it. Tight retry loops just make the problem worse and may get the client banned."
---

# REST API Design & Authentication

> REST isn't a spec, it's a vibe. Predictable conventions are the product.

## The hook

REST won the API wars of the 2010s because the conventions were *good enough* and the tooling was everywhere. Curl, Postman, every language's HTTP library — they all spoke the same dialect.

Building a clean REST API is mostly about being predictable. Resources as nouns. Verbs as actions. Status codes as outcomes. Get the conventions right and integrations get easy. Get them wrong and every consumer pays the price — guessing endpoints, parsing weird errors, retrying the wrong way.

The good APIs feel obvious. That obviousness is the whole craft.

## The concept

REST is a set of conventions for building HTTP APIs around **resources**. Five things matter:

- **Resource-based URLs** — paths are nouns. `/users/42/orders`, not `/getOrdersForUser?id=42`.
- **HTTP verbs as actions** — GET reads, POST creates, PUT replaces, PATCH updates, DELETE removes.
- **Status codes as outcomes** — 2xx success, 4xx the client did something wrong, 5xx the server did.
- **Stateless** — every request carries its own context. No server-side session juggling between calls.
- **Hypermedia (HATEOAS)** — responses link to related actions. Beautiful in theory, mostly skipped in practice.

If you nail the first four, you have a REST API people can use without reading much documentation. That's the bar.

## Diagram

```mermaid
flowchart LR
    A[/users/] -->|GET list, POST create| B[/users/{id}/]
    B -->|GET, PUT, PATCH, DELETE| C[/users/{id}/orders/]
    C -->|GET list, POST create| D[/users/{id}/orders/{order_id}/]
    D -->|GET, PATCH, DELETE| D
```

The hierarchy reads top-down. Each level is a resource. The verbs at each arrow are the legal actions. A consumer who learns one branch can guess the rest.

## Example — Stripe's API as the gold standard

If you're going to copy one API's conventions, copy Stripe's. It's the design template that has aged best — versioned, predictable, well-documented, and forgiving of network failures.

**URL design**

```
GET  /v1/customers/{id}
GET  /v1/customers/{id}/charges
POST /v1/charges
```

Versioned in the path (`/v1/`). Resources are plural nouns. Nesting reflects ownership — a charge belongs to a customer.

**Verb usage**

GET `/v1/charges/{id}` retrieves a charge. POST `/v1/charges` creates one. There's no DELETE on charges — money already moved. Instead, you POST `/v1/refunds`. That's a semantic choice: model the real-world action, don't pretend a charge can be erased.

**Status codes**

| Code | Meaning |
|---|---|
| 200 | Success |
| 400 | Bad parameters (you sent garbage) |
| 401 | Bad API key |
| 402 | Payment required (card declined, etc.) |
| 404 | Resource doesn't exist |
| 429 | Rate limited — back off |
| 500 | Stripe broke — retry safely |

**Idempotency keys**

POST is not idempotent by default. Stripe lets clients send a header:

```
Idempotency-Key: 7f3a9b2e-5c1d-4e8f-9a0b-2c4d6e8f0a1b
```

Same key, same request body, same response — even if you fire it ten times. The retry safely returns the original charge instead of creating ten. This is the move every payment-style API should copy.

**Pagination**

Cursor-based, not page-number-based:

```
GET /v1/charges?limit=25&starting_after=ch_3NqK...
```

Cursors don't break when records are inserted mid-iteration. Page numbers do.

**Errors**

Structured JSON, every time:

```json
{
  "error": {
    "type": "card_error",
    "code": "card_declined",
    "message": "Your card was declined.",
    "param": "source"
  }
}
```

Consumers can branch on `code` programmatically and show `message` to humans. No guessing.

## Mechanics

**REST conventions**

| Convention | Rule | Example |
|---|---|---|
| URL design | Plural nouns, nested by ownership | `/users/42/orders/100` |
| GET | Safe + idempotent — read only, no side effects | `GET /orders/100` |
| POST | Create; not idempotent (use idempotency keys for safety) | `POST /orders` |
| PUT | Full replace; idempotent | `PUT /orders/100` |
| PATCH | Partial update; should be idempotent | `PATCH /orders/100` |
| DELETE | Remove; idempotent (second delete returns 404 or 204) | `DELETE /orders/100` |
| Status codes | 2xx success, 4xx client fault, 5xx server fault | 200, 201, 204, 400, 401, 404, 429, 500 |
| Versioning | URL path (Stripe, GitHub) or `Accept` header (more REST-pure, less common) | `/v1/...` or `Accept: application/vnd.api.v1+json` |

**Auth methods**

| Method | How it works | When to use |
|---|---|---|
| **API Key** | Static key in a header (`Authorization: Bearer your-api-key-here`) | Server-to-server, internal tools, simple SaaS |
| **Bearer Token (OAuth/JWT)** | Short-lived token issued by an auth flow; sent in `Authorization` header | Public APIs, third-party access, user-delegated permissions |
| **HTTP Basic** | `Authorization: Basic base64(user:password)` | Legacy systems, internal admin tools — only over TLS |
| **HMAC signature** | Client signs the request with a secret; server recomputes and compares | High-security APIs (AWS SigV4 style) — proves integrity, not just identity |
| **mTLS** | Mutual TLS — client presents a certificate, server verifies it | Service-to-service inside a trusted network, regulated environments |

Default: API key for B2B, OAuth/JWT for anything user-facing. Reach for HMAC or mTLS only when the threat model demands it.

## Related concepts

| Concept | What it is | Relevance |
|---|---|---|
| **HTTP fundamentals** | Verbs, status codes, headers, statelessness | REST is the convention layer on top of HTTP. Can't do REST without HTTP fluency. |
| **OAuth / JWT** | Token-based delegated authentication | The default auth mechanism for any user-facing or third-party REST API. |
| **API Gateway** | Front door for APIs — auth, rate limiting, routing, transformation | Where you enforce cross-cutting REST concerns instead of duplicating in every service. |
| **Rate limiting** | Capping requests per client to protect the service | Pairs with REST's `429` status code. Every public API needs it. |
| **Idempotency** | Safe-to-retry semantics for non-idempotent operations | The Stripe-style `Idempotency-Key` is how you make POST safe across network failures. |
| **API versioning** | Path (`/v1/`) or header-based versioning | Lets you evolve the API without breaking existing clients. |
| **GraphQL** | Single endpoint, client-specified queries | The main alternative to REST when nested fetches dominate the workload. |
| **gRPC** | Binary RPC over HTTP/2 with schema-first contracts | Service-to-service alternative when throughput and tight contracts matter more than browser tooling. |

## When (and when not) to use REST

**Use REST when:**

- You're building a **public-facing API** — REST has the broadest tooling, docs, and developer familiarity
- You have a **mix of clients** (web, mobile, third-party integrators) — every language has a clean HTTP client
- Your domain is **CRUD-heavy** and maps cleanly to resources (users, orders, posts, files)
- You want **maximum tooling support** — Postman, OpenAPI, curl, every API gateway on the planet

**Skip REST when:**

- The frontend does **heavy nested fetches** (a screen needs user + posts + comments + author of each comment) — GraphQL collapses that into one round trip
- You need **service-to-service at high throughput** — gRPC's binary framing and HTTP/2 streams beat JSON over HTTP/1.1
- You need **real-time bidirectional** updates — WebSockets or Server-Sent Events, not REST polling
- Your domain is **fundamentally action-oriented**, not resource-oriented — `cancelSubscription`, `runPayroll`, `triggerExport` may be more honest as RPC than as forced-into-REST nouns

REST isn't always the right tool. But it's almost always the right *default* for an external-facing HTTP API in 2026.

## Key takeaway

- **REST is conventions, not a strict spec** — the value is in being predictable to consumers
- **Resources as nouns, verbs as actions, status codes as outcomes** — get those three right and 80% of the design lands
- **Idempotency keys on POST** are the Stripe quality bar — copy them for any operation where retries cost money
- **Cursor pagination beats page numbers** once data starts moving
- **HATEOAS sounds great, almost nobody ships it** — don't feel bad about skipping it
- **Auth: API key for internal/B2B, OAuth/JWT for user-facing** — anything else needs a specific reason

---

*Quiz available in the SLAM OG app — three questions on REST conventions, idempotency, and status code semantics.*
