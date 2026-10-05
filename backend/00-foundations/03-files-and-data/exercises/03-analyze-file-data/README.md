# Exercise: Analyze File Data

*`00-foundations/03-files-and-data/exercises/03-analyze-file-data/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

The till exports `sales_log.txt` at closing time. Real exports are messy. This one has a header, a blank line, a line with missing fields, and a line where the amount says `twenty` instead of a number. The owner wants to know how much each product earned, and which payment method customers use most.

A program that crashes on the first bad line is no use to anyone. Yours has to read the good lines, skip the bad ones, and report how many it skipped.

## What You Need to Build

In `starter.py`, implement three functions:

1. **`read_sales(filepath)`**, returns `(sales, skipped_count)`. `sales` is a list of `(item, amount, payment)` tuples with `amount` as a float. Skip the header and blank lines without counting them. Skip malformed lines and count each one.
2. **`revenue_by_item(sales)`**, returns a dict of `{item: total_revenue}`, rounded to 2 decimal places.
3. **`busiest_payment_method(sales)`**, returns the payment method that appears in the most sales.

## Concepts You'll Need

- [`04-reading-files.md`](../../concepts/04-reading-files.md)
- [`10-parsing.md`](../../concepts/10-parsing.md)
- [`11-data-validation.md`](../../concepts/11-data-validation.md), deciding what counts as a line worth keeping
- [`13-errors-and-exceptions.md`](../../../01-programming/concepts/13-errors-and-exceptions.md), from `01-programming`, for handling a number that won't convert

## Self Check

```bash
python starter.py
```

You should see `All checks passed.`
