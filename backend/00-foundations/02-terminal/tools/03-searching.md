# Searching

*`00-foundations/02-terminal/tools/03-searching.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Reference**

Finding text inside files, and finding files by name, both without opening a single one by hand.

---

## The Commands

| Command | What It Does | Example |
|---|---|---|
| `grep "<text>" <file>` | Searches inside a file for lines containing that text | `grep "discount" main.py` |
| `grep -r "<text>" <directory>` | Searches every file inside a directory, and its subdirectories, for that text | `grep -r "NotImplementedError" exercises` |
| `grep -n "<text>" <file>` | Same as `grep`, but also shows the line number of every match | `grep -n "TODO" main.py` |
| `grep -i "<text>" <file>` | Searches without caring about uppercase or lowercase | `grep -i "sugar" main.py` |
| `find <directory> -name "<pattern>"` | Searches for files or directories by name, throughout a whole directory tree | `find . -name "*.py"` |

---

## Walking Through It

Checking exactly how much of the exercises folder is still unfinished:

```bash
$ grep -rn "NotImplementedError" exercises
exercises/01-values-and-variables/starter.py:17:    raise NotImplementedError("TODO: implement parse_cost")
exercises/01-values-and-variables/starter.py:25:    raise NotImplementedError("TODO: implement parse_quantity")
exercises/03-functions/starter.py:15:    raise NotImplementedError("TODO: implement calculate_loyalty_discount_rate")
```

Every remaining function still needing an implementation, across every exercise, in one command.

Finding every Python file inside `examples/`:

```bash
$ find examples -name "*.py"
examples/till-calculator/main.py
examples/stock-reorder-alert/main.py
examples/customer-feedback-analyzer/main.py
examples/shop-inventory-tracker/inventory.py
examples/shop-inventory-tracker/sales.py
examples/shop-inventory-tracker/receipts.py
examples/shop-inventory-tracker/main.py
```

---

## Common Mistakes

- Search text with a space in it needs quotes around it, `grep discount rate main.py` is read as two separate arguments, `grep "discount rate" main.py` is read as one.
- Forgetting `-r` on `grep` searches only the one file you named, even when the real answer is spread across several.
- The `*` in `find -name "*.py"` is a wildcard meant for `find` itself to interpret. Leaving off the quotes around it can let the shell expand it first, before `find` ever sees it, producing confusing results.

---

## What You Need to Understand

- `grep` searches inside files for matching text
- `find` searches for files or directories by name
- both work recursively through an entire folder tree with the right flag

---

## Exercise

Use `grep -rn` to find every place the word `"discount"` appears anywhere inside `01-programming/`. Then use `find` to list every `README.md` file in the whole folder, at any depth.

---

## Checkpoint

1. What's the difference between what `grep` searches for and what `find` searches for?
2. What does the `-n` flag add to a `grep` search?
3. Why does search text containing a space need quotes around it?
