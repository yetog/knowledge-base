---
tags:
  - tech
  - blog
  - wte
---

# AI Your Guide To What's Coming

**Source:** https://www.wte.net/AI-Your-Guide-To-What-is-Coming  
**Date:** January 2023  
**Author:** Eric Garrison

---

## Overview

This comprehensive guide explores the rapid advancement of artificial intelligence, particularly following ChatGPT's viral adoption. Garrison discusses how AI is reshaping technology services and introduces two emerging business models: AI-as-a-Service (AIaaS) and AI-as-a-Platform (AIaaP).

## What is AI?

Garrison contrasts various perspectives on artificial intelligence, from Alan Turing's philosophical approach to modern definitions. He references IBM's practical definition:

> "Artificial intelligence combines computer science and robust datasets to enable problem-solving, encompassing machine learning and deep learning."

ChatGPT's definition emphasizes AI's capacity for tasks requiring human intelligence—language understanding, image recognition, decision-making, and problem-solving.

## What is ChatGPT?

ChatGPT, or Generative Pre-training Transformer, functions as a language model predicting word sequences based on probability. The GPT-3 version contains billions of parameters, enabling sophisticated responses across varied tasks without task-specific training.

Garrison notes ChatGPT-3's November 30 release marked a turning point; the chatbot achieved conversational quality nearly indistinguishable from human interaction, despite occasional downtime.

## AI-as-a-Service (AIaaS)

Rather than embedding ChatGPT directly (due to availability issues), WTE Solutions develops tailored end-use applications. The approach mirrors their previous work with Twilio SMS and Amazon Polly voice services.

### Key Implementation Strategy

- Build microservice architecture for modularity and scalability
- Deploy on Microsoft .Net Core with Kubernetes frameworks
- Integrate APIs to connect these "Lego-like" components
- Leverage existing experience with Azure Predictive Search (deployed over four years)

### The "Ask Eric" Project

WTE is developing an AIaaS application using the Pareto Principle—identifying that approximately 20% of answers address 80% of typical questions. This optimization reduces computing demands for simultaneous users and enables dashboard-based tuning for subscribers.

## AI-as-a-Platform (AIaaP)

While OpenAI develops research tools, organizations like WTE create end-use applications on these platforms. The analogy: OpenAI provides elementary education; companies specialize it through college-level training.

Implementation requires:

- Preparing training data through use cases and conversations
- Understanding JSON and command-line interfaces
- Navigating complex documentation

## Secret Sauce: Prompt Management

WTE employs "Prompt Toolkit" strategies—structured input management ensuring AI receives properly formatted data. Similar to Alexa recognizing specific command syntax, effective prompt management guides users through interactions with clarity and efficiency.

## Conclusion

Garrison emphasizes WTE's 25-year expertise in solving complex technical and marketing challenges, positioning the company to demystify AI's benefits for businesses seeking implementation strategies beyond theoretical applications.
