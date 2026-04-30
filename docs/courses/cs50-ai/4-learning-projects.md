---
tags:
  - ai
  - python
  - course
  - learning
---

# Projects 4: Learning

**CS50's Introduction to Artificial Intelligence with Python**

---

## Project 1 — Shopping

**Build a k-nearest-neighbor classifier to predict whether online shoppers will complete a purchase.**

### Background

When users browse a retail site, most won't buy. A naive classifier that always predicts "no purchase" would have high accuracy but be useless. This project emphasizes two metrics:

- **Sensitivity** (true positive rate) — proportion of actual purchasers correctly identified
- **Specificity** (true negative rate) — proportion of non-purchasers correctly identified

### Data

~12,000 user sessions with 17 evidence columns + 1 label (`Revenue: TRUE/FALSE`):

| Columns | Type |
|---|---|
| Administrative, Informational, ProductRelated (counts) | Integer |
| Duration columns, BounceRates, ExitRates, PageValues, SpecialDay | Float |
| Month | Integer (0=Jan … 11=Dec) |
| OperatingSystems, Browser, Region, TrafficType | Integer |
| VisitorType | 1 (returning) or 0 (other) |
| Weekend | 1 (True) or 0 (False) |

### Specification

Implement 3 functions in `shopping.py`:

**`load_data(filename)`**

Returns `(evidence, labels)` tuple:
- `evidence` — list of 17-element lists (numeric)
- `labels` — list of integers (1 = purchase, 0 = no purchase)
- Apply all type conversions from the table above

**`train_model(evidence, labels)`**

Returns a fitted `KNeighborsClassifier` with k=1.

```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=1)
model.fit(evidence, labels)
return model
```

**`evaluate(labels, predictions)`**

Returns `(sensitivity, specificity)` as floats 0–1:
```
sensitivity = correctly predicted purchases / total actual purchases
specificity = correctly predicted non-purchases / total actual non-purchases
```

### Constraints

- Only modify the three specified functions
- Use Python's standard `csv` module for file loading
- Don't modify `shopping.csv`

```bash
pip3 install scikit-learn
check50 ai50/projects/2024/x/shopping
```

---

## Project 2 — Nim

**Teach an AI to play Nim optimally through reinforcement learning (Q-learning).**

### Background

Nim: players take turns removing objects from piles. The player forced to take the last object loses.

- **State:** current pile configuration, e.g., `[1, 1, 3, 5]`
- **Action:** `(i, j)` = remove j objects from pile i
- **Rewards:** +1 for winning, -1 for losing, 0 for continuing
- **Q-learning update:**

```
Q(s, a) ← Q(s, a) + α × (reward + future_reward − Q(s, a))
```

### Code Structure

**`Nim`** — game state, `available_actions(piles)`, move execution (pre-built)

**`NimAI`** — learning agent with `self.q` (Q-value dict), `alpha` (learning rate), `epsilon` (exploration rate)

Training occurs through self-play simulations.

### Specification

Implement 4 functions in `NimAI`:

**`get_q_value(state, action)`**

Returns Q-value for the state-action pair. Returns 0 if not in `self.q`. Convert state lists to tuples for dict keys.

**`update_q_value(state, action, old_q, reward, future_rewards)`**

Applies the Q-learning update:
```
new_Q = old_Q + alpha × (reward + future_rewards − old_Q)
```
Stores result in `self.q`.

**`best_future_reward(state)`**

Returns the highest Q-value among available actions. Returns 0 if no actions available or all Q-values are unknown.

**`choose_action(state, epsilon=False)`**

- **Greedy (epsilon=False):** Pick action with highest Q-value
- **ε-greedy (epsilon=True):** With probability `self.epsilon` pick randomly; otherwise pick best action
- Ties may resolve to any option

### Hints

- `tuple(list)` converts states for use as dict keys
- After training (self-play), the AI should never lose to a human opponent

```bash
python play.py  # interactive testing after training
check50 ai50/projects/2024/x/nim
```
