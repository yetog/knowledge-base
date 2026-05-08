---
slug: http-fundamentals
title: HTTP Fundamentals
tagline: "The vocabulary of the web. Verbs, codes, and headers — that's the whole game."
tier: foundation
difficulty: beginner
estimated_minutes: 9
prerequisites: [networking-fundamentals]
related: [rest-api, urls-uris-urns, https-ssl-encryption, api-styles-compared]
tags:
  - system-design
  - course
  - networking
  - http
  - foundation
quiz:
  - q: "Which of these HTTP verbs is NOT idempotent?"
    options:
      - "GET"
      - "PUT"
      - "POST"
      - "DELETE"
    answer: 2
    explain: "POST creates a new resource each time you call it — fire it twice, you get two records. GET, PUT, and DELETE all produce the same end state no matter how many times you call them. That's the definition of idempotent."
  - q: "You see a 401 response. What does that actually mean?"
    options:
      - "The server crashed"
      - "You're not logged in (or your token is bad)"
      - "You're logged in but not allowed to do this"
      - "The resource doesn't exist"
    answer: 1
    explain: "401 is 'Unauthorized' — really means unauthenticated. The server doesn't know who you are. 403 is 'Forbidden' — it knows who you are and is saying no. 404 is 'not found.' 5xx codes are server errors."
  - q: "Which header tells the browser how long it can cache a response?"
    options:
      - "Content-Type"
      - "Authorization"
      - "Cache-Control"
      - "User-Agent"
    answer: 2
    explain: "Cache-Control is the modern caching directive — `max-age=3600` means cache for an hour. Content-Type describes the body format. Authorization carries credentials. User-Agent identifies the client."
---

# HTTP Fundamentals

> The vocabulary of the web. Verbs, codes, and headers — that's the whole game.

## The hook

You click a link. A page loads. Feels instant.

Behind that click, your browser opened a TCP connection, wrote a few lines of text, and waited. The server read those lines, did some work, and wrote a few lines back. That conversation is HTTP.

Open Chrome DevTools, hit the Network tab, and reload any page. Every row you see is one HTTP request and one HTTP response. Get fluent in reading those rows and you can debug almost anything that happens on the web.

## The concept

HTTP is a request/response protocol. Client sends a request. Server sends a response. That's it.

Every request has three parts that matter:

1. **A verb** — what you want to do (GET, POST, PUT, DELETE, PATCH)
2. **A URL** — what resource you want to do it to (`/api/users/42`)
3. **Headers** — metadata about the request (who you are, what format you accept, auth tokens)

Every response has three parts that matter:

1. **A status code** — did it work? (200, 404, 500)
2. **Headers** — metadata about the response (content type, cache rules, cookies)
3. **A body** — the actual payload (HTML, JSON, an image, nothing)

That's the whole protocol. Verbs say what. Status codes say how it went. Headers carry everything else.

## Diagram

```mermaid
sequenceDiagram
    participant C as Client (Browser)
    participant S as Server (api.stripe.com)
    C->>S: POST /v1/charges HTTP/1.1<br/>Host: api.stripe.com<br/>Authorization: Bearer sk_test_...<br/>Content-Type: application/json<br/><br/>{"amount": 2000, "currency": "usd"}
    Note over S: Validate auth<br/>Process charge<br/>Write to DB
    S->>C: HTTP/1.1 200 OK<br/>Content-Type: application/json<br/>Cache-Control: no-store<br/>Request-Id: req_abc123<br/><br/>{"id": "ch_xyz", "status": "succeeded"}
```

The request line on top, headers below, blank line, then body. The response mirrors that shape. Every HTTP transaction looks like this — the only thing that changes is what's inside.

## Example — a real POST to Stripe

Here's an actual `POST` to Stripe's charge API. Walk through it line by line.

**The request:**

```http
POST /v1/charges HTTP/1.1
Host: api.stripe.com
Authorization: Bearer sk_test_EXAMPLE_KEY_REDACTED
Content-Type: application/json
Content-Length: 87
Idempotency-Key: a1b2c3d4-e5f6
User-Agent: Stripe/v1 NodeBindings/12.0.0

{"amount": 2000, "currency": "usd", "source": "tok_visa", "description": "Test charge"}
```

What each piece is doing:

- **`POST /v1/charges HTTP/1.1`** — verb, path, protocol version. We're creating a new charge.
- **`Host`** — which domain. One IP can serve many sites; this disambiguates.
- **`Authorization: Bearer ...`** — the API key. This is how Stripe knows it's you.
- **`Content-Type: application/json`** — the body is JSON. Server uses this to parse it.
- **`Content-Length: 87`** — bytes in the body. Lets the server know when to stop reading.
- **`Idempotency-Key`** — Stripe-specific. If the request retries, Stripe won't double-charge. POST is normally not idempotent — this header makes it safe.
- **`User-Agent`** — who's calling. Useful for analytics and debugging.

**The response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-cache, no-store
Request-Id: req_AbCdEf123
Stripe-Version: 2024-04-10

