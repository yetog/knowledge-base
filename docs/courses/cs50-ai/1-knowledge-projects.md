---
tags:
  - ai
  - python
  - course
  - learning
---

# Projects 1: Knowledge

**CS50's Introduction to Artificial Intelligence with Python**

---

## Project 1 — Knights

**Solve "Knights and Knaves" logic puzzles using propositional logic and model checking.**

### Background

From Raymond Smullyan's 1978 puzzles:
- **Knight:** Always tells the truth — if a knight says P, then P is true
- **Knave:** Always lies — if a knave says P, then P is false

Each character is exclusively one or the other. Goal: determine each character's type from their statements.

### Code Structure

**`logic.py`** — Logical connective classes (pre-built). Compose expressions like `And(Not(A), Or(B, C))`. The `model_check` function evaluates whether a KB entails a query.

**`puzzle.py`** — Defines symbols (`AKnight`, `AKnave`, `BKnight`, `BKnave`, `CKnight`, `CKnave`) and four empty knowledge bases.

### Specification

Populate four knowledge bases to solve each puzzle:

| Puzzle | Statements |
|---|---|
| **Puzzle 0** | A says: "I am both a knight and a knave." |
| **Puzzle 1** | A says: "We are both knaves." B says nothing. |
| **Puzzle 2** | A says: "We are the same kind." B says: "We are of different kinds." |
| **Puzzle 3** | A makes an ambiguous statement. B claims A said "I am a knave" and that "C is a knave." C claims "A is a knight." |

### Key Hints

- Each KB needs two types of information:
  1. **Puzzle structure rules** (each person is a knight XOR a knave)
  2. **Statement encodings** (what each character's statement implies given their type)
- A knight saying P → P is true. A knave saying P → P is false.
- Do not modify `logic.py`

```bash
check50 ai50/projects/2024/x/knights
```

---

## Project 2 — Minesweeper

**Build an AI that plays Minesweeper using logical inference.**

### Background

Rather than full propositional logic, use a simplified representation: each **sentence** is a set of cells paired with a count of how many are mines.

**Inference rules:**
- If count = 0 → all cells are safe
- If count = len(cells) → all cells are mines
- If `set1 ⊆ set2` → `(set2 − set1)` contains `count2 − count1` mines

### Code Structure

**`Minesweeper`** — Game logic (fully implemented)

**`Sentence`** — A logical statement about cells:
- `cells`: set of involved cells
- `count`: number of mines among them
- Implement: `known_mines()`, `known_safes()`, `mark_mine()`, `mark_safe()`

**`MinesweeperAI`** — The AI player:
- `self.moves_made`, `self.mines`, `self.safes`, `self.knowledge`
- Implement: `add_knowledge()`, `make_safe_move()`, `make_random_move()`

### Specification

**`Sentence` methods:**

| Method | Behavior |
|---|---|
| `known_mines()` | Return cells confirmed as mines |
| `known_safes()` | Return cells confirmed as safe |
| `mark_mine(cell)` | Remove cell, decrement count |
| `mark_safe(cell)` | Remove cell, count unchanged |

**`MinesweeperAI` methods:**

`add_knowledge(cell, count)` — core inference engine:
1. Mark cell as a move made and safe
2. Add new sentence based on cell's unrevealed neighbors and count
3. Mark newly confirmed mines/safes
4. Derive new sentences using subset inference
5. Repeat until no new inferences

`make_safe_move()` — return a known-safe unplayed cell, or `None`

`make_random_move()` — return random unplayed non-mine cell, or `None`

### Hints

- `add_knowledge()` will be your longest function — build it incrementally
- Use Python set operations: `copy()`, `difference()`, etc.
- Never modify a set while iterating over it
- The AI won't always win — some positions require guessing

```bash
pip3 install -r requirements.txt
check50 ai50/projects/2024/x/minesweeper
```
