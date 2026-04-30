---
tags:
  - ai
  - python
  - course
  - learning
---

# Quiz 6: Language

**CS50's Introduction to Artificial Intelligence with Python**

---

## Question 1

**Which sentences can be derived from the given context-free grammar?**

1. Cats run.
2. Cats climb trees.
3. Small cats run.
4. Small white cats climb.

**Answer: Sentences 1, 3, and 4** ✓

> **Why:** CFG rules define what structures are grammatically valid. Sentence 2 ("Cats climb trees") requires a VP → V NP rule. If the grammar only allows VP → V (intransitive), then sentence 2 can't be derived. Sentences 1, 3, and 4 fit the rules as written.

---

## Question 2

**Which of the following is *not* a true statement?**

- Attention mechanisms can identify important input sequence parts to focus on
- **One-hot representations better represent word meaning than distributed representations** ✓ (this is FALSE)
- Transformers train faster than RNNs due to parallelization
- Naive Bayes assumes word order doesn't matter for classification

> **Why:** One-hot representations are actually *worse* at capturing meaning — they treat every word as equally dissimilar (orthogonal vectors). Distributed (dense) representations like word2vec capture semantic similarity, so synonyms have close vectors.

---

## Question 3

**Why is "smoothing" useful when applying Naive Bayes?**

- **Handles cases where evidence never appeared for a particular category** ✓
- Manages many classification categories instead of just two
- Makes classifier less naive by not assuming conditional independence
- Converts conditional probability of evidence given category to probability of category given evidence

> **Why:** If a word never appeared in positive training examples, P(word | positive) = 0, which zeros out the entire product regardless of all other evidence. Smoothing (e.g., Laplace smoothing) prevents any probability from being exactly zero.

---

## Question 4

**From the phrase "must be the truth", how many word n-grams of length 2 can be extracted?**

**Answer: 3** ✓

> **Why:** Bigrams are consecutive two-word pairs: "must be", "be the", "the truth" — **3 bigrams**. For a sequence of N words, you can extract N−1 bigrams.
