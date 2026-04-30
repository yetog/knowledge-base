---
tags:
  - ai
  - python
  - course
  - learning
---

# Quiz 4: Learning

**CS50's Introduction to Artificial Intelligence with Python**

---

## Question 1

**A social network's AI uses existing tagged photos to identify people in new photos. What type of machine learning is this?**

- **This is an example of supervised learning** ✓
- This is an example of reinforcement learning
- This is an example of unsupervised learning
- This is not an example of machine learning

> **Why:** The AI is trained on labeled input-output pairs (photos tagged with names). Learning from labeled examples to classify new inputs is the definition of supervised learning.

---

## Question 2

**Calculate the total L2 loss for five data points with the given true and predicted values.**

**Answer: 16** ✓

> **Why:** L2 loss = Σ(actual − predicted)². Square each individual error and sum. Unlike L1 loss (absolute values), L2 penalizes larger errors more heavily.

---

## Question 3

**If Hypothesis 1 has lower L1 and L2 loss than Hypothesis 2 on training data, why might Hypothesis 2 still be preferable?**

- Hypothesis 1 might result from regularization
- **Hypothesis 1 might result from overfitting** ✓
- Hypothesis 1 might result from loss
- Hypothesis 1 might result from cross-validation
- Hypothesis 1 might result from regression

> **Why:** A model with lower training loss isn't necessarily better — it may have memorized the training data (overfitting) and will generalize poorly to new examples. Hypothesis 2's higher training loss might mean it's a simpler, more generalizable model.

---

## Question 4

**In the ε-greedy approach to reinforcement learning, which ε value makes it identical to a purely greedy approach?**

- **ε = 0** ✓
- ε = 0.25
- ε = 0.5
- ε = 0.75
- ε = 1

> **Why:** With ε = 0, the probability of random exploration is 0% — the agent always exploits its best known action. With ε = 1, it would always explore randomly. The whole point of ε-greedy is balancing these extremes.
