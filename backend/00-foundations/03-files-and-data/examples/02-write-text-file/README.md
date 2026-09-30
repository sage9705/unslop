# Daily Sales Logger

*`00-foundations/03-files-and-data/examples/02-write-text-file/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What It Does

Logs each sale to `sales_log.txt` as it happens. Demonstrates the exact difference between starting a fresh log with `"w"` mode and adding to an existing one with `"a"` mode, side by side, in one run.

## Concepts It Demonstrates

- [`05-writing-files.md`](../../concepts/05-writing-files.md), `"w"` erases, `"a"` adds

## How to Run

```bash
python main.py
```

## Sample Output

```
==============================
SALES LOG
==============================
item_name,amount
Rice bag,51.00
Sugar,38.25
Cooking oil,18.00
==============================

Logging one more sale, without starting a new log...
==============================
SALES LOG
==============================
item_name,amount
Rice bag,51.00
Sugar,38.25
Cooking oil,18.00
Flour,15.00
==============================
```

Notice the second printout has four lines instead of three. `log_sale` used `"a"` mode, so the Flour sale was added onto the existing log rather than replacing it.

## Try Changing

- Call `start_new_log` a second time, right before logging Flour, and compare the output, you'll see exactly what `"w"` mode does to a log that already had sales in it.
- Add a `total_sales(filepath)` function that reads `sales_log.txt` back and sums every `amount` column.
