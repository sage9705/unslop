# Logic Errors

*`00-foundations/01-programming/debugging/01-logic-errors/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What a Logic Error Is

The program runs from top to bottom without a single crash, and produces an answer. The answer is just wrong. Nothing in the output looks obviously broken, which is exactly what makes this category dangerous, a logic error can sit in production code for months if not spotted early(happens without thorough testing) before anyone notices the numbers don't quite add up.

---

## `broken_stock_status.py`

**Symptom:** A shop owner says items with exactly `5` units left are being marked "Well Stocked" instead of "Reorder Now", meaning stock is running out with no warning.

Run it:

```bash
python broken_stock_status.py
```

<details>
<summary>Hint, if you're genuinely stuck</summary>

Pay close attention to the exact boundary value in the comparison. Is `5` included in the range the code thinks needs reordering, or excluded from it?

</details>

---

## `broken_discount_priority.py`

**Symptom:** A shop's loyalty program is supposed to give customers whichever discount benefits them more, loyalty or bulk. Customers are complaining they're getting smaller discounts than the shop advertises.

Run it:

```bash
python broken_discount_priority.py
```

<details>
<summary>Hint, if you're genuinely stuck</summary>

The function is supposed to pick the larger of two discount rates. Which built in function is being used to compare them, and does it pick the larger one or the smaller one?

</details>
