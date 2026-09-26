# Structured Data

*`00-foundations/03-files-and-data/concepts/07-structured-data.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Fundamental**

## The Question

How do you represent something more complex than a single value in a file?

---

## More Than a Single Line

A product is several pieces of information bundled together as one unit, a name, a price, a quantity. A whole catalog is many of those bundles, collected. Inside a running program, this is nothing new, `01-programming/concepts/08-dictionaries-and-sets.md` already covered exactly this shape:

```python
catalog = {
    "Rice bag": {"price": 25.50, "quantity": 40},
    "Sugar": {"price": 12.75, "quantity": 30},
}
```

The question this doc asks is different: how do you represent that same shape once it leaves memory and becomes text in a file?

---

## The Trouble With `catalog.txt`'s Approach

```text
Rice bag,25.50,40
Sugar,12.75,30
```

This works, and it's exactly what `save_catalog` and `load_catalog` use. It's also fragile in ways worth noticing now. A product name containing a comma, "Rice, 5kg bag", would silently break the `.split(",")` logic that reads it back. Adding a new field later, a category, a supplier, means rewriting the format and every line that already exists. There's no built in way to tell the difference between "this line is malformed" and "this line is just unusual."

```mermaid
flowchart LR
    A["Python dict in memory"] --> B["Hand-rolled text format"]
    B --> C["Fragile to edge cases"]
```

---

## A Better Path Exists

Formats built specifically to represent structured, nested data reliably already exist, well tested, widely supported, and far less fragile than a hand-rolled comma split. The most common one in modern software is covered next.

```mermaid
flowchart LR
    A["Python dict in memory"] --> B["A standard structured format"]
    B --> C["Reliable, extensible, widely supported"]
```

---

## Where This Shows Up

Every real API, every modern config file, every data export from a serious piece of software uses a structured format for exactly these reasons. Reliability and extensibility outweigh plain text's simplicity the moment data grows past a single flat line per record, which happens faster than it seems like it will.

---

## Try It

Look at `catalog.txt` from `shop-inventory-tracker`, if you still have one lying around, or imagine one. Picture adding a `"category"` field to every product. Notice how much would need to change, the format, the write logic, the read logic, every existing line, just to add one new fact about each product.

---

## What You Need to Understand

- structured data means information organized as named, related pieces, not just a single flat value
- a hand-rolled text format for structured data is fragile around edge cases and hard to extend
- standard structured formats exist specifically to solve this reliably

---

## Exercise

Write down, in plain language, three problems that could occur with `catalog.txt`'s comma-separated format if the shop's data got messier, more products, more fields, less careful input. Don't fix them yet, just name them clearly.

---

## Checkpoint

Explain, in your own words:

1. What makes data "structured" rather than just a single value?
2. What's one concrete way `catalog.txt`'s format could break on real, messy data?
3. Why does adding a new field to a comma-separated format require touching every existing line?
