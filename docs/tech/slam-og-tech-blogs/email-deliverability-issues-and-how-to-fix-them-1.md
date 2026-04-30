---
tags:
  - tech
  - blog
  - wte
---

# Email Deliverability Issues and How to Fix Them

**Source:** https://www.wte.net/Email-Deliverability-Issues-and-How-to-Fix-Them-1  
**Date:** January 2022  
**Author:** Erica in Client Services

---

## Introduction

The article opens by addressing a common problem: legitimate emails ending up in spam folders while sent business emails fail to reach inboxes. The root cause is identified as spammers overwhelming email providers, forcing them to implement protective measures. The solution proposed centers on email authentication standards.

## What is Email Authentication?

Email authentication serves as proof to internet service providers that an email genuinely originates from its claimed sender. As explained, "Spammers are notoriously good at spoofing email accounts and making them look legitimate." Authentication helps block phishing and spam while improving deliverability for legitimate senders.

## Three Main Email Authentication Standards

### DKIM (Domain Keys Identified Mail)

DKIM protects against malicious message modification through a public and private key system. The article describes it as "the simplest method of protection" using a relatively basic three-step process suitable for many businesses.

### SPF (Sender Policy Framework)

SPF records specify which IP addresses can send email on behalf of a domain. During an SPF check, mailbox providers verify the sending IP against DNS records. Matching addresses result in authentication success; mismatches may cause blocking or spam folder placement.

### DMARC (Domain-based Message Authentication, Reporting & Conformance)

DMARC represents the latest advancement, unifying SPF and DKIM into a common framework. Messages must pass both SPF and DKIM authentication with proper alignment. Organizations can implement three policy types:

- **p=none:** No action taken on failed authentication
- **p=quarantine:** Failed messages directed to spam/junk folders
- **p=reject:** Failed messages blocked entirely

## Implementation Guidance

DNS record access is required for implementation. WTE Solutions offers assistance through AgileMail Pro, SocketLabs integration, and SendGrid services for transactional and marketing email management.
