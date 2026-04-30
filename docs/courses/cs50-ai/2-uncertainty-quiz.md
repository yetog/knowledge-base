---
tags:
  - ai
  - python
  - course
  - learning
---

# Quiz 2: Uncertainty

**CS50's Introduction to Artificial Intelligence with Python**

---

## Question 1

**A standard 52-card deck has 13 values in 4 suits. If a card is drawn at random, what is the probability it is a spade or a two?**

- About 0.019
- About 0.077
- About 0.17
- About 0.25
- **About 0.308** ✓
- About 0.327
- About 0.5

> **Why:** Use inclusion-exclusion: P(spade ∨ two) = P(spade) + P(two) − P(spade ∧ two)
> = 13/52 + 4/52 − 1/52 = 16/52 ≈ **0.308**
> The two of spades gets counted in both sets, so subtract it once.

---

## Question 2

**Flipping two fair coins, what is the probability that one lands heads and the other lands tails?**

**Answer: 0.5** ✓

> **Why:** Possible outcomes: HH, HT, TH, TT — each with probability 0.25. Outcomes with one head and one tail: HT and TH = 0.25 + 0.25 = **0.5**.

---

## Question 3

**From the Bayesian Network in lecture (Rain → Maintenance → Train → Appointment), which statement is true?**

- Rain affects appointment probability when train is on time
- Maintenance affects train punctuality when rain is known
- Rain affects train punctuality when maintenance is known
- **Assuming we know the train is on time, whether or not there is track maintenance does not affect the probability that the appointment is attended.** ✓
- Rain affects appointment when maintenance is known

> **Why:** In a Bayesian network, once we observe a node (Train = on time), the path from its parents (Maintenance) to its children (Appointment) is **blocked**. This is conditional independence — knowing the train status screens off maintenance from affecting the appointment.

---

## Question 4

**Factory A produces 60% of batteries (2% defect rate). Factory B produces 40% (4% defect rate). What is the probability that a battery is both made by Factory A and defective?**

**Answer: 0.012** ✓

> **Why:** P(Factory A ∧ defective) = P(defective | Factory A) × P(Factory A) = 0.02 × 0.60 = **0.012**
