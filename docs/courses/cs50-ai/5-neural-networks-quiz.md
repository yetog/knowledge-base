---
tags:
  - ai
  - python
  - course
  - learning
---

# Quiz 5: Neural Networks

**CS50's Introduction to Artificial Intelligence with Python**

---

## Question 1

**Network weights: w0 = -5, w1 = 2, w2 = -1, w3 = 3. Inputs: x1 = 3, x2 = 2, x3 = 4. What does the network compute using a step activation function? A ReLU activation function?**

- 0 for step, 0 for ReLU
- 0 for step, 1 for ReLU
- 1 for step, 0 for ReLU
- **1 for step, 11 for ReLU** ✓
- 1 for step, 16 for ReLU
- 11 for step, 11 for ReLU
- 16 for step, 16 for ReLU

> **Why:** Compute the weighted sum: −5 + (2×3) + (−1×2) + (3×4) = −5 + 6 − 2 + 12 = **11**
>
> - **Step:** Output 1 if value ≥ 0 → 11 ≥ 0 → **1**
> - **ReLU:** Output max(0, value) → max(0, 11) → **11**

---

## Question 2

**How many total weights (including biases) will a fully connected neural network have with: input layer (3 units), hidden layer (5 units), output layer (4 units)?**

**Answer: 44** ✓

> **Why:** Count connections + biases at each layer:
> - Input → Hidden: 3 × 5 = 15 weights + 5 biases = **20**
> - Hidden → Output: 5 × 4 = 20 weights + 4 biases = **24**
> - Total: 20 + 24 = **44**

---

## Question 3

**A recurrent neural network listens to audio speech and classifies it by whose voice it is. What architecture fits best?**

- One-to-one (single input, single output)
- **Many-to-one (multiple inputs, single output)** ✓
- One-to-many (single input, multiple outputs)
- Many-to-many (multiple inputs, multiple outputs)

> **Why:** The input is a sequence of audio frames (many inputs), and the output is a single speaker classification (one output). Many-to-one captures sequential data and produces a single label.

---

## Question 4

**Apply a 2×2 max-pool to a 4×4 grayscale image. What is the result?**

- [[16, 14], [32, 30]]
- [[22, 24], [32, 30]]
- **[[16, 12], [32, 28]]** ✓
- [[14, 12], [30, 28]]
- [[16, 14], [22, 24]]
- [[16, 12], [32, 30]]

> **Why:** Max-pooling divides the image into non-overlapping 2×2 regions and takes the maximum value from each. For each quadrant, find the largest pixel value — those become the output values.
