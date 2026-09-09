# Expressions and Operators

*`00-foundations/01-programming/concepts/03-expressions-and-operators.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Fundamental**

## Learn the Syntax

This doc explains why operators and precedence matter, not the full list of symbols Python supports. For that side:

- **[W3Schools: Python Operators](https://www.w3schools.com/python/python_operators.asp)**, every operator with a runnable example, good for a first pass
- **[Real Python: Operators and Expressions in Python](https://realpython.com/python-operators-expressions/)**, a deeper walkthrough covering precedence and edge cases
- **[Official docs: Expressions](https://docs.python.org/3/reference/expressions.html)**, the authoritative reference, including the full precedence table

## The Question

How does a program compute new values from existing ones?

---

## Expressions

An **expression** is anything that evaluates to a value.

```python
price * quantity        # evaluates to a total
subtotal - discount     # evaluates to a discounted total
stock_quantity >= 5     # evaluates to True or False
```

A variable assignment isn't itself an expression, but the right hand side is:

```python
total = price * quantity   # price * quantity is the expression, total = ... is the assignment
```

---

## Arithmetic Operators

| Operator | Meaning            | Example    | Result  |
| -------- | ------------------ | ---------- | ------- |
| `+`    | addition           | `5 + 2`  | `7`   |
| `-`    | subtraction        | `5 - 2`  | `3`   |
| `*`    | multiplication     | `5 * 2`  | `10`  |
| `/`    | division           | `5 / 2`  | `2.5` |
| `//`   | floor division     | `5 // 2` | `2`   |
| `%`    | remainder (modulo) | `5 % 2`  | `1`   |
| `**`   | exponent           | `5 ** 2` | `25`  |

---

## Comparison Operators

Comparisons always evaluate to `True` or `False`.

| Operator | Meaning               | Example    | Result    |
| -------- | --------------------- | ---------- | --------- |
| `==`   | equal to              | `5 == 5` | `True`  |
| `!=`   | not equal to          | `5 != 3` | `True`  |
| `<`    | less than             | `3 < 5`  | `True`  |
| `>`    | greater than          | `3 > 5`  | `False` |
| `<=`   | less than or equal    | `5 <= 5` | `True`  |
| `>=`   | greater than or equal | `5 >= 6` | `False` |

---

## Logical Operators

Logical operators combine `True`/`False` values.

| Operator | Meaning                   | Example            | Result    |
| -------- | ------------------------- | ------------------ | --------- |
| `and`  | both must be true         | `True and False` | `False` |
| `or`   | at least one must be true | `True or False`  | `True`  |
| `not`  | flips the value           | `not True`       | `False` |

```python
stock_available = True
payment_confirmed = True

can_ship_order = stock_available and payment_confirmed   # True
```

---

## Operator Precedence

Python evaluates expressions in a set order, not strictly left to right. `*` and `/` happen before `+` and `-`, the same rule you learned in school math.

```python
total = price + price * 0.15
```

| Step | What Happens                                        | Value So Far |
| ---- | --------------------------------------------------- | ------------ |
| 1    | `price * 0.15` is evaluated first, the tax amount | tax amount   |
| 2    | `price + tax` is evaluated next                   | final total  |

If you want a different order, use parentheses:

```python
total = (price + price) * 0.15   # a very different number
```

When in doubt, add parentheses. In real financial code, precedence mistakes are exactly how a business ends up overcharging or undercharging a customer without anyone noticing for weeks.

---

## Where This Shows Up

Every checkout, every invoice, every payroll run is built from exactly these operators, stacked in a specific order: subtotal, then discount, then tax, then total. Get that order wrong and the amount a real customer pays is wrong. Unless someone double checks the math by hand, nobody notices until a customer complains or the books don't balance at the end of the month.

---

## Try It

```python
unit_price = 15.00
quantity = 3
tax_rate = 0.125

subtotal = unit_price * quantity
total = subtotal + subtotal * tax_rate

print(subtotal)
print(total)
```

Predict each line's output before running it.

---

## What You Need to Understand

- expressions versus statements
- arithmetic, comparison, and logical operators
- how operator precedence affects evaluation order
- using parentheses to control order


## Exercise

A customer buys three different items at a shop. Write a program that:

1. Calculates the subtotal for all three items.
2. Applies a 5% discount if the subtotal is over 100.
3. Adds a 12.5% tax on top of the discounted total.
4. Prints the final amount the customer owes.

Then calculate the change due if the customer pays with a specific amount of cash.

> Write this one yourself, no AI. That's the Golden Rule, see the [section README](../README.md#the-golden-rule-zero-ai-code-generation).

---

## Checkpoint

Explain, in your own words:

1. What is the difference between `/` and `//`?
2. Why does tax get calculated before it's added to the price, rather than after?
3. What does `and` require that `or` doesn't?
4. Why do parentheses matter more in code that touches money than almost anywhere else?
