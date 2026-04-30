---
tags:
  - ai
  - python
  - course
  - learning
---

# Projects 3: Optimization

**CS50's Introduction to Artificial Intelligence with Python**

---

## Project — Crossword

**Build an AI that generates crossword puzzles by solving a constraint satisfaction problem.**

### Background

Given a crossword structure (grid) and a word list, assign words to variables satisfying all constraints.

Each **variable** is defined by: row (i), column (j), direction (ACROSS or DOWN), and length.

**Constraints:**
- **Unary:** Word length must match variable length
- **Binary:** Overlapping variables must share the same character at intersection points
- **Uniqueness:** No word can appear twice

### Code Structure

**`crossword.py`** (pre-built):
- `Variable` class — row, col, direction, length
- `Crossword` class — structure, words, variables, overlaps
- `crossword.overlaps[v1, v2]` → returns `(i, j)` overlap position or `None`
- `crossword.neighbors(v)` → returns overlapping variables

**`generate.py`** (implement this):
- `CrosswordCreator` — contains `crossword` and `domains` (variable → possible words)
- `solve()` calls your functions in order

### Specification

Implement 8 functions:

**`enforce_node_consistency()`**
Remove words from each variable's domain that don't match the variable's required length.

**`revise(x, y)`**
Make variable x arc-consistent with y. Remove values from x's domain where no valid y value exists at the overlap. Returns `True` if domain changed.

**`ac3(arcs=None)`**
Run AC-3 to enforce full arc consistency. Returns `False` if any domain empties (unsolvable), `True` otherwise.

**`assignment_complete(assignment)`**
Returns `True` if every variable has been assigned a word.

**`consistent(assignment)`**
Returns `True` if assignment satisfies all constraints:
- All words are distinct
- Words have correct lengths
- No conflicts at overlapping cells

**`order_domain_values(var)`**
Returns domain values sorted by least-constraining value heuristic — fewest eliminated choices for neighboring unassigned variables first.

**`select_unassigned_variable(assignment)`**
Returns the next variable to assign using:
1. **MRV** — fewest remaining domain values (primary)
2. **Degree** — most neighbors (tiebreaker)

**`backtrack(assignment)`**
Backtracking search. Returns complete assignment dict or `None` if unsolvable.

### Running It

```bash
python generate.py data/structure1.txt data/words1.txt
python generate.py data/structure1.txt data/words1.txt output.png  # with image
```

### Hints

- Start without heuristics, add them after the basic algorithm works
- Interleave inference with search: run AC-3 after each assignment (maintaining arc consistency) for a more efficient solver

```bash
check50 ai50/projects/2024/x/crossword
style50 generate.py
```
