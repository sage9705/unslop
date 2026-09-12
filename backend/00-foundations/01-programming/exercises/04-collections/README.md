# Exercise: Multi-Branch Stock Comparison

*`00-foundations/01-programming/exercises/04-collections/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

The shop has grown into three branches, each with its own inventory. The owner wants three things the [`stock-reorder-alert`](../../examples/stock-reorder-alert/) example never had to deal with, because it only ever looked at one branch:

1. A combined view of total stock per product across all branches.
2. A way to see which products a given branch doesn't carry at all, that other branches do.
3. Which single branch is holding the most total stock right now.

## What You Need to Build

In `starter.py`, you're given a `branches` dictionary shaped like:

```python
{
    "Branch A": {"Rice bag": 40, "Sugar": 10, "Cooking oil": 5},
    "Branch B": {"Rice bag": 15, "Flour": 20, "Sugar": 8},
    "Branch C": {"Cooking oil": 12, "Bread": 30},
}
```

Implement four functions:

1. **`combine_inventories(branches)`**, returns a single dict with the total quantity of each product summed across every branch.
2. **`all_products(branches)`**, returns a set of every distinct product name across every branch.
3. **`missing_products(branches, branch_name)`**, returns a set of products carried by other branches but not by `branch_name`.
4. **`branch_with_most_stock(branches)`**, returns the name of the branch with the highest total quantity across all of its own products.

## Concepts You'll Need

- [`07-collections.md`](../../concepts/07-collections.md)
- [`08-dictionaries-and-sets.md`](../../concepts/08-dictionaries-and-sets.md), especially set differences for `missing_products`

## Self Check

```bash
python starter.py
```

Set comparisons don't care about order, so `self_check()` compares your sets directly. You should see `All checks passed.` with no errors.
