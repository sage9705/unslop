# Pseudocode

*`00-foundations/01-programming/problem-solving/03-pseudocode.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Core Skill**

## The Question

How do you plan the logic of a solution before committing to actual Python syntax?

---

## What Pseudocode Is

Pseudocode is writing out the steps of a solution in plain, structured language, no real syntax rules, no exact keywords, just clear enough that anyone could follow the logic.

Take "Record a sale," one of the pieces decomposed in the previous doc:

```text
Ask for the item name
If the item is not in the catalog:
    Print "item not found" and stop
Ask for the quantity
If the quantity is more than what's in stock:
    Print "not enough stock" and stop
Reduce stock by the quantity
Add price times quantity to today's total
Print a confirmation message
```

Nothing here is valid Python. There's no colon-and-indentation requirement, no exact function names. That's the point.

---

## Why Bother

Writing this out in plain language surfaces logic problems immediately: what happens if the item isn't in stock? What if there isn't enough quantity? Both of those questions got answered above, in five seconds of thinking, before a single line of Python existed.

It's far cheaper to fix a mistake in five lines of plain English than in twenty lines of code you've already half debugged. Pseudocode separates two different kinds of thinking, "what should happen" and "how do I write this in Python", so you're never trying to do both at once.

---

## From Pseudocode to Python

The translation is usually direct once the logic is already sorted out.

```python
def record_sale(catalog, item_name, quantity, daily_total):
    if item_name not in catalog:
        print("Item not found.")
        return daily_total

    price, stock = catalog[item_name]

    if quantity > stock:
        print("Not enough stock.")
        return daily_total

    catalog[item_name] = (price, stock - quantity)
    daily_total += price * quantity
    print(f"Sale recorded: {item_name} x{quantity}")
    return daily_total
```

Every line of pseudocode maps to a recognizable chunk of the actual function. The hard thinking already happened before this step.

---

## Where This Shows Up

Real engineers sketch pseudocode-like plans constantly, in code review comments, design documents, and whiteboard discussions, before any implementation code exists. It's fast to write, fast to correct, and understandable by teammates regardless of which programming language they're most comfortable in. A design that's wrong in pseudocode takes a minute to fix. A design that's wrong after being fully implemented can take days.

---

## Practice

Write pseudocode, not Python, for checking whether a single product needs reordering: given a stock quantity and a threshold, decide whether to print a reorder message. This mirrors the logic from `concepts/04-conditionals.md`.

---

## What You Need to Understand

- what pseudocode is and what it deliberately leaves out
- why writing logic in plain language first catches mistakes earlier
- how pseudocode maps onto an actual Python implementation

---

## Exercise

Write full pseudocode for the Stock Reorder Alert tool: loop through a list of products and their quantities, print a reorder message for anything at or below a threshold, and count how many products need reordering in total.

Then translate your pseudocode into actual Python and compare the two side by side.

> Do this one yourself, no AI. That's the Golden Rule, see the [section README](../README.md#the-golden-rule-zero-ai-code-generation).

---

## Checkpoint

Explain, in your own words:

1. What makes pseudocode different from actual code?
2. Why is it cheaper to catch a logic mistake in pseudocode than in working Python?
3. What two kinds of thinking does pseudocode help you separate?
4. Why would a team write pseudocode in a design document instead of just writing the real code directly?
