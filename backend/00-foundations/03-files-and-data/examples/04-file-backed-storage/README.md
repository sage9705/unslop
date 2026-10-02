# Validated Catalog Store

*`00-foundations/03-files-and-data/examples/04-file-backed-storage/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What It Does

A small catalog store that remembers its contents between runs. It loads whatever was saved last time, tries to add a batch of new products, rejects any that fail validation with a clear reason, and saves only what passed. Run it twice in a row, and the second run picks up exactly where the first left off.

## Why It's Split Into Two Files

`catalog_store.py` holds the reusable logic: loading, saving, validating, and adding products. `main.py` is a short script that uses it. This is the same split `shop-inventory-tracker` used back in `01-programming`, and the same idea covered in [`01-programming/concepts/12-modules.md`](../../../01-programming/concepts/12-modules.md).

## Concepts It Demonstrates

- [`10-parsing.md`](../../concepts/10-parsing.md), reading structured data back from a JSON file
- [`11-data-validation.md`](../../concepts/11-data-validation.md), rejecting a negative price, an empty name, and a negative quantity before any of them reach the file
- [`12-persistence.md`](../../concepts/12-persistence.md), the catalog survives between runs

## How to Run

```bash
python main.py
```

Run it a second time without changing anything.

## Sample Output

First run:

```
Loaded 0 existing product(s) from catalog_store.json
Added: Rice bag
Added: Sugar
Rejected: Could not add 'Cooking oil': price must be a positive number
Rejected: Could not add '': name must be a non-empty string
Rejected: Could not add 'Flour': quantity must be a non-negative integer
Added: Bread

Saved 3 product(s) to catalog_store.json
```

Second run:

```
Loaded 3 existing product(s) from catalog_store.json
Added: Rice bag
Added: Sugar
Rejected: Could not add 'Cooking oil': price must be a positive number
Rejected: Could not add '': name must be a non-empty string
Rejected: Could not add 'Flour': quantity must be a non-negative integer
Added: Bread

Saved 3 product(s) to catalog_store.json
```

The second run opens with `Loaded 3 existing product(s)`, where the first opened with `0`. Nothing was typed in between, the data survived because it was written to disk, which is the whole point of persistence.

Three of the six attempted products were rejected, and none of them ever reached `catalog_store.json`. Validation stopped them at the door.

## Try Changing

- Delete `catalog_store.json` and rerun, watch the store start empty again.
- Add a rule to `validate_product` rejecting any price above 1000, and add a product that trips it.
- Change one product's quantity to the string `"forty"` and see which validation check catches it.
- Open `catalog_store.json` in a text editor after a run, and compare how easy it is to read next to the old `catalog.txt` format.
