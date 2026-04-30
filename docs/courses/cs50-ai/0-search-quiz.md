---
tags:
  - ai
  - python
  - course
  - learning
---

# Quiz 0: Search

**CS50's Introduction to Artificial Intelligence with Python**

---

## Question 1

**Between depth-first search (DFS) and breadth-first search (BFS), which will find a shorter path through a maze?**

- DFS will always find a shorter path than BFS
- BFS will always find a shorter path than DFS
- **BFS will sometimes, but not always, find a shorter path than DFS** ✓
- DFS will sometimes, but not always, find a shorter path than BFS
- Both algorithms will always find paths of the same length

> **Why:** BFS explores layer by layer and guarantees the *shortest* path — but only when one exists and is reachable. DFS may find a path faster in some cases but won't guarantee it's optimal.

---

## Question 2

**Which search algorithm could have produced a specific maze solution path shown?**

- DFS
- BFS
- Greedy best-first search
- A*

**Answer: Could only be DFS** ✓

> **Why:** The path shown backtracks and explores deep before widening — a characteristic of stack-based DFS. BFS and informed search algorithms would produce different shaped paths.

---

## Question 3

**Why is depth-limited minimax sometimes preferable to minimax without a depth limit?**

- Depth-limited minimax always produces better results
- Depth-limited minimax can be used when there is no utility function
- **Depth-limited minimax can arrive at a decision more quickly because it explores fewer states** ✓
- Depth-limited minimax will always find the optimal solution

> **Why:** Full minimax on complex games (like chess with ~10^29,000 possible games) is computationally infeasible. Depth limiting trades guaranteed optimality for practical speed, using an evaluation function to estimate utility at the cutoff.

---

## Question 4

**Calculate the value of the root node in the following Minimax tree.**

*(Tree diagram from lecture — maximizing node at root, alternating min/max layers)*

**Answer: 5** ✓

> **Why:** Work bottom-up — min nodes take the minimum of their children, max nodes take the maximum. Trace upward to find the value that propagates to the root.
