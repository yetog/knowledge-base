---
tags:
  - tech
  - blog
  - wte
---

# The DMARC & DKIM Revolution You Can't Afford to Miss

**Source:** https://www.wte.net/Blog/August-2023/The-DMARC-DKIM-Revolution-You-Can-t-Afford-to-Miss  
**Date:** August 2023  
**Author:** Eric Garrison

---

## Introduction

The article examines how DMARC and DKIM protect against the 300 billion daily emails, addressing phishing threats through "a digital signature, a seal of authenticity."

## What is Phishing?

The post describes phishing as "the art of digital deception" and outlines five common tactics:

- Urgent CEO emails requesting wire transfers
- IRS-themed messages requesting financial information
- Prize notifications requiring payment or personal data
- Fake verification emails mimicking legitimate services
- Messages from compromised accounts belonging to trusted contacts

## Types of Phishing Attacks

**Spear Phishing:** Precision-targeted attacks using personal details about victims, with higher success rates than generic phishing due to customization.

**Vishing:** Voice-based deception via phone calls, employing urgent narratives to extract sensitive information.

**Smishing:** SMS text message scams using brevity and urgency to manipulate recipients into clicking links or revealing data.

## What is DMARC?

DMARC (Domain-based Message Authentication, Reporting & Conformance) serves as Microsoft's solution to email spoofing, acting as a "discerning gatekeeper" that determines which emails reach inboxes and provides transparency about authentication attempts.

## What is DKIM?

DKIM (DomainKeys Identified Mail) functions as a cryptographic signature — comparable to "sending a letter with a wax seal" — verifying email authenticity and origins.

## How DMARC and DKIM Work Together

The article uses theatrical metaphors: DKIM provides authentication signatures while DMARC directs policy responses (rejection, quarantine, or monitoring) for failed authenticity checks, creating integrated email security.

## Microsoft 365 Implementation

Organizations can:

- Control handling of failing DMARC emails
- Set custom actions based on policy settings
- Protect against brand spoofing
- Maintain email delivery while enforcing authentication
- Update authentication workflows with partners

**Seven recommendations include:**

1. Understanding basics
2. Using Microsoft setup wizards
3. Enabling DKIM for custom domains
4. Carefully crafting DMARC policies
5. Monitoring reports
6. Educating teams
7. Seeking community support
