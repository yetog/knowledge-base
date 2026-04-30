---
tags:
  - ai
  - prompts
  - chatgpt
  - llm
  - prompt-engineering
---

# Prompt Engineering

Prompt engineering is the practice of structuring inputs to large language models in ways that reliably produce better, more useful outputs. Learning these patterns makes you more effective than someone who prompts intuitively.

## How LLMs Work

Large language models generate output **token by token** (roughly word by word). The process:

1. The model receives your input (the prompt)
2. It predicts the most likely next token based on that input plus everything generated so far
3. That token is appended, and the process repeats
4. This continues until the model predicts a "stop" token or hits a length limit

Key implications:

- Models are trained on massive text datasets — they have broad knowledge but no live awareness
- **The same prompt can produce different outputs on different runs** — this variability is a feature, not a bug. Different runs can yield different styles, voices, and approaches
- How you structure your prompt shapes what the model treats as relevant context at each generation step

## Why Prompt Structure Matters

With the right structure, prompts unlock powerful capabilities that intuitive prompting misses. Think of a prompt as giving form to your ideas through the model — the clearer and more specific the form, the more useful the output.

Learning prompt patterns lets you:

- Get more consistent, high-quality results
- Control tone, format, and depth
- Chain prompts together for complex workflows
- Reduce back-and-forth iteration

---

## Core Prompt Patterns

### 1. Persona Pattern

Ask the model to adopt a specific identity or role. This unlocks specialized knowledge, tone, and perspective that a generic response won't have.

> "I want you to act as a senior software engineer with 10 years of experience reviewing my code. Be direct about weaknesses."

> "Act as Albert Einstein and explain quantum mechanics to a 10-year-old."

> "You are a seasoned hiring manager with 20 years of experience reviewing job applications."

**When to use it:** When you need expert-level framing, a specific voice, or domain-specific judgment.

---

### 2. Context + Constraint Pattern

Give the model context about who you are, what you already know, and constrain the output format. This prevents over-explanation and focuses the response.

> "I'm a junior developer learning Java. Explain interfaces to me using a real-world analogy. Keep it under 200 words."

**Key elements:**
- Who you are (background, skill level)
- What you need (the actual request)
- Output constraints (length, format, tone)

---

### 3. Step-by-Step Decomposition

Ask the model to break work into explicit steps. This forces the model to reason through the problem sequentially rather than jumping to a summary answer.

> "Walk me through how to set up a Spring Boot project step by step. Include what to install, the file structure, and a working Hello World endpoint."

**When to use it:** Tutorials, how-to guides, debugging walkthroughs, planning tasks.

---

### 4. Feynman Technique Prompts

Named after physicist Richard Feynman's learning method: if you can't explain it simply, you don't understand it. Use these prompts to extract clear, simple explanations from the model.

> "Explain [topic] as if I'm 10 years old."

> "Condense this concept and give me a header: [paste text]"

> "Use an analogy to explain [concept]."

**When to use it:** Learning new topics, simplifying dense material, building intuition before diving into detail.

---

### 5. Refine + Iterate

Generate a first pass, then give specific feedback and ask for targeted revisions. Treat the model like a collaborator, not a one-shot oracle.

> "That future section is too vague. Give me one specific example from my resume that connects to this job description."

**Best practice:** Be specific about what's wrong and what you want instead. Vague feedback ("make it better") gets vague results.

---

### 6. Output Format Control

Specify exactly how you want the response structured. The model defaults to flowing prose — if you need something else, ask for it explicitly.

> "Respond with a table. Columns: Term | Definition | Example."

> "Give me a bulleted list, no more than 5 points, each under 15 words."

> "Respond only with code. No explanations."

**Common format options:** tables, bullet lists, numbered steps, code blocks, JSON, headers and sections, one-sentence summaries.

---

## Career & Resume Prompt Chain

A powerful multi-step workflow for job searching. Run these prompts in sequence, using the output of each step as input to the next.

1. **Extract priorities** — Get the top 3 responsibilities from a job description
2. **Frame your story** — Structure a "tell me about yourself" answer using the Present-Past-Future framework
3. **Sharpen the future section** — Refine it with job-specific examples from your resume
4. **Rewrite resume bullets** — Use the formula: "accomplished X by measure Y that resulted in Z"
5. **Prep for interviews** — Generate 10 likely interview questions for the role

This chain transforms a job description into a tailored narrative and prep set in under an hour.

---

## Resources

- **Prompt Engineering for Beginners** — OpenAI (free)
- **Prompt Engineering with Bard** — Google AI (free)
- **Towards Data Science** — prompt engineering guides and deep dives
