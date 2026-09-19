# Data Errors

*`00-foundations/01-programming/debugging/03-data-errors/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What a Data Error Is

The code is often perfectly correct in isolation. The bug shows up because the actual data doesn't match what the code assumed about it; a different capitalization than expected, a number that arrived as text. Sometimes this produces a wrong answer, like a logic error. Sometimes it crashes the program outright. Both are data errors, the root cause is the same: a mismatch between what the code expects and what the data actually is.

---

## `broken_price_lookup.py`

**Symptom:** Looking up a product's price works fine most of the time, but every so often it returns `0` for a product that's definitely in the catalog, and the shop owner can't figure out why it's inconsistent.

Run it:

```bash
python broken_price_lookup.py
```

<details>
<summary>Hint, if you're genuinely stuck</summary>

Look closely at the exact spelling and capitalization of the catalog's keys versus the names being looked up. Dictionary keys are matched exactly, `"Rice bag"` and `"rice bag"` are two completely different keys as far as Python is concerned.

</details>

---

## `broken_total_calculation.py`

**Symptom:** This one doesn't quietly give a wrong answer, it crashes. A function meant to add up a list of quantities fails the moment it's given data straight from a form.

Run it:

```bash
python broken_total_calculation.py
```

<details>
<summary>Hint, if you're genuinely stuck</summary>

Read the error message all the way through, it tells you the exact two types Python couldn't combine. What type is each quantity actually stored as, and what type does `+` expect for addition?

</details>
