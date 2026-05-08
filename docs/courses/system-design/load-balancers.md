---
slug: load-balancers
title: Load Balancers
tagline: "Traffic cop for your servers. No load balancer, no scale."
tier: foundation
difficulty: beginner
estimated_minutes: 8
prerequisites: [networking-basics, http-fundamentals]
related: [cdn, reverse-proxy, api-gateway, health-checks]
tags:
  - system-design
  - course
  - infrastructure
  - networking
quiz:
  - q: "Main difference between L4 and L7 load balancing?"
    options:
      - "L4 is faster, L7 is smarter"
      - "L7 routes by URL/headers, L4 by IP/port"
      - "They're the same thing, marketed differently"
      - "L4 only handles HTTPS, L7 handles HTTP"
    answer: 1
    explain: "L4 routes at the transport layer — IP and port. Fast but blind to content. L7 routes at the application layer — URL, headers, cookies. Slower per request, smarter overall. The first answer captures the vibe but not the technical distinction."
  - q: "Your app crashes under traffic spikes. Why doesn't round-robin DNS solve it?"
    options:
      - "DNS is too slow"
      - "DNS doesn't know if a server is healthy"
      - "DNS only supports four A records"
      - "It actually does solve it"
    answer: 1
    explain: "Round-robin DNS will happily send users to a dead server. A load balancer health-checks each backend and routes around the broken ones. That's the whole point."
  - q: "When would you NOT need a load balancer?"
    options:
      - "Single server, low traffic"
      - "Anytime you have under 1,000 users"
      - "Never — every app needs one"
      - "Only when you're not using HTTPS"
    answer: 0
    explain: "If you've got one box and traffic is low, a load balancer is overhead with no benefit. The moment you scale to two backends, you need one."
---

# Load Balancers

> Traffic cop for your servers. No load balancer, no scale.

## The hook

You launched. Your app got linked on Hacker News. 50,000 people hit it in the next hour. Your one server taps out.

You can't just spin up more servers — *how* do users get routed to them? Round-robin DNS is broken (no health checks). Telling users "click this URL on Tuesdays, that one on Thursdays" obviously doesn't work.

You need a load balancer. It's the box that sits in front of your servers and decides who gets which one.

## The concept

A load balancer accepts incoming traffic, picks a backend server, and forwards the request. The user never knows which server actually answered.

Three jobs:

1. **Distribution** — spread traffic across servers so none gets crushed
2. **Health checking** — stop sending traffic to dead servers
3. **Abstraction** — your servers can change (add, remove, upgrade) without users noticing

Two flavors based on what they inspect:

| Type | Layer | Routes by | Speed | Use when |
|---|---|---|---|---|
| **L4** | Transport (TCP/UDP) | IP, port | Fast — doesn't open the packet | Raw throughput beats smart routing |
| **L7** | Application (HTTP) | URL, headers, cookies | Slower — parses the request | You need `/api` to one fleet and `/admin` to another |

For most web apps, **L7**. The flexibility is worth the small latency cost.

## Diagram

```mermaid
flowchart LR
    U1[User] --> LB[Load Balancer]
    U2[User] --> LB
    U3[User] --> LB
    LB -.health check.-> S1
    LB -.health check.-> S2
    LB -.health check.-> S3
    LB --> S1[Server 1]
    LB --> S2[Server 2]
    LB --> S3[Server 3 ❌]
    style S3 stroke:#f66,stroke-dasharray:5
```

The dashed lines are health checks. The crossed-out server is unhealthy — the LB stops routing to it until checks pass again.

## Example

**Netflix** uses L7 load balancers (their own + AWS ALB) to route by URL path:

- `/api/movies` → catalog service
- `/api/watch` → streaming service
- `/api/recommendations` → ML service

Each path hits a different fleet. One load balancer, many backend services. Users see one domain.

This pattern — one front door, many backends — is the foundation of microservices. The load balancer is what makes it work.

## Algorithms (how it picks a server)

| Algorithm | What it does | When to use |
|---|---|---|
| **Round-robin** | Server 1, 2, 3, 1, 2, 3... | Backends are roughly equal |
| **Least connections** | Server with fewest active requests | Long-lived connections (WebSockets, streaming) |
| **IP hash** | Same client → same server | Sticky sessions (avoid if you can) |
| **Weighted** | Some servers get more traffic | Mixed hardware (the big box gets 2x) |

Default to round-robin or least connections. Don't reach for IP hash unless you can't store session state in a shared cache (Redis) — and if you can't, fix that first.

## Key takeaway

- **One server → no LB.** Two servers → you need one.
- **L7 by default** for web apps. L4 only when raw speed beats routing logic.
- **Health checks are non-negotiable** — automatic failover is the entire point.
- **The LB itself is a single point of failure.** Production runs two LBs in active-passive or active-active.

---

*Quiz available in the SLAM OG app — three questions on L4 vs L7, why round-robin DNS isn't enough, and when you don't need a load balancer.*
