---
tags:
  - ai
  - python
  - course
  - learning
---

# Week 4: Learning

**CS50's Introduction to Artificial Intelligence with Python**

---

Machine learning enables computers to recognize patterns from data rather than following explicit instructions. Three primary approaches: **supervised learning**, **reinforcement learning**, and **unsupervised learning**.

---

## Supervised Learning

Trains algorithms using input-output pairs to map inputs to outputs. The goal is creating a hypothesis function *h* that approximates an unknown natural function *f*.

---

## Classification

Maps inputs to **discrete outputs**.

### Nearest-Neighbor Classification

Assigns classification based on the single closest observation. Fails when a nearby outlier dominates the decision.

### k-Nearest-Neighbors

Examines the *k* nearest data points and selects the most frequent classification among them.

- More accurate than 1-NN
- Requires computing distances to every point — computationally expensive at scale

### Perceptron Learning

Establishes a decision boundary separating data classes.

- **Input vector:** x = (1, x₁, x₂)
- **Weight vector:** w = (w₀, w₁, w₂)
- **Decision rule:** Rain if `w₀ + w₁x₁ + w₂x₂ ≥ 0`

**Perceptron learning rule:** Weights update iteratively based on prediction errors.
- Correct prediction → no update
- Underestimate → increase weights
- Overestimate → decrease weights

**Hard threshold:** Binary output (0 or 1) — absolute predictions.

**Soft threshold:** Logistic function output between 0 and 1 — expresses confidence levels.

### Support Vector Machines

Creates decision boundaries that **maximize distance** from both classes — the **Maximum Margin Separator**.

- Handles non-linear boundaries and higher dimensions
- The maximum margin ensures new data points slightly differing from training examples won't be misclassified

---

## Regression

Maps inputs to **continuous values** rather than discrete classifications.

Example: predicting sales revenue based on advertising expenditure. The hypothesis function generates a line predicting output values rather than separating categories.

---

## Loss Functions

Quantify prediction inaccuracy.

| Function | Formula | Notes |
|---|---|---|
| **0-1 Loss** | 0 if correct, 1 if wrong | Classification |
| **L₁ Loss** | \|actual − predicted\| | Absolute differences |
| **L₂ Loss** | (actual − predicted)² | Penalizes outliers more severely |

---

## Overfitting and Regularization

**Overfitting:** Model fits training data perfectly but fails on new data.

**Regularization** penalizes complexity:

```
cost(h) = loss(h) + λ × complexity(h)
```

Higher λ → discourages complexity → less overfitting risk.

### Validation Strategies

**Holdout Cross Validation:** Split data into training and test sets.

**k-Fold Cross-Validation:** Divide data into *k* sets; train *k* times rotating test sets. Averages generalization estimates without losing data.

---

## scikit-learn

```python
from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

# Train on evidence + labels, evaluate on test data
model = Perceptron()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

## Reinforcement Learning

Trains agents through **reward and punishment** feedback. Agents observe environmental states, perform actions, and receive rewards (positive) or punishments (negative) based on outcomes.

### Markov Decision Processes

| Component | Description |
|---|---|
| **S** | Set of states |
| **Actions(S)** | Set of actions available in each state |
| **P(s' \| s, a)** | Transition model |
| **R(s, a, s')** | Reward function |

### Q-Learning

Uses a function **Q(s, a)** estimating the value of taking action *a* in state *s*.

**Update rule:**
```
Q(s, a) ← Q(s, a) + α(new value estimate − Q(s, a))
```

- **α (alpha):** Learning rate — controls how quickly new estimates override old ones
- Future rewards incorporate the highest estimated value of the next state's actions

### Explore vs. Exploit Tradeoff

**Greedy decision-making:** Always selects the action with the highest Q-value. Prevents discovering potentially better routes.

**ε-greedy algorithm:**
- With probability **1 − ε**: exploit (choose best known action)
- With probability **ε**: explore (choose randomly)

**Function approximation:** Enables Q-Learning in complex domains (like chess) by approximating Q-values using features rather than storing every state-action pair.

---

## Unsupervised Learning

Finds patterns in **unlabeled** input data — no pre-assigned classifications.

### k-Means Clustering

Groups similar data points together:

1. Randomly place *k* cluster centers
2. Assign each point to its nearest cluster center
3. Move each center to the mean of its assigned points
4. Repeat steps 2–3 until no point changes clusters (equilibrium)

Partitions data into *k* groups based on spatial similarity.
