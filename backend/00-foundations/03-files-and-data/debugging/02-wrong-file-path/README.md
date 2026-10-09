# Debugging: Wrong File Path

*`00-foundations/03-files-and-data/debugging/02-wrong-file-path/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Report

"It works perfectly on my computer. When my colleague runs the same program, she gets a file not found error, and the file is definitely there."

## Reproduce It

First, run it from inside this folder:

```bash
python broken_catalog_loader.py
```

Look closely at what happens. Then go up one level to `debugging/`, and run it again from there:

```bash
python 02-wrong-file-path/broken_catalog_loader.py
```

The code is identical in both runs. Only the place you launched it from changed.

## Investigate

Revisit [`concepts/06-file-paths.md`](../../concepts/06-file-paths.md). The path in `open()` is a relative one. Work out what it is relative to, and why that differs between your computer and your colleague's.

## Fix It

Make `load_catalog()` find `data/catalog.json` no matter which directory the program is launched from.

<details>
<summary>Hint, if you're genuinely stuck</summary>

A running script can find out where its own file lives on disk. Build the path from that location, and the program stops depending on where it was launched.
</details>
