# What Is Data

*`00-foundations/03-files-and-data/concepts/01-what-is-data.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Fundamental**

## The Question

Why does a program need to think about data any differently from an ordinary variable?

---

## Everything in Memory Disappears

A variable like `price = 25.50` only exists while a program is running. The moment that process ends, the way `02-terminal/concepts/06-processes.md` covered, every variable it was holding disappears completely. Run the program again tomorrow, and it starts from nothing, with no memory of what happened yesterday.

**Data**, in the sense this folder means it, is information that needs to survive past the life of a single run. A shop's product catalog, a day's sales log, a customer's saved preferences, all of it has to exist tomorrow, when a brand new process starts with a clean slate.

```mermaid
flowchart LR
    A["Process running"] --> B["Variables in memory"]
    B --> C["Process ends"]
    C --> D["Variables gone"]
```

Compare that to information written to disk:

```mermaid
flowchart LR
    A["Process running"] --> B["Data written to a file"]
    B --> C["Process ends"]
    C --> D["File still exists"]
    D --> E["A new process reads it back"]
```

---

## This Is the Bridge

`01-programming` built the logic, how to compute a total, how to check stock, how to validate an order. This folder builds the other half: making the results of that logic durable, so they outlast the single run that produced them.

You already did this once, without necessarily naming it. `examples/shop-inventory-tracker/inventory.py`'s `save_catalog` and `load_catalog` functions exist for exactly one reason, so the shop's stock levels aren't reinvented from scratch every single time the program runs.

---

## Where This Shows Up

Every real application depends on this distinction constantly. A web app's database holds data that survives the server restarting. A text editor's autosave exists because in-memory edits vanish the instant the app crashes. The entire discipline of backend development, covered later in Unslop, is largely about managing data that has to outlive any one process, reliably, even when things go wrong.

---

## Try It

Run `shop-inventory-tracker/main.py` twice in a row. Notice `catalog.txt` exists after the first run, and gets read back in if you add a `load_catalog` call at the start. Now compare that to `daily_total`, a variable inside `main()`, it resets to zero every single time, nothing preserves it between runs.

---

## What You Need to Understand

- a running program's variables exist only in memory, and disappear when the process ends
- data, in the sense this folder covers, means information meant to outlive a single run
- writing to a file is what makes that survival possible

---

## Exercise

Look through one of your shop programs from `01-programming`. Write down every piece of information it currently only holds in memory, that would be lost the instant the program ends, and briefly note which of those might actually be worth saving to a file.

---

## Checkpoint

Explain, in your own words:

1. What happens to a Python variable the moment its process ends?
2. What makes something "data" in the sense this folder uses the word, rather than just a value?
3. Why did `shop-inventory-tracker` need `save_catalog` and `load_catalog` at all?
