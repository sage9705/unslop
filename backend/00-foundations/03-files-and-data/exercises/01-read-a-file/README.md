# Exercise: Read a File

*`00-foundations/03-files-and-data/exercises/01-read-a-file/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

The shop keeps a record of every supplier delivery in `deliveries.txt`. The owner wants to know what the shop spent across all deliveries, and which single delivery cost the most.

Open `deliveries.txt` and look at it before writing anything. It has a header line, a blank line in the middle, and a different kind of value in each column. Your reading code has to cope with all of that.

## What You Need to Build

In `starter.py`, implement three functions:

1. **`read_deliveries(filepath)`**, reads the file and returns a list of `(date, item, quantity, unit_cost)` tuples. Skip the header line and any blank lines. Convert `quantity` to an `int` and `unit_cost` to a `float`.
2. **`total_cost(deliveries)`**, returns the sum of `quantity * unit_cost` across every delivery.
3. **`largest_delivery(deliveries)`**, returns the single delivery tuple with the highest `quantity * unit_cost`.

## Concepts You'll Need

- [`04-reading-files.md`](../../concepts/04-reading-files.md)
- [`06-file-paths.md`](../../concepts/06-file-paths.md), `starter.py` builds its path to `deliveries.txt` from `__file__`, so it works from any directory

## Self Check

```bash
python starter.py
```

It prints each delivery you read, then runs `self_check()`. You should see `All checks passed.` at the end.
