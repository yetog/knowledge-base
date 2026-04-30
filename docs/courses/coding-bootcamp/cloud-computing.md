---
tags:
  - cloud
  - infrastructure
  - course
  - tech
---

# Cloud Computing

## What is Cloud Computing?

On-demand access to shared computing resources — servers, storage, networking, software — over the internet from a third-party provider. You pay for what you use instead of owning and maintaining physical hardware.

---

## Service Models

### IaaS — Infrastructure as a Service

Rent the basic building blocks: servers, storage, and networking. You manage the OS and everything above it.

**Examples:** AWS EC2, Microsoft Azure VMs, Google Compute Engine

**Best for:** Maximum control; teams that want to configure their own stack.

### PaaS — Platform as a Service

A managed runtime/platform to build and deploy applications. The provider handles the OS, runtime, and infrastructure.

**Examples:** Heroku, Google App Engine, AWS Elastic Beanstalk

**Best for:** Developers who want to focus on code, not infrastructure.

### SaaS — Software as a Service

Pre-built applications delivered over the internet. No installation or maintenance required.

**Examples:** Gmail, Salesforce, Microsoft Office 365, Slack

**Best for:** End users consuming software, not building it.

| Model | You manage          | Provider manages              |
|-------|---------------------|-------------------------------|
| IaaS  | OS, runtime, apps   | Hardware, networking, storage |
| PaaS  | App code, data      | OS, runtime, middleware       |
| SaaS  | Data, user access   | Everything else               |

---

## Benefits of Cloud Computing

| Benefit                | Description                                                       |
|------------------------|-------------------------------------------------------------------|
| Pay-as-you-go          | No large upfront capital expense — pay only for what you consume  |
| Scalability            | Scale resources up or down on demand                              |
| Accessibility          | Access resources from anywhere with internet                      |
| No maintenance burden  | Provider handles hardware, patching, and physical security        |
| Multi-tenancy          | Cost shared across many customers, lowering individual expense    |
| High availability      | Built-in redundancy — if one server fails, others take over       |

---

## Deployment Models

### Private Cloud

Infrastructure provisioned exclusively for a single organization. Can be hosted on-premises or by a third party. Provides maximum control and security.

**Best for:** Regulated industries (finance, healthcare), sensitive data.

### Public Cloud

Infrastructure shared across multiple customers and operated by a third-party provider. Open market access with low entry cost.

**Examples:** AWS, Google Cloud Platform (GCP), Microsoft Azure

**Best for:** General workloads, startups, teams needing fast provisioning.

### Hybrid Cloud

A mix of private and public cloud. Sensitive data stays on the private cloud; public-facing services or burst workloads run on the public cloud.

**Use case:** A hospital keeps patient records on a private cloud but hosts its patient portal on a public cloud.

### Community Cloud

Shared infrastructure for organizations with common needs (e.g., regulatory compliance, shared mission). Costs and governance are shared among the group.

**Example:** A group of hospitals sharing HIPAA-compliant infrastructure.

### Multicloud

Using multiple public cloud providers simultaneously to avoid vendor lock-in or leverage pricing differences.

**Example:** Compute on AWS, data analytics on GCP, collaboration tools on Azure.

### Polycloud

Selectively picking the best individual services from different providers rather than committing to one vendor's full stack.

---

## Virtualization

Virtualization splits one physical machine into multiple isolated virtual machines (VMs), each with its own OS and resource allocation.

### Hypervisors

A hypervisor is the software layer that creates and manages VMs.

| Type               | Description                             | Examples                           |
|--------------------|-----------------------------------------|------------------------------------|
| Type 1 (Bare-metal)| Runs directly on hardware — enterprise  | VMware ESXi, Microsoft Hyper-V     |
| Type 2 (Hosted)    | Runs on top of an existing OS — lighter | VirtualBox, VMware Workstation     |

### Benefits of Virtualization

- **Better resource utilization** — multiple VMs share one physical machine
- **Isolation** — each VM is sandboxed; a crash in one doesn't affect others
- **Easier disaster recovery** — VMs can be snapshotted and restored quickly
- **Flexibility** — spin up or tear down environments in minutes

### Key Terms

| Term           | Definition                                               |
|----------------|----------------------------------------------------------|
| VM             | Virtual machine — a software-based computer             |
| Guest OS       | The OS running inside a VM                              |
| Host OS        | The OS running on the physical machine                  |
| Hypervisor     | Software that creates and manages VMs                   |
| Provisioning   | Allocating and configuring resources for use            |
| Elasticity     | Automatically scaling resources in response to demand   |
| Scalability    | Ability to increase capacity to handle more load        |
| Multitenancy   | Multiple customers sharing the same physical resources  |

---

## Industry Snapshot (2024)

- **SaaS** accounts for approximately 54% of global cloud revenue
- **Private cloud** accounts for 46%+ of market revenue
- **Hybrid cloud** is growing at 20%+ annually
- In the EU, 45.2% of enterprises purchased cloud services in 2023
- **Agentic AI platforms** — cloud-hosted AI agents — are beginning to reshape developer and enterprise workflows
