# Exercise: Sales Log Cleaner and Reporter

*`00-foundations/01-programming/exercises/05-data-processing/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

The shop's till exports a raw sales log at the end of the day. It's messy in exactly the way real exports are: inconsistent spacing, inconsistent capitalization, "Rice bag" and "RICE BAG" and "rice bag" all meaning the same product. Before you can report on anything, you need to clean it up, and you need to do it without accidentally corrupting the original log while you're at it.

## What You Need to Build

In `starter.py`, you're given a `RAW_LOG` list of raw comma separated strings. Implement four functions:

1. **`parse_log_line(raw_line)`**, splits a raw line into `(item_name, price, quantity)`. Clean up whitespace, and normalize the item name so different capitalizations of the same product match, `.title()` is a reasonable way to do this.
2. **`build_sales_report(raw_log)`**, returns a dict of `{item_name: total_revenue}`, summed across every line for that product.
3. **`total_quantity_sold(raw_log)`**, returns a dict of `{item_name: total_quantity}`, summed the same way.
4. **`mark_processed(log_lines)`**, returns a **new** list with `"[PROCESSED] "` added to the front of every line, **without modifying the original list**. This is the exact trap covered in [`concepts/11-mutation-and-references.md`](../../concepts/11-mutation-and-references.md), it's easy to accidentally return something that's secretly still pointing at the original data.

## Concepts You'll Need

- [`09-strings.md`](../../concepts/09-strings.md)
- [`10-scope.md`](../../concepts/10-scope.md), notice that `build_sales_report` and `total_quantity_sold` can each use a local variable with the same name without conflict
- [`11-mutation-and-references.md`](../../concepts/11-mutation-and-references.md), for `mark_processed`

## Self Check

```bash
python starter.py
```

`self_check()` verifies your parsing, your two reports, and specifically confirms that the original `RAW_LOG` list is completely untouched after calling `mark_processed`. You should see `All checks passed.` with no errors.
