# Catalog Value Reader

*`00-foundations/03-files-and-data/examples/01-read-text-file/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What It Does

Reads the shop's `catalog.txt`, the same format `shop-inventory-tracker` saves, and reports the total value of everything currently in stock, price times quantity, summed across every product.

## Concepts It Demonstrates

- [`02-files-and-directories.md`](../../concepts/02-files-and-directories.md), a file as something a program opens and reads, not just navigates to
- [`03-text-and-binary-data.md`](../../concepts/03-text-and-binary-data.md), `catalog.txt` read in text mode
- [`04-reading-files.md`](../../concepts/04-reading-files.md), `with open(...)` and reading line by line

## How to Run

```bash
python main.py
```

## Sample Output

```
========================================
CATALOG VALUE REPORT
========================================
Rice bag          40 x  25.50 =  1020.00
Sugar             30 x  12.75 =   382.50
Cooking oil       15 x  18.00 =   270.00
Flour             22 x  15.00 =   330.00
Bread             12 x   8.50 =   102.00
----------------------------------------
TOTAL STOCK VALUE               2104.50
========================================
```

## Try Changing

- Add a sixth line to `catalog.txt` and confirm it shows up in the report.
- Change `read_catalog` to also return the highest-value single product, the one where `price * quantity` is largest.
- Break `catalog.txt` on purpose, remove one of the three comma-separated values from a line, and see exactly what error that produces.
