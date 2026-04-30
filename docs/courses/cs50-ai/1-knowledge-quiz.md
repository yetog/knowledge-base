---
tags:
  - ai
  - python
  - course
  - learning
---

# Quiz 1: Knowledge

**CS50's Introduction to Artificial Intelligence with Python**

---

## Question 1

**Which of the following logical entailments is true?**

- Sentence 6 entails Sentence 2
- Sentence 1 entails Sentence 4
- Sentence 6 entails Sentence 3
- **Sentence 2 entails Sentence 5** ✓
- Sentence 1 entails Sentence 2
- Sentence 5 entails Sentence 6

> **Why:** α ⊨ β means in every world where α is true, β is also true. Evaluate each sentence pair by checking if the truth of the first forces the truth of the second across all models.

---

## Question 2

**Which of the following is logically equivalent to `A ⊕ B`?** (where ⊕ represents exclusive or)

- **`(A ∨ B) ∧ ¬(A ∧ B)`** ✓
- `(A ∧ B) ∨ ¬(A ∨ B)`
- `(A ∨ B) ∧ (A ∧ B)`
- `(A ∨ B) ∧ ¬(A ∨ B)`

> **Why:** Exclusive or is true when exactly one of A or B is true. `(A ∨ B)` ensures at least one is true. `¬(A ∧ B)` ensures both aren't true simultaneously. The conjunction captures "one or the other, but not both."

---

## Question 3

**Which of the following is a propositional logic representation of "If it is raining, then it is cloudy and not sunny"?**

- `(R → C) ∧ ¬S`
- `R → C → ¬S`
- `R ∧ C ∧ ¬S`
- **`R → (C ∧ ¬S)`** ✓
- `(C ∨ ¬S) → R`

> **Why:** The implication `R → (C ∧ ¬S)` reads "if R, then (C and not S)." The parentheses matter — both C and ¬S must follow from R together, not separately.

---

## Question 4

**Which of the following is a first-order logic translation of "There is a course that Harry and Hermione are both enrolled in"?**

- **`∃x. Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)`** ✓
- `∀x. Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)`
- `∃x. Enrolled(Harry, x) ∧ ∃y. Enrolled(Hermione, y)`
- `∀x. Enrolled(Harry, x) ∧ ∀y. Enrolled(Hermione, y)`
- `∃x. Enrolled(Harry, x) ∨ Enrolled(Hermione, x)`
- `∀x. Enrolled(Harry, x) ∨ Enrolled(Hermione, x)`

> **Why:** "There is a course" → existential quantifier ∃. The same variable x must appear in both Enrolled predicates to ensure it's the *same* course, not two different ones.
