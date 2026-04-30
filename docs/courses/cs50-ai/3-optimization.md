---
tags:
  - ai
  - python
  - course
  - learning
---

# Week 3: Optimization

**CS50's Introduction to Artificial Intelligence with Python**

---

Optimization is choosing the best option from a set of possible options.

---

## Local Search

Maintains a single node and explores neighboring nodes — differs from pathfinding by seeking the *best* answer rather than the quickest route. Often settles for satisfactory rather than globally optimal solutions to conserve computation.

### Key Definitions

| Term | Meaning |
|---|---|
| **Objective Function** | Maximizes solution value |
| **Cost Function** | Minimizes solution cost |
| **Current State** | The state presently under consideration |
| **Neighbor State** | An adjacent state reachable from the current state |

**Example:** In a hospital placement problem, the sum of Manhattan distances from houses to nearest hospitals represents the cost to minimize.

---

## Hill Climbing

Compares neighbor states to the current state, moving to any superior neighbor.

```
function Hill-Climb(problem):
    current = initial state of problem
    repeat:
        neighbor = best valued neighbor of current
        if neighbor not better than current:
            return current
        current = neighbor
```

### Limitations — Local vs. Global Extrema

| Term | Meaning |
|---|---|
| **Local Maximum** | Superior to neighboring states only |
| **Global Maximum** | Highest value across all states |
| **Local Minimum** | Lower than neighboring states only |
| **Global Minimum** | Lowest value across all states |

Hill climbing is **myopic** — it can get trapped at local optima, flat plateaus, or shoulders.

### Variants

| Variant | Description |
|---|---|
| **Steepest-ascent** | Select the highest-valued neighbor (standard) |
| **Stochastic** | Randomly choose from superior-valued neighbors |
| **First-choice** | Select the first better-valued neighbor found |
| **Random-restart** | Run hill climbing multiple times from random states |
| **Local Beam Search** | Track the *k* best-valued neighbors simultaneously |

---

## Simulated Annealing

Inspired by the metallurgical process of heating metal and cooling slowly. Accepts worse neighbors early (high temperature) but becomes increasingly selective as temperature decreases.

```
function Simulated-Annealing(problem, max):
    current = initial state of problem
    for t = 1 to max:
        T = Temperature(t)
        neighbor = random neighbor of current
        ΔE = how much better neighbor is than current
        if ΔE > 0:
            current = neighbor
        with probability e^(ΔE/T) set current = neighbor
    return current
```

The probability formula **e^(ΔE/T)** ensures: increasingly negative energy differences and higher temperatures yield greater acceptance probabilities.

### Traveling Salesman Problem

Requires connecting all points while choosing the shortest possible distance. With just 10 points, there are **10! = 3,628,800** possible routes. Simulated annealing provides computationally efficient approximations.

---

## Linear Programming

Optimizes a linear equation subject to constraints.

**Components:**
- **Cost function:** c₁x₁ + c₂x₂ + … + cₙxₙ
- **Constraints:** Linear inequalities or equalities (a₁x₁ + a₂x₂ + … ≤ b)
- **Variable bounds:** lᵢ ≤ xᵢ ≤ uᵢ

```python
import scipy.optimize

result = scipy.optimize.linprog(
    [50, 80],                          # Cost function: 50x₁ + 80x₂
    A_ub=[[5, 2], [-10, -12]],
    b_ub=[20, -90],
)

if result.success:
    print(f"X1: {round(result.x[0], 2)} hours")
    print(f"X2: {round(result.x[1], 2)} hours")
```

---

## Constraint Satisfaction

Problems where variables need to be assigned values while satisfying conditions.

**Components:**
- Set of variables (x₁, x₂, …, xₙ)
- Domain set for each variable
- Set of constraints C

### Constraint Types

| Type | Description |
|---|---|
| **Hard Constraint** | Must be satisfied in correct solutions |
| **Soft Constraint** | Expresses preference between solutions |
| **Unary Constraint** | Involves one variable |
| **Binary Constraint** | Involves two variables |

---

## Consistency

### Node Consistency

All values in a variable's domain satisfy its **unary constraints**. Achieved by removing incompatible domain values based on single-variable restrictions.

### Arc Consistency

All values in a variable's domain satisfy its **binary constraints**. To make arc (X, Y) consistent: remove elements from X's domain until every X value permits at least one valid Y value.

**Revise Algorithm:**

```
function Revise(csp, X, Y):
    revised = false
    for x in X.domain:
        if no y in Y.domain satisfies constraint for (X,Y):
            delete x from X.domain
            revised = true
    return revised
```

**AC-3 Algorithm:**

```
function AC-3(csp):
    queue = all arcs in csp
    while queue non-empty:
        (X, Y) = Dequeue(queue)
        if Revise(csp, X, Y):
            if size of X.domain == 0:
                return false
            for each Z in X.neighbors - {Y}:
                Enqueue(queue, (Z, X))
    return true
```

---

## Backtracking Search

Takes into account the structure of constraint satisfaction problems — assigns one variable at a time and backtracks when a contradiction is found.

```
function Backtrack(assignment, csp):
    if assignment complete:
        return assignment
    var = Select-Unassigned-Var(assignment, csp)
    for value in Domain-Values(var, assignment, csp):
        if value consistent with assignment:
            add {var = value} to assignment
            result = Backtrack(assignment, csp)
            if result ≠ failure:
                return result
            remove {var = value} from assignment
    return failure
```

### Inference Integration

**Maintaining Arc-Consistency (MAC):** Runs AC-3 after each variable assignment, propagating constraints before exploring further.

### Selection Heuristics

| Heuristic | Strategy |
|---|---|
| **Minimum Remaining Values (MRV)** | Select the variable with the fewest remaining domain values |
| **Degree Heuristic** | Choose the variable with the most arc connections |
| **Least Constraining Values** | Select values that constrain the fewest other variables |

MRV and Degree together identify which variable to assign next. Least Constraining Values determines which value to try first, minimizing future conflicts.
