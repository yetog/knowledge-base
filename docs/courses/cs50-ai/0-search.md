---
tags:
  - ai
  - python
  - course
  - learning
---

# Week 0: Search

**CS50's Introduction to Artificial Intelligence with Python**

---

## Search Problems

Search involves an agent transitioning from an initial state toward a goal state using algorithmic reasoning. Navigation apps exemplify practical search applications.

### Key Components

**Agent:** An entity perceiving its environment and making decisions based on observations.

**State:** A configuration describing the agent's position within the environment. Initial states represent starting points.

**Actions:** Decision points available in a given state, formally represented as functions returning applicable moves.

**Transition Model:** Functions describing state changes resulting from specific actions.

**State Space:** The complete collection of reachable states from the initial configuration, visualizable as directed graphs.

**Goal Test:** The evaluation criterion determining whether a state satisfies the objective.

**Path Cost:** Numerical values measuring the expense of traversing specific routes toward solutions.

---

## Search Solutions

**Solution:** A sequence of actions progressing from the initial to goal state.

**Optimal Solution:** The solution carrying the minimal path cost among all possible solutions.

### Node Data Structure

Nodes store essential search information:
- Current state representation
- Parent node reference
- Action triggering the current node's generation
- Path cost from initiation to the present node

Nodes enable solution reconstruction by tracing parent-child relationships backward through the explored space.

### Frontier Mechanism

The frontier manages nodes during search execution:

1. Return failure if frontier is empty
2. Remove a candidate node from frontier
3. Test for goal state achievement
4. Expand non-goal nodes and append new candidates to frontier
5. Archive examined nodes in explored set

---

## Uninformed Search Algorithms

### Depth-First Search (DFS)

DFS exhausts each direction completely before exploring alternatives, using a **stack** structure (last-in, first-out).

**Advantages:**
- Optimal speed when the algorithm selects the correct initial path

**Disadvantages:**
- Solutions may be suboptimal
- Worst-case performance explores all possible paths

```python
def remove(self):
    if self.empty():
        raise Exception("empty frontier")
    else:
        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node
```

### Breadth-First Search (BFS)

BFS progresses uniformly across all directions using a **queue** structure (first-in, first-out). One step occurs in every direction before proceeding further.

**Advantages:**
- Guaranteed optimal solution discovery

**Disadvantages:**
- Typically requires longer execution periods
- Worst-case performance is computationally intensive

```python
def remove(self):
    if self.empty():
        raise Exception("empty frontier")
    else:
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node
```

---

## Informed Search Algorithms

Informed algorithms leverage domain knowledge to guide exploration, improving performance over uninformed methods.

### Greedy Best-First Search

Prioritizes nodes nearest to the goal using a heuristic function **h(n)** estimating proximity to the objective.

**Manhattan Distance:** Calculates orthogonal steps (up, down, left, right) required to reach the goal, ignoring obstacles.

**Limitations:** Heuristic functions can mislead algorithms toward inefficient paths despite their general utility.

### A* Search

A* synthesizes two cost components:
- **g(n):** Accumulated cost reaching the current node
- **h(n):** Estimated cost from the current node to the goal

The algorithm tracks **g(n) + h(n)**, abandoning paths when their combined cost exceeds previously discovered alternatives.

**Optimality Requirements** — the heuristic must be:
1. **Admissible** — never overestimating actual costs
2. **Consistent** — satisfying `h(n) ≤ h(n') + c` for successors *n'* with transition cost *c*

---

## Adversarial Search

Adversarial algorithms navigate environments where opponents pursue conflicting objectives, commonly used in game AI.

### Minimax Algorithm

Assigns value outcomes as **-1** (one player) and **+1** (opposing player), with alternating minimization and maximization strategies.

**Game State Representation:**

| Symbol | Meaning |
|--------|---------|
| S₀ | Empty initial board |
| Players(s) | Returns current player |
| Actions(s) | Returns legal moves |
| Result(s, a) | Returns resulting game state |
| Terminal(s) | Indicates game completion |
| Utility(s) | Returns final value (-1, 0, or 1) |

**Pseudocode:**

```
Max-Value(state):
  v = -∞
  if Terminal(state): return Utility(state)
  for action in Actions(state):
    v = Max(v, Min-Value(Result(state, action)))
  return v

Min-Value(state):
  v = ∞
  if Terminal(state): return Utility(state)
  for action in Actions(state):
    v = Min(v, Max-Value(Result(state, action)))
  return v
```

### Alpha-Beta Pruning

Eliminates branches that cannot affect the final decision. Once a value establishes one action's superiority, exploring alternatives with worse preliminary indicators becomes unnecessary — reducing computational overhead significantly.

**Example:** Finding a minimizing move with value 3 when a maximizing alternative already scores 4 eliminates further investigation of that branch.

### Depth-Limited Minimax

Complete minimax is computationally infeasible for complex games. Chess has approximately **10^29,000** possible games — exhaustive analysis is impossible.

Depth-limited approaches evaluate only predetermined move sequences without reaching terminal states, relying on **evaluation functions** that estimate expected utility from non-terminal positions. In chess, evaluations consider piece quantities, positions, and board configurations.
