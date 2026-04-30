---
tags:
  - ai
  - python
  - course
  - learning
---

# Quiz 3: Optimization

**CS50's Introduction to Artificial Intelligence with Python**

---

## Question 1

**For which of the following will you always find the same solution, even if you re-run the algorithm multiple times?**

- Steepest-ascent hill-climbing, each time starting from a different starting state
- **Steepest-ascent hill-climbing, each time starting from the same starting state** ✓
- Stochastic hill-climbing, each time starting from a different starting state
- Stochastic hill-climbing, each time starting from the same starting state
- Both, so long as you always start from the same starting state
- No version of hill-climbing will guarantee the same solution every time

> **Why:** Steepest-ascent is **deterministic** — it always picks the single best neighbor. Given the same starting state, it follows the same path to the same result. Stochastic hill-climbing picks *randomly* from better neighbors, so the same start can yield different solutions.

---

## Question 2

**A farmer plants two crops: Crop 1 earns $500/acre, Crop 2 earns $400/acre. What is a valid objective function to maximize profit?**

- `500 * 10 * C1 + 400 * 4 * C2`
- `10 * C1 + 4 * C2`
- **`500 * C1 + 400 * C2`** ✓
- `-3 * C1 - 2 * C2`
- `C1 + C2`

> **Why:** The objective is to maximize total revenue. Each acre of C1 earns $500; each acre of C2 earns $400. The objective function captures profit per acre × acres planted.

---

## Question 3

**Same farming scenario. Crop 1 requires 3 hrs/acre (max 10 acres supply), Crop 2 requires 2 hrs/acre (max 4 acres supply), total labor is 12 hours. What are the constraints?**

- `3 * C1 + 2 * C2 <= 12; C1 + C2 <= 14`
- `3 * C1 <= 10; 2 * C2 <= 4`
- **`3 * C1 + 2 * C2 <= 12; C1 <= 10; C2 <= 4`** ✓
- `C1 + C2 <= 12; C1 + C2 <= 14`

> **Why:** Three independent constraints apply: (1) total labor budget, (2) supply limit on C1, (3) supply limit on C2. Each must be expressed as a separate inequality.

---

## Question 4

**An exam scheduling problem. After enforcing arc consistency on the entire CSP, what are the resulting domains for variables C, D, and E?**

- C: {Mon}, D: {Mon, Wed}, E: {Tue, Wed}
- C: {Mon}, D: {Tue}, E: {Wed}
- **C: {Mon}, D: {Mon, Wed}, E: {Tue, Wed}** ✓
- C: {Mon}, D: {Wed}, E: {Tue}
- C: {Mon, Tue}, D: {Wed}, E: {Mon}
- C: {Mon, Tue, Wed}, D: {Mon, Wed}, E: {Mon, Tue, Wed}

> **Why:** AC-3 propagates constraints: C's domain reduces to {Mon} based on its constraints. D must differ from C and can still be Mon or Wed. E must differ from D — with D possibly being Mon or Wed, E can only be Tue or Wed.
