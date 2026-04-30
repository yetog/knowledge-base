---
tags:
  - ai
  - python
  - course
  - learning
---

# Week 2: Uncertainty

**CS50's Introduction to Artificial Intelligence with Python**

---

## Probability Fundamentals

### Possible Worlds and Axioms

Every scenario is a **possible world** (ω). Core axioms:
- All probabilities range between 0 (impossible) and 1 (certain)
- Probabilities across all possible outcomes sum to 1

### Calculating Probabilities

Probability = favorable outcomes / total possible outcomes.

Example: Two dice yield 36 equally likely combinations. Only one produces a sum of 12, so **P(12) = 1/36**.

### Unconditional vs. Conditional Probability

**Unconditional probability:** Belief without any evidence.

**Conditional probability P(a|b):** Likelihood of event *a* given that *b* occurred.

```
P(a|b) = P(a ∧ b) / P(b)
```

This restricts consideration to worlds where *b* is true, then finds the proportion where *a* is also true.

---

## Random Variables and Independence

A **random variable** has a domain of possible values with associated probabilities.

Example — flight status:
```
{on time: 0.6, delayed: 0.3, canceled: 0.1}
```

**Independence:** One event's probability is unaffected by another.

```
P(a ∧ b) = P(a) × P(b)
```

---

## Bayes' Rule

Calculates P(b|a) from P(a|b):

```
P(b|a) = P(a|b) × P(b) / P(a)
```

**Example:** Given:
- 80% of rainy days start cloudy → P(cloudy|rain) = 0.8
- 40% of days are cloudy → P(cloudy) = 0.4
- 10% of days are rainy → P(rain) = 0.1

P(rain|cloudy) = (0.1 × 0.8) / 0.4 = **0.2 (20%)**

Bayes' rule reverses cause and effect — visible evidence infers hidden causes.

---

## Joint and Marginal Probability

**Joint probability tables** show the likelihood of multiple events co-occurring, enabling conditional distributions through normalization.

**Marginalization** recovers individual variable probabilities:
```
P(a) = P(a, b) + P(a, ¬b)
```

### Probability Rules Summary

| Rule | Formula |
|---|---|
| Negation | P(¬a) = 1 − P(a) |
| Inclusion-Exclusion | P(a ∨ b) = P(a) + P(b) − P(a ∧ b) |
| Marginalization | Sum joint probabilities across hidden variables |
| Conditioning | P(a) = P(a\|b)P(b) + P(a\|¬b)P(¬b) |

---

## Bayesian Networks

A directed graph where:
- Each **node** represents a random variable
- **Arrows** indicate dependency (parent → child)
- Each node stores **P(X | Parents(X))**

**Example structure:** Rain → Maintenance → Train → Appointment

Parents directly influence children; indirect ancestors don't appear in conditional probability tables.

### Inference in Bayesian Networks

**Components:**
- **Query variable (X):** Target of probability calculation
- **Evidence variables (E):** Observed facts
- **Hidden variables (Y):** Unobserved factors
- **Goal:** Calculate P(X|e)

**Inference by enumeration:** Sums joint probabilities of query and evidence across all hidden variable combinations, then normalizes.

### Code Example (Pomegranate)

```python
from pomegranate import *

# Root node
rain = Node(DiscreteDistribution({
    "none": 0.7, "light": 0.2, "heavy": 0.1
}), name="rain")

# Conditional node
maintenance = Node(ConditionalProbabilityTable([
    ["none", "yes", 0.4],
    ["none", "no", 0.6],
    # ... additional rows
], [rain.distribution]), name="maintenance")

model = BayesianNetwork()
model.add_states(rain, maintenance)
model.add_edge(rain, maintenance)
model.bake()
```

---

## Sampling Methods

### Basic Sampling

Generate approximate distributions by repeatedly sampling each variable according to its conditional probability given parent values. Count occurrences to estimate probabilities.

For conditional queries like P(Rain|Train=delayed), discard samples not matching the evidence constraint.

### Likelihood Weighting

More efficient than rejection sampling:

1. Fix evidence variables at observed values
2. Sample remaining variables using conditional probabilities
3. Weight each sample by P(evidence | sampled parents)

Avoids discarding incompatible samples entirely.

```python
def generate_sample():
    sample = {}
    parents = {}
    for state in model.states:
        if isinstance(state.distribution, ConditionalProbabilityTable):
            sample[state.name] = state.distribution.sample(parent_values=parents)
        else:
            sample[state.name] = state.distribution.sample()
        parents[state.distribution] = sample[state.name]
    return sample
```

---

## Markov Models

### The Markov Assumption

The current state depends only on a **finite fixed number of prior states**, making complex prediction tractable.

### Markov Chains

A sequence where each event's probability depends solely on the previous event.

**Requirements:**
- **Transition model:** P(Xₜ₊₁ | Xₜ)
- **Start probabilities:** Initial distribution

```python
model = MarkovChain([
    DiscreteDistribution({"sun": 0.5, "rain": 0.5}),
    ConditionalProbabilityTable([
        ["sun", "sun", 0.8],
        ["sun", "rain", 0.2],
        ["rain", "sun", 0.3],
        ["rain", "rain", 0.7]
    ], [start])
])
```

---

## Hidden Markov Models

Systems with **unobservable internal states** generating observable evidence.

**Examples:**
- Robot position (hidden) vs. sensor readings (observed)
- Spoken words (hidden) vs. audio waveforms (observed)
- User engagement (hidden) vs. analytics data (observed)

**Key components:**
- **Emission model:** P(observation | state)
- **Transition model:** P(next state | current state)
- **Sensor Markov assumption:** Evidence depends only on current state

**Applications:**

| Task | Description |
|---|---|
| Filtering | Current state probability given observations so far |
| Prediction | Future state probability |
| Smoothing | Past state probability given current observations |
| Most likely explanation | Most probable state sequence producing observations |

```python
sun = DiscreteDistribution({"umbrella": 0.2, "no umbrella": 0.8})
rain = DiscreteDistribution({"umbrella": 0.9, "no umbrella": 0.1})

transitions = numpy.array([[0.8, 0.2], [0.3, 0.7]])
starts = numpy.array([0.5, 0.5])

model = HiddenMarkovModel.from_matrix(
    transitions, [sun, rain], starts,
    state_names=["sun", "rain"])
```