{"id": "ch_3OqAbc...", "amount": 2000, "currency": "usd", "status": "succeeded", "paid": true}
```

- **`200 OK`** — it worked. Charge created.
- **`Content-Type`** — JSON coming back.
- **`Cache-Control: no-store`** — never cache this. It's a financial event.
- **`Request-Id`** — Stripe's trace ID. Paste this into a support ticket and they can find your exact call.
- **Body** — the new resource. `id` is the handle you'll use for refunds, lookups, webhooks.

That whole exchange happens in 100–300ms. Multiply by billions of requests and you've got Stripe.

## Mechanics — verbs & status codes

GET asks. POST creates. PUT replaces. DELETE removes. That's 80% of the verb game.

**Verbs:**

| Verb | What it does | Idempotent? | Has body? |
|---|---|---|---|
| **GET** | Read a resource | Yes | No |
| **POST** | Create a new resource | No | Yes |
| **PUT** | Replace a resource entirely | Yes | Yes |
| **PATCH** | Update part of a resource | No (technically) | Yes |
| **DELETE** | Remove a resource | Yes | Optional |
| **HEAD** | Like GET but no body — just headers | Yes | No |
| **OPTIONS** | Ask "what can I do here?" — used in CORS preflight | Yes | No |

*Idempotent* means: call it once or call it ten times, the end state is the same. GET reading a user doesn't change anything. PUT setting a user's name to "Alice" lands at the same place no matter how many times you fire it. POST creating an order ten times creates ten orders.

**Status codes:**

| Range | Meaning | Most common |
|---|---|---|
| **1xx** | Informational | `100 Continue` (rare) |
| **2xx** | Success | `200 OK`, `201 Created`, `204 No Content` |
| **3xx** | Redirection | `301 Moved Permanently`, `302 Found`, `304 Not Modified` |
| **4xx** | Client error — *you* messed up | `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `429 Too Many Requests` |
| **5xx** | Server error — *they* messed up | `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`, `504 Gateway Timeout` |

The two pairs people mix up:

- **401 vs 403** — 401 means "I don't know who you are." 403 means "I know who you are, and no."
- **502 vs 504** — 502 means a downstream server returned garbage. 504 means it didn't return at all (timeout).

## Related concepts

| Concept | What it is | How it relates to HTTP |
|---|---|---|
| **REST** | An architectural style for APIs using HTTP verbs against resource URLs | The dominant pattern for HTTP APIs. `GET /users/42` is REST in one line. |
| **HTTPS / TLS** | HTTP over an encrypted TCP connection | Same protocol, encrypted in transit. Default for the entire modern web. |
| **CORS** | Cross-Origin Resource Sharing — browser rule for cross-domain requests | Lives entirely in HTTP headers (`Access-Control-Allow-Origin`). Preflight uses OPTIONS. |
| **Cookies** | Server-set key-value pairs the browser sends back on every request | Just headers — `Set-Cookie` from server, `Cookie` from client. |
| **Caching headers** | `Cache-Control`, `ETag`, `Last-Modified` — control what's reused | The reason a page loads instantly on second visit. |
| **Authorization headers** | `Authorization: Bearer <token>` or `Basic <base64>` | How most APIs authenticate. The token is the credential, the header is the envelope. |
| **URL structure** | `scheme://host:port/path?query#fragment` | The address every HTTP request points at. |
| **HTTP/2 & HTTP/3** | Newer versions with multiplexing, header compression, and QUIC | Same verbs, codes, and headers — different wire format underneath. |

## When (and when not) to use it

**Use HTTP when:**

- You're building a **web app, mobile API, or anything talking to a browser** — HTTP is the default
- You need **wide compatibility** — every language, framework, and proxy speaks it
- You want **caching, observability, and standard tooling** — HTTP gets you all of this for free
- The interaction is **request/response** in nature — ask, get an answer, done

**Skip it (or pair it with something else) when:**

- You need **server-pushed updates** — chat apps, live dashboards, multiplayer games. Use **WebSockets** or **Server-Sent Events**.
- You're doing **internal microservice calls** at high volume — **gRPC** is faster (binary, HTTP/2, schema-typed). HTTP/JSON works, but you'll feel the cost.
- You need **streaming both ways** with low latency — gRPC streams or WebSockets, not HTTP.
- You're moving **huge payloads between data centers** — specialized protocols (or chunked uploads to object storage) beat raw HTTP.

For 95% of what you'll build, HTTP is the answer. Reach for the alternatives when the request/response shape doesn't fit.

## Key takeaway

- **Verbs say what. Status codes say how it went. Headers carry everything else.**
- **Idempotency matters** — GET, PUT, DELETE are safe to retry. POST is not (use an idempotency key).
- **Read 4xx as "you," 5xx as "them."** It tells you which side to debug first.
- **DevTools is your friend.** Every problem you'll hit on the web is visible in the Network tab.

---

*Quiz available in the SLAM OG app — three questions on idempotency, status code meaning, and which header controls caching.*
