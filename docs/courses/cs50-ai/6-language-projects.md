---
tags:
  - ai
  - python
  - course
  - learning
---

# Projects 6: Language

**CS50's Introduction to Artificial Intelligence with Python**

---

## Project 1 — Parser

**Write a context-free grammar to parse English sentences and extract noun phrase chunks.**

### Background

NLP relies on parsing to reveal sentence structure. Context-free grammar uses rewriting rules — starting from `S` (sentence), expanding through nonterminals until reaching terminal words.

Example rules:
```
S  -> N V
NP -> N | Det N | Det Adj N
VP -> V | V NP | V NP PP
```

### Getting Started

```bash
pip3 install -r requirements.txt  # installs nltk
```

**`parser.py`** contains:
- `TERMINALS` — already-defined rules for parts of speech (N, V, Adj, Adv, Conj, Det, P)
- `NONTERMINALS` — currently only `S -> N V`, needs expansion
- `preprocess()` — implement this
- `np_chunk()` — implement this

### Specification

**`preprocess(sentence)`**

Accepts a sentence string, returns a lowercased list of words:
- Use `nltk.word_tokenize()`
- Lowercase all words
- Exclude tokens with no alphabetic characters (e.g., `.`, `28`)

**`NONTERMINALS`**

Expand the grammar rules so that all sample sentences can be parsed:
- Each rule on a separate line using `->` and `|` syntax
- Must start with `S ->`
- Use `NP` to represent noun phrases
- Avoid over-generation (don't allow obviously wrong sentences)

**`np_chunk(tree)`**

Accepts an `nltk.tree` syntax tree, returns a list of noun phrase chunks:
- A "noun phrase chunk" is an `NP` subtree that contains **no nested NP**
- "the home" → chunk. "the armchair in the home" (contains nested NP) → not a chunk
- Return list of `nltk.tree` objects labeled `NP`

### Hints

- Use `tree.subtrees()` to iterate over subtrees
- Use `tree.label()` to check a subtree's label
- Multiple parse trees per sentence are expected — English is ambiguous
- Implement `np_chunk()` to return `[]` first while you test the grammar

```bash
python parser.py sentences/1.txt
check50 ai50/projects/2024/x/parser
style50 parser.py
```

---

## Project 2 — Attention

**Use BERT to predict masked words and analyze what attention heads have learned.**

### Background

BERT (Google, 2018) is a transformer trained to predict masked words from context. Base BERT uses 12 layers × 12 attention heads = **144 attention heads total**.

This project has two parts:
1. **Implement** masked word prediction + attention visualizations for all 144 heads
2. **Analyze** the diagrams to identify linguistic patterns

### Getting Started

```bash
pip3 install -r requirements.txt  # includes transformers, tensorflow
```

### Code Structure

`mask.py` program flow:
1. Prompts for text containing `[MASK]`
2. Tokenizes with `AutoTokenizer`
3. Uses `TFBertForMaskedLM` to predict top-K replacements
4. Calls `visualize_attentions` to generate diagrams

**Special tokens:**
- `[MASK]` — the word to predict
- `[CLS]` — start of sequence
- `[SEP]` — end of sequence

**Attention access:** `attentions[layer][beam][head]`

### Specification

Implement 3 functions:

**`get_mask_token_index(mask_token_id, inputs)`**

Returns the 0-indexed position of the mask token in `inputs`. Returns `None` if absent.

**`get_color_for_attention_score(attention_score)`**

Converts an attention score (0–1) to an RGB tuple for visualization:
- 0.0 → `(0, 0, 0)` (black)
- 1.0 → `(255, 255, 255)` (white)
- Intermediate → grayscale (all three channels equal, linear scale)

**`visualize_attentions(tokens, attentions)`**

Generates one diagram per attention head across all layers. Call `generate_diagram(layer, head, tokens, attention_weights)` for each, using **1-indexed** layer and head numbers.

### Analysis Component

Complete `analysis.md` — identify at least 2 attention heads with discernible patterns:
- Describe what each head appears to focus on
- Give ≥2 example sentences demonstrating the pattern
- Must differ from the two examples given in the spec (Layer 3 Head 10, Layer 4 Head 11)

**Example patterns to look for:** verb-object relationships, determiner-noun pairs, pronoun references, preposition attachments, reverse sequential attention

> **Note:** Many heads strongly attend to `[CLS]` or `[SEP]` when no other word demands attention — this is expected behavior, not a finding.

```bash
python mask.py
check50 ai50/projects/2024/x/attention
style50 mask.py
```
