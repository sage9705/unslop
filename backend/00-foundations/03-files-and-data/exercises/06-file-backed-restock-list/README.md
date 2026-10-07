# Exercise: File Backed Restock List

*`00-foundations/03-files-and-data/exercises/06-file-backed-restock-list/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

When stock runs low, someone has to order more, wait for it to arrive, and cross it off. Right now that lives on a sticky note. The shop wants a restock list that remembers each item's progress, and survives the computer being switched off overnight.

Each item moves through three stages, in order: `pending`, then `ordered`, then `received`. An item cannot jump from `pending` straight to `received`, because that would mean stock arrived that nobody ordered, which usually means a mistake somewhere.

This pulls together most of what this folder covers: validation on the way in, a rule about which changes are allowed, a save to disk, and a reload that picks up exactly where things were left.

## What You Need to Build

In `starter.py`, implement six functions:

1. **`load_list(filepath)`**, returns the saved list, or an empty list if the file doesn't exist yet.
2. **`save_list(items, filepath)`**, writes the list as JSON.
3. **`add_item(items, name, quantity)`**, adds a `pending` item with the next unused id, and returns it. Raises `ValueError` for a blank name, or a quantity that isn't a positive whole number.
4. **`update_status(items, item_id, new_status)`**, moves an item exactly one step forward. Raises `KeyError` for an unknown id, and `ValueError` for an unknown status or a skipped step.
5. **`pending_items(items)`**, returns every item still `pending`.
6. **`remove_received(items)`**, returns a new list without the received items, and leaves the original list alone.

An item looks like this:

```python
{"id": 1, "name": "Sugar", "quantity": 30, "status": "pending"}
```

## Concepts You'll Need

- [`09-serialization-and-deserialization.md`](../../concepts/09-serialization-and-deserialization.md)
- [`11-data-validation.md`](../../concepts/11-data-validation.md)
- [`12-persistence.md`](../../concepts/12-persistence.md)
- [`13-errors-and-exceptions.md`](../../../01-programming/concepts/13-errors-and-exceptions.md), from `01-programming`

## Self Check

```bash
python starter.py
```

`self_check()` works in a temporary folder and leaves nothing behind. It checks every rule above, including that ids keep counting upward after the list is saved and reloaded. You should see `All checks passed.`
