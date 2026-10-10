# Files and Data Checkpoint

*`00-foundations/03-files-and-data/checkpoint.md`, part of [Unslop](https://github.com/sage9705/unslop)*

## What This Is

Nobody grades this. Run it on yourself, honestly, before moving on. If something feels shaky, go back to the relevant file in `concepts/` and spend more time there.

The bar is simple: can you take a messy file you've never seen, turn it into data your program can trust, and keep that data safe between runs?

---

## Part 1: Explain

Answer these without looking anything up first.

1. A Python variable and a file can both hold a product's price. Why does one survive a restart and the other doesn't?
2. What is a file, underneath its name and extension? Why can't an extension tell you what a file really contains?
3. What's the difference between text and binary data, and what goes wrong if you open a binary file in text mode?
4. What does `with open(...)` guarantee that a plain `open(...)` doesn't?
5. What does `"w"` do to a file that already exists, and when would `"a"` be the right choice?
6. A relative path inside `open()` resolves against something. What is it, and how can one line of code create a file in two different places?
7. Why is JSON a better home for a product catalog than comma-separated lines? What's the difference between serializing and deserializing?
8. What's the difference between parsing a value and validating it? Give an example of something that parses without a problem and still shouldn't be trusted.
9. What can happen to a file if a program crashes partway through writing it, and what's one way to make that safer?

---

## Part 2: The Supplier Price List Import

Every project in this folder has described its inputs in detail. This one hands you a messy file and leaves the design to you.

**The problem:** A supplier emails the shop a price list as a plain text file. The shop keeps its own records in `price_list.json`. Build a program that imports the supplier's list safely.

### Setup

1. Make a new empty folder anywhere, for example `price-import/`.
2. Copy `supplier_prices.txt` and `verify.py` from this folder into it.
3. Create `price_list.json` in that folder, by hand, containing exactly this. It stands in for what the shop already has from earlier imports:

   ```json
   {
     "Matches": {"price": 1.5, "unit": "box"},
     "Sugar": {"price": 10.0, "unit": "kg"}
   }
   ```
4. Create `import_prices.py` in the same folder. This is the program you're building.

Open `supplier_prices.txt` and read it before writing anything. Each line has the shape `name | price | unit`.

### What the program must do

- Ignore blank lines, and lines starting with `#`.
- Accept a line only if it has exactly three fields separated by `|`, the name and unit are not empty once the whitespace around them is trimmed, and the price is a positive number.
- Merge the accepted products into `price_list.json`. New products get added, products already there get their price and unit updated, and products the supplier didn't mention stay exactly as they were.
- Write every rejected line to `rejected_lines.txt`, one per line, each with the reason it was rejected. Each run rewrites this file from scratch, so running the program twice leaves the same three lines the first run left.
- Build the paths to its files from the script's own location, so it works no matter which directory it's launched from.
- Print a one-line summary of how many products were saved and how many lines were rejected.

Work through it the way the rest of Unslop has taught you:

- Understand the problem first, with `01-programming/problem-solving/01-understanding-the-problem.md` in mind.
- Break it into pieces, and sketch pseudocode for the trickiest one, deciding whether a line is acceptable.
- Build it from functions.

### Run it twice

```bash
python import_prices.py
python import_prices.py
```

The second run should leave everything exactly as the first one did.

### Verify it

From inside your folder:

```bash
python verify.py
```

It checks `price_list.json` and `rejected_lines.txt` against what the correct result has to be. Then it launches your program from a different directory, to confirm it still finds its files. You should see `All checks passed.`

### Now break it on purpose

Keep a backup first, using the terminal:

```bash
cp price_list.json price_list_backup.json
```

Then open `price_list.json` in an editor and damage it, delete a closing brace, and run your program.

A well built program stops with a short message saying the file is damaged, and leaves the file exactly as it found it, so a person can look at it. If yours crashed with a long traceback, or quietly replaced the damaged file with a fresh one and destroyed what was in it, fix that. Restore the backup afterward, and run `verify.py` again.

---

## Part 3: The Final Question

Close everything. Don't look at your code.

Can you explain, from memory, how your program decides whether a line is acceptable, why it merges into the existing file, and what happens to the data if something goes wrong halfway through a save?

If yes, you're ready to move on. If not, that's useful information. Go back to the part that felt uncertain, and return when it feels solid.

---

## What's Next

Once this feels solid, move on to `00-foundations/04-git/`.

Your programs can now keep their data safe between runs. Git does the same thing for your work itself, a history of every change that you can search, compare, and return to.
