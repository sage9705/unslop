# Complexity Basics

*`00-foundations/01-programming/problem-solving/05-complexity-basics.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Core Skill**

## The Question

Why does some code slow down badly as the amount of data grows, and how do you start noticing that before it becomes a real problem?

This doc is a first exposure, not a full treatment. A proper look at Big O notation and algorithm analysis comes later in the curriculum. For now, the goal is just to start noticing when the amount of work a program does depends heavily on how much data it's handling.

---

## A Lookup That Works Fine, at First

With a small catalog, scanning through it to find a price is instant.

```python
def find_price(products, name):
    for product_name, price in products:
        if product_name == name:
            return price
    return None

products = [("Rice bag", 25.50), ("Sugar", 12.75), ("Cooking oil", 18.00)]
find_price(products, "Sugar")
```

With three products, this loop checks at most three entries. Nobody would notice a delay.

## The Same Code, at a Different Scale

Now imagine that shop grows into a chain with fifty thousand products across every branch. That same function, unchanged, now has to check, on average, tens of thousands of entries for a single lookup. Every checkout. Every single time someone scans an item.

The code isn't broken. It produces the correct price every time. It's just built in a way where the amount of work grows right alongside the amount of data, which is exactly the kind of thing that works fine in testing with ten sample products and quietly becomes a real bottleneck once the business actually grows.

---

## Why the Dictionary Mattered

This is precisely why `concepts/08-dictionaries-and-sets.md` reached for a dictionary instead of a list for the catalog.

```python
catalog = {"Rice bag": 25.50, "Sugar": 12.75, "Cooking oil": 18.00}
catalog["Sugar"]   # fast, and stays fast no matter how big the catalog gets
```

A dictionary lookup doesn't need to scan every entry to find a match. It goes almost directly to the answer, whether the catalog has three products or three hundred thousand. Choosing a dictionary over a list wasn't a style preference back in that lesson, it was a decision about how the code would behave as the business it supports actually grows.

---

## Another Example: Checking for Duplicates

Comparing every product against every other product to find duplicate codes is a common instinct, and a common trap.

```python
def has_duplicate(codes):
    for i in range(len(codes)):
        for j in range(len(codes)):
            if i != j and codes[i] == codes[j]:
                return True
    return False
```

This nested loop means the amount of work grows much faster than the amount of data, doubling the number of products roughly quadruples the number of comparisons. A set based approach avoids this entirely:

```python
def has_duplicate(codes):
    seen = set()
    for code in codes:
        if code in seen:
            return True
        seen.add(code)
    return False
```

This version checks each code once, using the same fast, near instant membership check a dictionary uses for keys.

---

## Where This Shows Up

A shop's search feature that works instantly with fifty products but grinds to a crawl with fifty thousand isn't a bug in the traditional sense, the code still gives the right answer. It's just structured in a way that doesn't scale, and that gap between "works in a demo" and "survives a growing, real business" is one of the most common and expensive lessons in software engineering. It's also exactly why the data structure choices back in `concepts/07-collections.md` and `concepts/08-dictionaries-and-sets.md` weren't just about syntax preference.

---

## Practice

Without necessarily writing code, think through this: a shop wants to check whether a customer's phone number has already been served today, to avoid counting them twice in a "unique customers" report. Would you check this against a list, scanning each entry, or against a set? Explain why, using what you now know about how each one behaves as the number of customers grows.

---

## What You Need to Understand

- that the same correct code can behave very differently depending on how much data it processes
- why scanning through a list gets slower as the list grows
- why a dictionary or set lookup stays fast regardless of size
- that this is a first exposure to a topic you'll study more formally later

---

## Exercise

Write two versions of a function that finds a product's price:

1. One that scans a list of `(name, price)` tuples.
2. One that looks the price up in a dictionary.

Confirm both return the correct price for a small test catalog. Then explain, in your own words, why the dictionary version stays fast as the catalog grows from ten products to ten thousand, while the list version doesn't.

> Do this one yourself, no AI. That's the Golden Rule, see the [section README](../README.md#the-golden-rule-zero-ai-code-generation).

---

## Checkpoint

Explain, in your own words:

1. Why can code be completely correct and still become a real problem as data grows?
2. Why does a dictionary lookup stay fast regardless of how many entries it has?
3. What happens to the number of comparisons in a nested loop as the input doubles?
4. Why does the choice between a list and a dictionary matter more for a growing business than a small one?
