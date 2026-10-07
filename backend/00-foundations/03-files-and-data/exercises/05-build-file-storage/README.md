# Exercise: Build File Storage

*`00-foundations/03-files-and-data/exercises/05-build-file-storage/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

The shop wants a loyalty scheme. Customers are identified by their phone number, and earn points on purchases. The records have to survive between runs, and bad data must never reach the file, a mistyped phone number or a negative number of points would quietly corrupt the whole scheme.

You're building the storage layer. Another part of the shop's software will call it, so it needs to fail loudly and clearly when it's handed something wrong.

## What You Need to Build

Two files, split the way [`concepts/12-modules.md`](../../../01-programming/concepts/12-modules.md) describes:

- **`storage.py`**, which you implement:
  1. **`load_store(filepath)`**, returns the store from a JSON file. A missing file gives back an empty dict. A file containing invalid JSON raises `ValueError`.
  2. **`save_store(store, filepath)`**, writes the store as JSON.
  3. **`register_customer(store, phone, name)`**, adds a customer with 0 points. Raises `ValueError` for a phone number that isn't exactly 10 digits, a blank name, or a phone number that's already registered.
  4. **`add_points(store, phone, points)`**, adds points and returns the new total. Raises `KeyError` for an unregistered phone number, and `ValueError` unless `points` is a positive whole number.
- **`main.py`**, already complete. It runs a demo against `loyalty_store.json`, then runs `self_check()`.

A store looks like this:

```python
{"0551234567": {"name": "Ama", "points": 20}}
```

## Concepts You'll Need

- [`09-serialization-and-deserialization.md`](../../concepts/09-serialization-and-deserialization.md)
- [`11-data-validation.md`](../../concepts/11-data-validation.md)
- [`12-persistence.md`](../../concepts/12-persistence.md)
- [`13-errors-and-exceptions.md`](../../../01-programming/concepts/13-errors-and-exceptions.md), from `01-programming`

## Self Check

```bash
python main.py
```

Run it twice. The second run should begin by loading the customers the first one saved. The final line should be `All checks passed.`

Delete `loyalty_store.json` when you're done.
