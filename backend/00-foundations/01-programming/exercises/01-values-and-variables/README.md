# Exercise: Delivery Slip Calculator

*`00-foundations/01-programming/exercises/01-values-and-variables/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

A supplier drops off stock at the shop. The delivery details arrive exactly the way they would from a paper delivery note being typed into a spreadsheet: as plain text, not numbers. Your job is to turn that raw text into a proper delivery slip with a calculated total for each item.

This is the same trap covered in [`concepts/02-types.md`](../../concepts/02-types.md): a unit cost of `"18.00"` looks like a number, but until it's converted, Python treats it as text, and `"18.00" * "24"` doesn't mean what you want it to mean.

## What You Need to Build

In `starter.py`, implement four functions:

1. **`parse_cost(cost_text)`**, converts a raw price string like `"18.00"` into a proper float.
2. **`parse_quantity(quantity_text)`**, converts a raw quantity string like `"24"` into a proper int.
3. **`calculate_delivery_cost(unit_cost, quantity)`**, returns the total cost for that line of the delivery.
4. **`format_delivery_line(item_name, unit_cost, quantity, total_cost)`**, returns one readable line of text combining all four pieces of information. The exact spacing is up to you, it just needs to be readable.

## Concepts You'll Need

- [`01-values-and-variables.md`](../../concepts/01-values-and-variables.md)
- [`02-types.md`](../../concepts/02-types.md)
- [`03-expressions-and-operators.md`](../../concepts/03-expressions-and-operators.md)

## Self Check

Once all four functions are implemented, run:

```bash
python starter.py
```

It will print a formatted line for each of the three sample deliveries, then run `self_check()`, which confirms your conversions and calculations are exactly right. You should see `All checks passed.` at the end with no errors above it.
