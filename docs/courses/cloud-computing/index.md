---
tags:
  - cloud-computing
  - course
---

# Cloud Computing — SLAM OG

> Building on the cloud, the way the cloud is actually built.

This course is the cloud-services-specific companion to the [System Design course](../system-design/index.md). System Design covers *how to architect software*. Cloud Computing covers *how to use AWS / Azure / GCP* — services, providers, IAM, networking, cost, security model.

If a topic is "*how do I architect software?*" → look in System Design. If it's "*how do I use this cloud platform?*" → here.

Each topic delivers:

- A 1-line hook — *why this matters*
- The core concept in 8–12 minutes
- A diagram (Mermaid) you can sketch on a napkin
- A real-world example (concrete services, real prices, real failure modes)
- A "test yourself" quiz embedded in the page metadata

The same content powers the **SLAM OG app** — same source, two consumers.

---

## Foundation tier

The five things every cloud engineer should know cold before specializing.

- [Cloud Computing 101](cloud-computing-101.md) — *Cloud isn't a place. It's a ladder of abstractions — pick the right rung.*
- [Cloud Networking — VPC, Subnets, Security Groups](cloud-networking.md) — *Your cloud workload lives in a VPC. Understanding that is non-negotiable.*
- [Identity & Access Management (IAM)](cloud-iam.md) — *Most cloud breaches aren't zero-days. They're a wide-open IAM policy.*
- [Cloud Storage Services (Block, File, Object)](cloud-storage-services.md) — *Three storage families, three jobs — pick by access pattern, not by default.*
- [Cloud Security & The Shared Responsibility Model](cloud-security-shared-responsibility.md) — *AWS protects the cloud. You protect what's in it.*

---

## Patterns tier *(coming next)*

Serverless & FaaS · Edge Computing · Managed Database Services · AI/ML Cloud Services

---

## Real systems tier *(coming next)*

Cost Management & FinOps · Multi-cloud & Hybrid Strategies · Cloud Migration Patterns

---

## How this is built

Source PDFs (Zen of Cloud, etc.) are extracted to a private `study/` folder (gitignored), read for context, then rewritten in SLAM OG voice with new diagrams. Original phrasing is never republished. See [STUDY.md](https://github.com/yetog/knowledge-base/blob/main/STUDY.md) for the workflow.

Cross-references back to the [System Design course](../system-design/index.md) handle topics covered there: containers, Kubernetes, microservices, cloud-native architecture, CI/CD.
