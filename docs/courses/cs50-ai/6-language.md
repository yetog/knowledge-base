---
tags:
  - ai
  - python
  - course
  - learning
---

# Week 6: Language

**CS50's Introduction to Artificial Intelligence with Python**

---

## Natural Language Processing

NLP encompasses tasks where AI receives human language as input.

| Application | Description |
|---|---|
| Automatic summarization | Converting text into concise summaries |
| Information extraction | Pulling structured data from text corpora |
| Language identification | Determining which language text is written in |
| Machine translation | Converting text between languages |
| Named entity recognition | Identifying proper nouns like company names |
| Speech recognition | Transcribing spoken words to text |
| Text classification | Categorizing text by type or sentiment |
| Word sense disambiguation | Resolving words with multiple meanings |

---

## Syntax and Semantics

**Syntax:** Sentence structure and grammatical rules. Sentences can be syntactically correct yet ambiguous — "I saw the man with the telescope" could mean viewing someone who possesses a telescope, or viewing using one.

**Semantics:** Meaning. Different sentences can convey identical meaning despite structural differences. Perfectly grammatical sentences can be meaningless (e.g., Chomsky's "Colorless green ideas sleep furiously").

---

## Context-Free Grammar

**Formal Grammar:** Systematic rules for generating sentences.

**Context-Free Grammar (CFG):** Abstracts sentences into structural representations.

### Example: "She saw the city"

| Word | Part of Speech |
|---|---|
| She | N (Noun) |
| saw | V (Verb) |
| the | D (Determiner) |
| city | N (Noun) |

- "the city" → Noun Phrase (NP)
- "saw the city" → Verb Phrase (VP)
- Full sentence S = NP + VP

### NLTK Implementation

```python
import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP

    NP -> D N | N
    VP -> V | V NP

    D -> "the" | "a"
    N -> "she" | "city" | "car"
    V -> "saw" | "walked"
""")

parser = nltk.ChartParser(grammar)

sentence = input("Sentence: ").split()
try:
    for tree in parser.parse(sentence):
        tree.pretty_print()
        tree.draw()
except ValueError:
    print("No parse tree possible.")
```

---

## N-grams

An **n-gram** is a sequence of *n* items from text.

| Term | Description |
|---|---|
| Unigram | Single item |
| Bigram | Two consecutive items |
| Trigram | Three consecutive items |

**Character n-grams** use characters; **word n-grams** use words.

N-grams enable prediction — smartphones suggest next words based on probability distributions from preceding sequences.

---

## Tokenization

Splits character sequences into tokens (words or sentences).

**Challenges:**
- Separating punctuation from words
- Handling apostrophes in contractions ("o'clock")
- Managing hyphens in compound words
- Distinguishing sentence-ending periods from abbreviation periods ("Mr.")

Proper tokenization is essential before analyzing n-grams or any text features.

---

## Markov Models for Text

Generate text by establishing probability distributions for tokens based on preceding ones. After training, a trigram-based model chooses the third word from distributions shaped by the first two words, then selects the fourth word using words two and three.

Produces grammatical-sounding sentences that lack actual semantic meaning or purpose.

---

## Bag-of-Words Model

Represents text as **unordered word collections**, ignoring syntax and focusing on meaning. Effective for classification tasks like sentiment analysis.

**Examples:**
- "My grandson loved it! So much fun!" → positive: "loved," "fun"
- "Product broke after a few days." → negative: "broke"
- "Kind of cheap and flimsy, not worth it." → negative: "cheap," "flimsy"

---

## Naive Bayes

Computes **P(sentiment | text)** — probability that text expresses a particular sentiment.

Using Bayes' rule:
```
P(sentiment | words) ∝ P(words | sentiment) × P(sentiment)
```

Calculates:
```
P(positive) × P("word₁" | positive) × P("word₂" | positive) × ...
```

The "naive" assumption treats each word's probability as **independent** from others — unrealistic but effective.

### Addressing Zero Probabilities

If a word never appears in positive training samples, its conditional probability becomes 0, incorrectly eliminating entire sentences.

**Additive Smoothing:** Adds value α to each distribution entry.

**Laplace Smoothing:** Adds 1 to each value — assumes all values appeared at least once.

---

## Word Representation

### One-Hot Representation

Each word gets a vector of vocabulary length with a single 1.

Example for "He wrote a book":
```
He:    [1, 0, 0, 0]
wrote: [0, 1, 0, 0]
a:     [0, 0, 1, 0]
book:  [0, 0, 0, 1]
```

**Problems:**
- 50,000-word vocabulary → 50,000-dimensional vectors
- Fails to capture similarity between synonyms ("wrote" and "authored")

### Distributed Representation

Compresses meaning across fewer dimensions:
```
He:    [-0.34, -0.08, 0.02, -0.18, …]
wrote: [-0.27,  0.40, 0.00, -0.65, …]
book:  [-0.23, -0.16, -0.05, -0.57, …]
```

- Smaller vectors
- Synonyms have similar values — captures semantic similarity

### Word Context Principle

J.R. Firth: *"You shall know a word by the company it keeps."*

Words appearing in similar contexts share meaning. Words completing "for ___ he ate" likely include breakfast, lunch, or dinner.

---

## word2vec

Generates distributed word representations using **Skip-Gram Architecture** — a neural network predicting context from target words.

**Architecture:**
- **Input layer:** One unit per target word
- **Hidden layer:** 50–100 units generating distributed representations
- **Output layer:** Predicts contextually similar words

**Results — book's nearest neighbors:** books, essay, memoir, essays, novella, anthology, blurb, autobiography, audiobook

### Vector Arithmetic

Word vectors enable semantic operations:
```
king − man ≈ queen − woman
(ramen − japan) + america ≈ burritos
```

---

## Neural Networks for Language

Translate sequences to sequences — essential for chatbots, Q&A, and translation.

### Recurrent Neural Networks

Process sequences by maintaining **hidden states**:

1. Input enters network → creates initial hidden state
2. Next input combines with previous hidden state → new hidden state
3. Repeat until end token
4. Decoding phase generates output sequences

**Problems:**
- All input information compresses into a single final state — inefficient for long sequences
- Not all hidden states carry equal importance

---

## Attention

Allows networks to **prioritize important values**. When answering "What is the capital of Massachusetts?", attention highlights "capital" and "Massachusetts" as most relevant.

**Process:**
1. Calculate attention scores
2. Multiply scores by hidden state values
3. Sum into a **context vector**
4. Decoder uses context vector for output generation

Sequential processing in RNNs bottlenecks performance with large datasets — motivating transformers.

---

## Transformers

Process **all input words simultaneously** rather than sequentially.

### Encoding

1. Words enter network simultaneously
2. **Position encoding** adds positional information, preserving word order
3. **Self-attention** steps determine each word's context
4. Multiple self-attention iterations refine understanding
5. Output: encoded representations ready for decoding

### Decoding

1. Previous output word + position encoding enter network
2. Multiple self-attention steps process information
3. Attention steps receive encoded representations
4. Words attend to each other across sequences
5. Parallel processing enables speed and accuracy

The transformer architecture powers modern large language models and most state-of-the-art NLP systems.
