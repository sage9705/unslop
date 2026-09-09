# Types

*`00-foundations/01-programming/concepts/02-types.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Fundamental**

## The Question

How does Python know what kind of value it's working with?

---

## Why Types Matter

Every value has a **type**. It tells Python, and you, what the value represents and what you can do with it.

```python
3            # a whole number of units
25.50        # a price with cents
"Rice bag"   # text
True         # a yes or no value
```

You can't do everything with every type. Adding two prices makes sense. Adding a price to a product name doesn't, and Python will stop you before it lets you make that mistake silently.

---

## Where This Shows Up

Every field in a real database, every response from a real API, has a declared type for exactly this reason. A shop's inventory system stores quantity as a whole number and price as a decimal on purpose, so a careless line of code can't quietly turn `3` units into the text `"3"` and break every calculation that depends on it.

---

## The Common Types

| Type         | Example              | Description                                         |
| ------------ | -------------------- | --------------------------------------------------- |
| `int`      | `3`                | A whole number, like a quantity of units            |
| `float`    | `25.50`            | A number with a decimal point, like a price         |
| `str`      | `"Rice bag"`       | Text, wrapped in quotes                             |
| `bool`     | `True` / `False` | A yes or no value, like whether an item is in stock |
| `NoneType` | `None`             | The absence of a value                              |

You'll meet more complex types, lists and dictionaries, etc. For now, focus on these five.

---

## Checking a Type

Python can tell you the type of anything with `type()`:

```python
type(3)          # <class 'int'>
type(25.50)      # <class 'float'>
type("Rice bag") # <class 'str'>
type(True)       # <class 'bool'>
```

When you're not sure what you're working with, ask.

---

## Type Conversion

You can often convert a value from one type to another:

```python
str(25.50)     # "25.50"
int("3")       # 3
float("25.5")  # 25.5
```

But not every conversion is safe:

```python
int("out of stock")   # raises an error, that text isn't a number
```

Python won't guess what you mean. If a conversion doesn't make sense, it fails rather than doing the wrong thing.

---

## A Real Bug This Causes

```python
"5" + 5
```

This raises an error. `"5"` is text, `5` is a number, and Python won't combine them. You have to be explicit:

```python
int("5") + 5     # 10
"5" + str(5)     # "55"
```

This isn't a made up beginner puzzle. It's one of the most common real bugs in retail and invoicing software. A price arrives from a spreadsheet, a form, or an API as text, `"25.50"` instead of `25.50`. If a developer forgets to convert it before adding it to a running total, the program either crashes or, worse, quietly produces a wrong number that ends up on a real invoice.

---

## Try It

```python
price_text = "10"
print(type(price_text))

price = float(price_text)
print(type(price))
print(price * 3)
```

Predict each `print()` output before running it.

---

## What You Need to Understand

- the common built in types (`int`, `float`, `str`, `bool`, `None`)
- checking a type with `type()`
- converting between types
- why mixing incompatible types causes errors

## Exercise

A customer's order comes in from an online form, which means every field arrives as text. Write a program that:

1. Stores a unit price as text, `"15.75"`, exactly as it would arrive from a form.
2. Converts it to a float.
3. Stores a quantity as text, `"4"`, and converts it to an int.
4. Calculates and prints the total cost, along with its type.

Then try breaking it on purpose. Store the price as `"fifteen seventy five"` instead and see what error you get. That's the exact kind of bad input a real system has to handle.

> Write this one yourself, no AI. That's the Golden Rule, see the [section README](../README.md#the-golden-rule-zero-ai-code-generation).

---

## Checkpoint

Explain, in your own words:

1. What is a type?
2. Why does `"5" + 5` fail?
3. How do you check the type of a value?
4. When would a type conversion fail?
5. Why would a real order form send every value as text, and why does that matter for a program reading it?
