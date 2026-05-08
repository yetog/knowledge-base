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

## Patterns tier

Cloud-services-specific patterns — what's unique to running things on AWS / Azure / GCP.

- [Serverless & FaaS](serverless.md) — *Stop running servers. Bring code, leave operations.*
- [Edge Computing](edge-computing.md) — *Push the code closer to the user, not just the content.*
- [Managed Database Services](managed-databases.md) — *Trade money for time. At most company sizes that's the right trade.*
- [AI/ML Cloud Services](cloud-ai-services.md) — *Stop training. Start calling. The API is the new architecture primitive.*

---

## Real systems tier

Strategy and operating reality — the topics that decide whether the cloud saves you money or eats you alive.

- [Cloud Cost Management & FinOps](cloud-cost-management.md) — *The surprise bill is a feature, not a bug.*
- [Multi-cloud & Hybrid Strategies](multi-cloud-hybrid.md) — *Multi-cloud is what you say in board meetings. Single-cloud is what you ship in production.*
- [Cloud Migration Patterns (the 6 R's)](cloud-migration.md) — *Lift-and-shift is one of six options — pick the wrong R and you'll waste years.*

**All 12 topics complete.** 🎉

---

## How this is built

Source PDFs (Zen of Cloud, etc.) are extracted to a private `study/` folder (gitignored), read for context, then rewritten in SLAM OG voice with new diagrams. Original phrasing is never republished. See [STUDY.md](https://github.com/yetog/knowledge-base/blob/main/STUDY.md) for the workflow.

Cross-references back to the [System Design course](../system-design/index.md) handle topics covered there: containers, Kubernetes, microservices, cloud-native architecture, CI/CD.
