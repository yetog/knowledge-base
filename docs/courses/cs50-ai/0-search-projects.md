---
tags:
  - ai
  - python
  - course
  - learning
---

# Projects 0: Search

**CS50's Introduction to Artificial Intelligence with Python**

---

## Project 1 — Degrees

**Find the shortest connection between two actors via shared movies (Six Degrees of Kevin Bacon).**

### Background

Any two Hollywood actors can be connected within ~6 steps, where each step is a shared film. Example: Jennifer Lawrence → Kevin Bacon (shared X-Men: First Class) → Tom Hanks (shared Apollo 13) = 2 degrees.

### Goal

Implement the `shortest_path` function to find the minimum degree of separation between two actors using BFS. States represent people; actions represent movies connecting them.

### Data

Three CSV files provided (`people.csv`, `movies.csv`, `stars.csv`). Pre-built dictionaries: `names`, `people`, `movies`.

### Specification

Implement `shortest_path(source, target)`:
- Accepts two person IDs
- Returns a list of `(movie_id, person_id)` tuples representing the path
- Returns `None` if no path exists
- Any valid minimum-length path is acceptable

```python
# Use the provided helper
neighbors_for_person(person_id)  # returns set of (movie_id, person_id) tuples
```

### Hints

- Check for goal state when **adding** to frontier (more efficient than checking on removal)
- Use `util.py`'s provided `Node`, `StackFrontier`, `QueueFrontier` classes
- BFS guarantees shortest path — use a queue frontier

---

## Project 2 — Tic-Tac-Toe

**Implement an unbeatable Tic-Tac-Toe AI using Minimax.**

### Background

With optimal play from both sides, Tic-Tac-Toe always ends in a draw. The AI should never lose.

### Getting Started

```bash
pip3 install -r requirements.txt  # installs pygame
```

Two files: `tictactoe.py` (implement this) and `runner.py` (graphical interface, pre-built).

Board is a 3×3 list of lists containing `X`, `O`, or `EMPTY`.

### Specification

Implement these 7 functions:

| Function | Description |
|---|---|
| `player(board)` | Returns whose turn it is — `X` or `O` |
| `actions(board)` | Returns set of valid moves as `(i, j)` tuples |
| `result(board, action)` | Returns new board after move — do **not** modify original |
| `winner(board)` | Returns `X`, `O`, or `None` |
| `terminal(board)` | Returns `True` if game over |
| `utility(board)` | Returns 1 (X wins), -1 (O wins), 0 (tie) |
| `minimax(board)` | Returns optimal move `(i, j)` for current player |

### Key Rules

- `result()` must use deep copy — original board unchanged
- `minimax()` returns `None` for terminal boards
- Multiple equally optimal moves — return any

### Hints

- Alpha-beta pruning is optional but improves efficiency
- Helper functions are allowed if they don't conflict with existing names

```bash
check50 ai50/projects/2024/x/tictactoe
style50 tictactoe.py
```
