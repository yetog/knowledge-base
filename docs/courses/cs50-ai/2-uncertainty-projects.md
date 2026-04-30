---
tags:
  - ai
  - python
  - course
  - learning
---

# Projects 2: Uncertainty

**CS50's Introduction to Artificial Intelligence with Python**

---

## Project 1 — PageRank

**Implement Google's PageRank algorithm using both sampling and iterative approaches.**

### Background

PageRank determines webpage importance based on which important pages link to it. Modeled as a **random surfer**: a user randomly clicks links across the web.

**Damping factor d = 0.85:**
- With probability d → follow a link on the current page
- With probability 1−d → jump to any page at random

**Iterative formula:**
```
PR(p) = (1 - d) / N + d × Σ PR(i) / NumLinks(i)
```
Where the sum is over all pages i that link to p.

### Specification

Implement three functions in `pagerank.py`:

**`transition_model(corpus, page, damping_factor)`**

Returns a probability distribution over which page the surfer visits next.
- With probability `d`: choose randomly from current page's links
- With probability `1 - d`: choose randomly from all pages
- If page has no outgoing links → treat as linking to all pages equally

Example: corpus `{"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}`, page `"1.html"`, d = 0.85 → `{"1.html": 0.05, "2.html": 0.475, "3.html": 0.475}`

**`sample_pagerank(corpus, damping_factor, n)`**

Estimates PageRank by generating n samples via the transition model.
- First sample: randomly chosen page
- Each subsequent sample: use previous page's transition probabilities
- Return proportion of samples on each page

**`iterate_pagerank(corpus, damping_factor)`**

Calculates PageRank using iterative formula application.
- Start: all pages have rank 1/N
- Repeatedly apply formula until all changes ≤ 0.001
- Pages with no links → treat as linking to every page (including itself)

### Hints

- Use Python's `random` module for sampling decisions
- Both methods should return values that sum to 1

```bash
check50 ai50/projects/2024/x/pagerank
style50 pagerank.py
```

---

## Project 2 — Heredity

**Model genetic inheritance and compute probabilities using a Bayesian network.**

### Background

Models the GJB2 gene (linked to hearing impairment). People carry 0, 1, or 2 copies of a mutated gene (hidden state). Trait expression depends on gene count (observable).

**Probabilities provided (`PROBS` dict):**

| Variable | Values |
|---|---|
| Base gene distribution | 96% (0 copies), 3% (1 copy), 1% (2 copies) |
| Trait expression | 1% (0 genes), ~56% (1 gene), 65% (2 genes) |
| Mutation rate | 1% — gene can change during inheritance |

Children inherit one gene copy from each parent. Each inherited copy has a 1% chance of mutation.

### Specification

Implement three functions in `heredity.py`:

**`joint_probability(people, one_gene, two_genes, have_trait)`**

Returns the joint probability of all the given gene counts and traits.
- For people **without** parents: use `PROBS["gene"]` directly
- For people **with** parents: calculate inheritance probability accounting for mutation
- Multiply by `PROBS["trait"]` for each person's trait status
- Return the product of all individual probabilities

**`update(probabilities, one_gene, two_genes, have_trait, p)`**

Adds joint probability p to the running totals in `probabilities`.
- `probabilities[person]["gene"][count] += p`
- `probabilities[person]["trait"][bool] += p`
- Modifies in-place, no return

**`normalize(probabilities)`**

Normalizes all distributions so they sum to 1.
- Divide each value by the sum of its distribution
- Modifies in-place, no return

### Worked Example

Family: Harry (child of Lily and James), with James having 2 genes and the trait:

```
joint_probability(people, {"Harry"}, {"James"}, {"James"}) ≈ 0.00266432
```

### Hints

- Joint probabilities are products — multiply everything together
- When a parent has 1 gene, they pass it with 50% probability (accounting for mutation)
- Consider both inheritance pathways for children

```bash
check50 ai50/projects/2024/x/heredity
```
