---
tags:
  - ai
  - python
  - course
  - learning
---

# Week 1: Knowledge

**CS50's Introduction to Artificial Intelligence with Python**

---

## Knowledge-Based Agents

Agents that reason by operating on internal representations of knowledge. A Harry Potter example demonstrates this: three given statements allow deduction of whether it rained, even though rain is never directly mentioned.

A **sentence** is an assertion about the world in a knowledge representation language — the mechanism through which AI stores and uses knowledge for inference.

---

## Propositional Logic

Based on propositions — statements that are either true or false.

### Propositional Symbols

Typically letters (P, Q, R) representing propositions.

### Logical Connectives

| Connective | Symbol | Meaning |
|---|---|---|
| Not | ¬ | Inverts truth value |
| And | ∧ | True only when both components are true |
| Or | ∨ | True when at least one component is true |
| Implication | → | "If P then Q"; false antecedent makes it trivially true |
| Biconditional | ↔ | "If and only if" — implication in both directions |

**Inclusive Or** is true if any argument is true. **Exclusive Or** is true if exactly one argument is true.

**Implication note:** When the antecedent (P) is false, the implication is always true regardless of the consequent — this is called "trivially true."

---

## Model and Knowledge Base

**Model:** An assignment of a truth value to every proposition. For *n* propositions, there are **2ⁿ** possible models.

**Knowledge Base (KB):** A set of sentences known by a knowledge-based agent.

**Entailment:** α ⊨ β means in any world where α is true, β is also true. Entailment describes a relationship between propositions; it differs from implication (a logical connective).

---

## Inference

The process of deriving new sentences from old ones.

### Model Checking Algorithm

To determine if KB ⊨ α:
- Enumerate all possible models
- If α is true in every model where KB is true, then KB ⊨ α

```python
def check_all(knowledge, query, symbols, model):
    if not symbols:
        if knowledge.evaluate(model):
            return query.evaluate(model)
        return True
    else:
        remaining = symbols.copy()
        p = remaining.pop()
        model_true = model.copy()
        model_true[p] = True
        model_false = model.copy()
        model_false[p] = False
        return (check_all(knowledge, query, remaining, model_true) and
                check_all(knowledge, query, remaining, model_false))
```

---

## Knowledge Engineering

The process of figuring out how to represent propositions and logic in AI.

### Clue Game Example

The murder-mystery game represents knowledge like:
- (Mustard ∨ Plum ∨ Scarlet)
- (knife ∨ revolver ∨ wrench)
- (ballroom ∨ kitchen ∨ library)

Cards revealed eliminate possibilities through negations. Failed guesses are expressed as disjunctions of negated elements.

### Mastermind

Each position and color combination becomes an atomic proposition. Game rules and clues are encoded, allowing model checking to find solutions.

---

## Inference Rules

Generate new knowledge from existing knowledge without checking all models.

| Rule | Form |
|---|---|
| **Modus Ponens** | If P → Q and P, then Q |
| **And Elimination** | If (P ∧ Q), then P (or Q) |
| **Double Negation** | ¬(¬P) = P |
| **Implication Elimination** | P → Q = ¬P ∨ Q |
| **Biconditional Elimination** | P ↔ Q = (P → Q) ∧ (Q → P) |
| **De Morgan's (And)** | ¬(P ∧ Q) = ¬P ∨ ¬Q |
| **De Morgan's (Or)** | ¬(P ∨ Q) = ¬P ∧ ¬Q |

### Knowledge as Search

Inference modeled as search:
- **Initial state:** the knowledge base
- **Actions:** inference rules
- **Transition model:** resulting KB after applying rules
- **Goal test:** whether the target statement is in the KB
- **Path cost:** number of proof steps

---

## Resolution

If one of two atomic propositions in an Or proposition is false, the other must be true.

**Complementary Literals:** Two identical propositions where one is negated — P and ¬P.

- From (P ∨ Q) and ¬P → infer Q
- From (P ∨ Q) and (¬P ∨ R) → infer (Q ∨ R)

### Conjunctive Normal Form (CNF)

A **clause** is a disjunction of literals. **CNF** is a conjunction of clauses.

Example: `(A ∨ B ∨ C) ∧ (D ∨ ¬E) ∧ (F ∨ G)`

**Conversion steps to CNF:**
1. Eliminate biconditionals: (α ↔ β) → (α → β) ∧ (β → α)
2. Eliminate implications: (α → β) → ¬α ∨ β
3. Move negation inward using De Morgan's Laws

**Example:** Convert (P ∨ Q) → R

```
(P ∨ Q) → R
→ ¬(P ∨ Q) ∨ R          (implication elimination)
→ (¬P ∧ ¬Q) ∨ R         (De Morgan's Law)
→ (¬P ∨ R) ∧ (¬Q ∨ R)   (distributive law)
```

### Resolution Algorithm

To determine if KB ⊨ α:
1. Convert (KB ∧ ¬α) to CNF
2. Repeatedly apply resolution to generate new clauses
3. If the **empty clause** is produced → contradiction exists → KB ⊨ α
4. If no more clauses can be inferred → no entailment

**Factoring** removes duplicate literals. Resolving complementary literals produces the **empty clause ()**, which is always false.

---

## First Order Logic

Extends propositional logic with:
- **Constant symbols** — representing objects (e.g., Minerva, Gryffindor)
- **Predicate symbols** — relations returning true/false (e.g., Person(x), BelongsTo(x, y))

Example: `Person(Minerva)` and `BelongsTo(Minerva, Gryffindor)`

### Universal Quantification (∀)

"For all" — applies to every entity in the domain.

```
∀x. BelongsTo(x, Gryffindor) → ¬BelongsTo(x, Hufflepuff)
```
If any entity belongs to Gryffindor, it doesn't belong to Hufflepuff.

### Existential Quantification (∃)

"There exists at least one."

```
∃x. House(x) ∧ BelongsTo(Minerva, x)
```
Minerva belongs to some house.

### Combined Quantification

```
∀x. Person(x) → (∃y. House(y) ∧ BelongsTo(x, y))
```
Every person belongs to a house.
