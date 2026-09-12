# Exercise: Supplier Order Manager

*`00-foundations/01-programming/exercises/06-supplier-order-manager/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

Everything so far has looked at the shop from the customer facing side, sales, receipts, feedback. This exercise looks at the other side: placing restock orders with suppliers. It's the same shape as [`examples/shop-inventory-tracker/`](../../examples/shop-inventory-tracker/), a catalog, validation, error handling, and persistence, split across modules, but applied to a genuinely different problem, so working through it means actually understanding the pattern, not recognizing it.

A shop deals with more than one supplier, and each supplier only carries certain products at their own prices. An order can fail for real reasons: the supplier doesn't carry that item, or someone typed a negative quantity by mistake. Both need to be caught and reported clearly, not allowed to crash the whole program.

## What You Need to Build

This exercise is split into two files, the way [`concepts/12-modules.md`](../../concepts/12-modules.md) describes:

- **`orders.py`**, you implement this one. It contains:

  1. **`place_order(supplier_catalog, supplier_name, item_name, quantity)`**, looks up the unit cost and returns `unit_cost * quantity`. Raise `KeyError` if the supplier doesn't exist, or if that supplier doesn't carry `item_name`. Raise `ValueError` if `quantity` is `0` or negative.
  2. **`save_catalog(supplier_catalog, filepath)`**, saves the catalog to a plain text file, one line per supplier and item, in whatever format you choose, as long as `load_catalog` can read it back correctly.
  3. **`load_catalog(filepath)`**, reads a catalog previously saved with `save_catalog` and returns it in the original nested dict shape.
- **`main.py`**, already complete, don't need to change it. It builds a sample catalog, runs a batch of order requests (some deliberately invalid), tracks totals, and runs `self_check()`.

The `supplier_catalog` shape is a dictionary of dictionaries:

```python
{
    "Accra Wholesale": {"Rice bag": 22.00, "Sugar": 11.00},
    "Tema Distributors": {"Cooking oil": 16.50, "Flour": 13.00},
}
```

A hint worth noticing: `supplier_catalog[supplier_name][item_name]` will naturally raise a `KeyError` on its own if either key is missing, you don't need to write a separate check for each one.

## Concepts You'll Need

Genuinely, most of the folder. Specifically:

- [`08-dictionaries-and-sets.md`](../../concepts/08-dictionaries-and-sets.md), nested dictionaries
- [`12-modules.md`](../../concepts/12-modules.md), why this is split into two files
- [`13-errors-and-exceptions.md`](../../concepts/13-errors-and-exceptions.md), raising and catching specific exceptions

## Self Check

```bash
python main.py
```

`main.py` runs a batch of order requests, prints what succeeded and what failed and why, then runs `self_check()`. You should see `All checks passed.` at the end with no errors.
