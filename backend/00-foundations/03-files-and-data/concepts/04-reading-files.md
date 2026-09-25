# Reading Files

*`00-foundations/03-files-and-data/concepts/04-reading-files.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Fundamental**

## The Question

How does a program actually pull a file's content into memory to work with it?

---

## Opening a File Safely

```python
with open("catalog.txt", "r") as file:
    content = file.read()
```

`open()` establishes a connection between your program and the file on disk. The `with` statement guarantees that connection gets closed properly once you're done with it, even if something goes wrong partway through. Without `with`, a crash halfway through reading could leave the file open, holding onto a resource your program never properly released.

This is the exact pattern `inventory.py`'s `load_catalog` already used:

```python
def load_catalog(filepath):
    catalog = {}
    with open(filepath, "r") as file:
        for line in file:
            item_name, price, quantity = line.strip().split(",")
            catalog[item_name] = {"price": float(price), "quantity": int(quantity)}
    return catalog
```

---

## Three Ways to Read

| Method | What It Gives You | When to Use It |
|---|---|---|
| `file.read()` | The entire file as one string | Small files, or when you need the whole thing at once |
| `for line in file:` | One line at a time, as you loop | Large files, or when processing line by line matters |
| `file.readlines()` | Every line as a list of strings | When you need all lines, but as a list you can index into |

```python
with open("catalog.txt", "r") as file:
    for line in file:
        print(line.strip())
```

Looping directly over a file, like this, reads it one line at a time rather than loading everything into memory at once, which matters once a file gets genuinely large.

---

## Where This Shows Up

Reading a config file when a program starts up, reading a log file line by line while searching for a specific error, reading a saved catalog back into memory, all of it is this exact pattern. `02-terminal/tools/03-searching.md`'s `grep` is, underneath, doing something very close to this same line-by-line read, just automated and built for you.

```mermaid
flowchart LR
    A["open the file"] --> B["read its content"]
    B --> C["file closes automatically"]
```

---

## Try It

Open `catalog.txt` from `shop-inventory-tracker`, if it exists, or create one with a couple of lines by hand. Read it with `file.read()` and print the result. Then read it again with a `for line in file:` loop, printing each line. Compare what each approach gives you.

---

## What You Need to Understand

- `with open(path, "r") as file:` is the standard safe way to open a file for reading
- `read()`, line by line iteration, and `readlines()` each return something different
- `with` guarantees the file closes, even if an error happens while reading

---

## Exercise

Write a small script that opens `catalog.txt`, reads it line by line, and prints only the lines where the quantity is below 10. You'll need to split each line and convert the quantity to an int first, the same pattern `load_catalog` already uses.

---

## Checkpoint

Explain, in your own words:

1. What does `with` actually guarantee that a plain `open()` call alone doesn't?
2. What's the difference between `file.read()` and looping with `for line in file:`?
3. Why would looping line by line matter more for a very large file than for a small one?
