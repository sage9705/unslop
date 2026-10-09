# Debugging: Invalid JSON

*`00-foundations/03-files-and-data/debugging/03-invalid-json/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Report

"I opened the catalog file in a text editor to fix a price. I saved it, and now the program won't start. I only touched one number."

## Reproduce It

```bash
python load_catalog.py
```

## Investigate

This time the Python code is fine, and `load_catalog.py` should stay exactly as it is. The problem lives in `shop_catalog.json`, a file edited by hand.

Python's error message is precise. It names what it expected, and the exact line and column where it gave up. Open `shop_catalog.json` and go to that exact spot.

There may be more than one mistake. A JSON parser stops at the first problem it finds, so fixing one and running again will show you the next.

## Fix It

Correct `shop_catalog.json` until `load_catalog.py` passes. The catalog's contents must stay the same, only the formatting needs repairing. Revisit [`concepts/08-json.md`](../../concepts/08-json.md) if you need the rules of the format.

<details>
<summary>Hint, if you're genuinely stuck</summary>

Fix only what the error message points at, then run it again. Resist rewriting the whole file, the point of this exercise is learning to read the message, and the next message comes from the next problem.
</details>
