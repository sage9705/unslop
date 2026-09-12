# Exercise: Stock Status Report

*`00-foundations/01-programming/exercises/02-control-flow/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

The [`stock-reorder-alert`](../../examples/stock-reorder-alert/) example only distinguishes three states: out of stock, needs reordering, or fine. A shop owner asks for something more useful: a fourth tier that catches items getting low, before they're urgent enough to reorder immediately.

## What You Need to Build

In `starter.py`, implement two functions:

1. **`get_status(quantity, reorder_threshold=5, low_threshold=15)`**, returns one of four strings based on `quantity`:

   - `"Out of Stock"` if quantity is `0`
   - `"Reorder Now"` if quantity is greater than `0` but at or below `reorder_threshold`
   - `"Low"` if quantity is above `reorder_threshold` but at or below `low_threshold`
   - `"Well Stocked"` otherwise
2. **`summarize_inventory(inventory, reorder_threshold=5, low_threshold=15)`**, loops through a list of `(product_name, quantity)` tuples and returns a dictionary counting how many products fall into each of the four status categories, shaped like:

   ```python
   {"Out of Stock": 1, "Reorder Now": 2, "Low": 1, "Well Stocked": 2}
   ```

## Concepts You'll Need

- [`04-conditionals.md`](../../concepts/04-conditionals.md)
- [`05-loops.md`](../../concepts/05-loops.md)

## Self Check

```bash
python starter.py
```

It will print the status of every product in the sample inventory, then run `self_check()` against known correct answers. You should see `All checks passed.` at the end.
