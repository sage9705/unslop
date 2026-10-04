# Exercise: Write a File

*`00-foundations/03-files-and-data/exercises/02-write-a-file/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

Every morning the shop owner wants a short reorder report, a file listing everything running low. Sometimes a person adds a handwritten note to it afterward. The report gets regenerated daily, and the notes should never wipe out the report.

## What You Need to Build

In `starter.py`, implement two functions:

1. **`write_reorder_report(catalog, threshold, filepath)`**, writes the first line `REORDER REPORT`, then one `name,quantity` line for every product at or below `threshold`, sorted by name. Returns how many products it listed. Running it again must replace the old report completely.
2. **`append_note(filepath, note)`**, adds one line onto the end of the file without erasing anything already in it.

Choosing the right write mode for each function is the whole exercise. One of them needs `"w"`, the other needs `"a"`, and getting them backwards fails quietly.

## Concepts You'll Need

- [`05-writing-files.md`](../../concepts/05-writing-files.md)

## Self Check

```bash
python starter.py
```

`self_check()` writes into a temporary folder, so it never leaves files behind. You should see `All checks passed.`
