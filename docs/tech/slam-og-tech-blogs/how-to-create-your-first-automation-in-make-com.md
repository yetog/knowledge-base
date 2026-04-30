---
tags:
  - tech
  - blog
  - wte
---

# How to Create Your First Automation in Make.com

**Source:** https://www.wte.net/Blog/July/How-to-Create-Your-First-Automation-in-Make-com  
**Date:** July 2025  
**Author:** Izaic Yorks

---

*A Beginner's Guide with Pro Tips*

## Introduction

The article opens by explaining that automation through Make.com (formerly Integromat) can streamline workflows for IT professionals and business owners. The author emphasizes this is a "no-code platform that connects apps like email and Google Sheets" without requiring advanced coding skills.

The tutorial focuses on capturing email details and logging them into a Google Sheet as the foundational project, using a Mail Hook and Google Sheets module.

## Why This Automation?

Three key reasons are provided:

- Straightforward setup with minimal complexity
- Teaches fundamental app-connection principles in Make.com
- Practical applications including tracking emails, managing leads, and logging inquiries

**Note:** Some features may require a paid account; the core setup works on the free plan.

## What You'll Need

Prerequisites:

- Make.com account (free tier acceptable)
- Google account with Drive and Sheets access
- Email client (Gmail or Outlook)
- Basic email and spreadsheet familiarity

## Step-by-Step Instructions

### Step 1: Create a New Scenario

Log into Make.com and click "Create new scenario" to open the visual workspace. The author notes: "Think of a scenario as a flowchart. Each 'module' (an app or action) links to the next."

### Step 2: Set Up a Mail Hook

- Search for "Mail Hook" in the scenario builder
- Configure to generate a unique email address
- Save the address for testing

The author explains Mail Hook functions as an "instant trigger," activating automation immediately upon email receipt.

### Step 3: Create a Google Sheet

- Open Google Drive and create new sheet
- Add headers: From, Date, Subject, Body
- Author notes longer fields like Body work better positioned last for readability

### Step 4: Add a Google Sheets Module

- Click "+" icon to add new module
- Select "Google Sheets" and "Add a Row" option
- Authorize Google account via OAuth

### Step 5: Configure the Google Sheets Module

- Select spreadsheet and Sheet1
- Map Mail Hook data to columns:
  - From: sender's email
  - Date: timestamp
  - Subject: email subject
  - Body: email content

**Expert Tip:** "Mapping is where the magic happens. If a field doesn't show up, expand the Mail Hook's output options."

### Step 6: Test Your Automation

- Save the scenario
- Send test email to Mail Hook address
- Verify data appears in Google Sheet
- Author notes processing may take several seconds

## Troubleshooting Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Email not triggering | Wrong Mail Hook address | Verify exact address from Make.com |
| Sheet not updating | Wrong spreadsheet/sheet selected | Check spreadsheet name/ID and sheet name |
| No data in columns | Field mapping error | Recheck Google Sheets module field links |
| OAuth errors | Expired/denied permissions | Reauthorize Make.com in Google settings |

## Advanced Features

### 1. Handling Attachments

- Add Iterator module after Mail Hook
- Filter unwanted file types (e.g., GIFs from signatures)
- Save attachments to Google Drive or process further

### 2. AI Integration with ChatGPT

Two-step process:

1. Upload files to ChatGPT API (requires API key)
2. Pass file ID with analysis prompt; return results as JSON

The author notes this two-step approach prevents common errors and enables sophisticated document analysis.

### 3. Optimize with AI (Advanced Strategy)

- Export scenario as JSON blueprint
- Use Claude (version 4.0+) to optimize the blueprint
- Claude can improve basic logic like date calculations and conditionals
- Import updated blueprint back into Make.com
- Author advises keeping backup blueprints for version control

**Limitation noted:** Claude struggles with regex and highly complex formulas but excels at workflow optimization.

## Conclusion

The author summarizes this email-to-Google-Sheet automation as an ideal starting point, encouraging experimentation and iteration. Additional resources referenced include Make.com documentation, community forums, YouTube tutorials, and Google Sheets help.

The piece closes with an invitation for reader questions and collaboration opportunities.
