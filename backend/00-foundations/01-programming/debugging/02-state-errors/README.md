# State Errors

*`00-foundations/01-programming/debugging/02-state-errors/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What a State Error Is

Every individual line of code might look reasonable on its own. The bug is in the timeline, when a variable gets created, when it gets reset, and whether two variables unknowingly refer to the same thing. These are usually harder to spot than logic errors because you can stare at any single line and it looks completely correct.

---

## `broken_running_total.py`

**Symptom:** A function meant to add up a week's sales into one running total is returning a number that looks suspiciously like just one day's sales, not the whole week's.

Run it:

```bash
python broken_running_total.py
```

<details>
<summary>Hint, if you're genuinely stuck</summary>

Trace this one by hand, the way `problem-solving/04-tracing-programs.md` describes, one row per pass through the loop. Watch exactly what value `total` holds at the start of each pass. Where is it being set, and how often?

</details>

---

## `broken_shared_specials_list.py`

**Symptom:** Building a "today's specials" list from the shop's main inventory list is somehow also changing the main inventory itself, items are appearing in stock that were never actually delivered.

Run it:

```bash
python broken_shared_specials_list.py
```

<details>
<summary>Hint, if you're genuinely stuck</summary>

This is the exact bug covered in `concepts/11-mutation-and-references.md`. Ask yourself: when `specials` is created from `main_inventory`, does that line create a new, independent list, or does it just give a second name to the same one?

</details>
