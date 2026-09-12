# Shop Inventory and Sales Tracker

*`00-foundations/01-programming/examples/shop-inventory-tracker/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What It Does

The capstone example for this folder. It runs a small shop for a day: builds a starting catalog, processes a batch of orders against it, handles the ones that fail (not enough stock, an item that doesn't exist) without crashing, prints an end of day summary, and saves the updated catalog to a file so it isn't lost when the program ends.

## Why It's Split Into Multiple Files

Unlike the other three examples, this one is deliberately split across `inventory.py`, `sales.py`, `receipts.py`, and `main.py`, the exact structure described in [`12-modules.md`](../../concepts/12-modules.md). Each file owns one responsibility:

- `inventory.py`, adding stock, reducing stock, looking up prices, saving and loading the catalog
- `sales.py`, recording a sale, including handling failures gracefully
- `receipts.py`, formatting receipt lines and the end of day summary
- `main.py`, ties the three together and runs the day

## Concepts It Demonstrates

- [`07-collections.md`](../../concepts/07-collections.md) and [`08-dictionaries-and-sets.md`](../../concepts/08-dictionaries-and-sets.md), the catalog and the sales log
- [`11-mutation-and-references.md`](../../concepts/11-mutation-and-references.md), the catalog dictionary is passed into and modified by functions across three different files
- [`12-modules.md`](../../concepts/12-modules.md), the whole reason this example is more than one file
- [`13-errors-and-exceptions.md`](../../concepts/13-errors-and-exceptions.md), a sale for more stock than exists, or for an item that isn't in the catalog, fails with a clear message instead of crashing the program
- A small addition not covered in `concepts/`: `save_catalog` and `load_catalog` use Python's built in `open()` to read and write a plain text file. This is basic file handling, included here because a real inventory system has to remember its data between runs. A more formal treatment of file handling comes later in the curriculum.

## How to Run

```bash
python main.py
```

## Sample Output

```
Sale recorded: Rice bag x2 = 51.00
Sale recorded: Sugar x3 = 38.25
Sale recorded: Cooking oil x1 = 18.00
Sale failed: Not enough stock for 'Sugar': 27 available, 50 requested.
Sale failed: 'Flour' is not in the catalog.

========================================
END OF DAY SUMMARY
========================================
Rice bag          2 x  25.50 =   51.00
Sugar             3 x  12.75 =   38.25
Cooking oil       1 x  18.00 =   18.00
----------------------------------------
DAILY TOTAL                      107.25
========================================

Remaining stock:
  Rice bag: 38
  Sugar: 27
  Cooking oil: 14

Catalog saved to catalog.txt
```

Two of the five sample orders are deliberately built to fail, one asks for more sugar than is in stock, one asks for a product that was never added to the catalog. Both are handled without stopping the program, which is the entire point of this example.

Running it creates a `catalog.txt` file in the same folder, containing the saved end of day catalog. Delete it and rerun the program at any time, it will be recreated from scratch.

## Try Changing

- Add a sixth order for a product and quantity that should succeed, and confirm it shows up in both the summary and the remaining stock.
- Add a new product with `inventory.add_stock` before the orders run, and sell some of it.
- Call `inventory.load_catalog("catalog.txt")` at the start of `main()` instead of building the catalog from scratch, and confirm it picks up where the last run left off.
