---
tags:
  - tech
  - blog
  - wte
---

# Air Gap Backups - A Comprehensive Guide

**Source:** https://www.wte.net/Blog/March-2023/Air-Gap-Backups-A-Comprehensive-Guide  
**Date:** March 2023  
**Author:** Eric Garrison

---

## Introduction

After a friend's website experienced a breach, air gap backups created preventatively proved instrumental in recovery. This guide explores how intelligent attackers target critical data and infrastructure, and why modern backup strategies must evolve beyond traditional approaches.

The author reflects on WTE's founding twenty years ago, when tape backups and offline storage were standard practice. Today's threat landscape—particularly ransomware capable of infiltrating cloud backup systems—has renewed the relevance of air-gapped solutions.

## What is Cybersecurity?

Cybersecurity protects computer systems, networks, and digital information from "unauthorized access, theft, or damage." It encompasses multiple dimensions:

- **Data** - Protecting digital information
- **Network** - Securing computer networks from attacks
- **Applications** - Safeguarding software from vulnerabilities
- **Endpoints** - Protecting individual devices
- **Cloud** - Securing cloud-based resources
- **Identity & Access Management** - Controlling authorized access
- **Incident Response** - Developing recovery solutions

The field continuously evolves as cybercriminals develop sophisticated attacks, while human error remains a persistent vulnerability factor.

## Common Backup Strategies

Several approaches protect against data loss:

- **Full Backup** - Complete copy of all data; comprehensive but resource-intensive
- **Incremental Backup** - Captures only changed data since last backup; efficient but potentially slower recovery
- **Differential Backup** - Backs up changes since last full backup; more storage than incremental
- **Mirror Backup** - Exact system copy; simple restoration
- **Cloud Backup** - Remote storage via providers like AWS
- **Hybrid Backup** - Combines multiple methods

Selection depends on data volume, backup frequency, and recovery speed requirements.

## What is Role Based Access Control?

Role-based access control restricts resources according to organizational role. Benefits include:

- **Improved Security** - Prevents unauthorized access
- **Increased Efficiency** - Users access only necessary resources
- **Simplified Administration** - Manage access by role rather than individual

RBAC provides "a flexible and scalable approach to access control that can be adapted to meet the organization's changing needs."

## What Are Air Gap Backups?

Air gap backups achieve physical isolation from internet and other networks, creating an "air gap" preventing online attacks. While not new, the approach has regained importance due to ransomware threats.

Ransomware encrypts files, making them inaccessible while attackers demand decryption payment. Air gap security prevents malware from reaching backups through network channels. However, physical vulnerabilities exist—infected USB devices introduced via social engineering can compromise isolated systems.

Despite higher costs, the investment protects sensitive customer and operational data. "What's your data worth?" when potential breaches could trigger multi-million dollar lawsuits.

## Types of Air Gap Backups

- **Hard Air Gap** - Strictest isolation with zero network connectivity
- **Soft Air Gap** - Limited communication through controlled channels
- **Data Diode** - One-directional data flow
- **Virtual/Logical Air Gap** - Software-based separation despite physical connectivity

### More About Virtual & Logical Air Gaps

When physical isolation proves impossible, logical air gaps provide alternative protection. These use encryption and access controls while maintaining system connections. Financial institutions and hospitals employ this approach to protect sensitive systems and data.

## What is Ransomware?

Ransomware is malware that "encrypts files on a computer or network, making those encrypted files inaccessible to their owners and creators." Attackers demand cryptocurrency payment for decryption keys.

Two primary types exist:

- **Encrypting Ransomware** - Encrypts victim files
- **Locker Ransomware** - Locks users out entirely

Attacks often include threats to publish stolen data or delete encrypted files. The consequences extend beyond financial—legal and regulatory penalties may apply if organizations fail protective obligations.

## What is Disaster Recovery?

Comprehensive disaster recovery planning involves:

- **Risk Assessment** - Identify threats and impacts
- **Continuity Planning** - Develop operational procedures
- **Recovery** - Implement daily full air gap backups and hourly cloud-to-cloud backups for critical systems
- **Recovery Testing** - Quarterly testing validates procedures before crisis
- **Incident Response** - Dashboard monitoring and alerts enable rapid response
- **Training** - Employee education on security and disaster response

"Rapid recovery from natural or manufactured disasters helps minimize the impact on a business."

## Summary & WTE's Air Gaps

### Summary

Cybersecurity importance will increase as attack frequency and severity rise. "Backups aren't enough these days" when sophisticated attackers can tunnel into standard backup systems. Air gap solutions provide necessary additional protection.

### How WTE Does Air Gap Backups

The firm creates air gap backups using external Network Attached Storage devices located in segregated facilities outside their Raleigh, North Carolina datacenters. These alternate locations feature isolated connections, separate internet access, dedicated admin accounts, encryption, and redundant security layers. Frequent cloud backups complement less frequent but more secure full backups, creating a balanced disaster recovery framework.
