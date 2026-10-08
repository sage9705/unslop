# Debugging: File Not Found

*`00-foundations/03-files-and-data/debugging/01-file-not-found/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Report

"We installed the new till program this morning. It crashed immediately. Nothing was wrong with the computer, it just wouldn't start."

## Reproduce It

```bash
python broken_catalog_load.py
```

Read the error all the way to its last line.

## Investigate

The program loads `shop_catalog.json` when it starts. Ask when that file would exist, and when it wouldn't. A brand new installation has never saved anything yet.

The `self_check()` at the bottom has three parts, and each one matters. A first run with no file should work. An existing file should load normally. A damaged file should still be reported as a problem. A fix has to satisfy all three.

## Fix It

Make the program start cleanly on a first run, without hiding genuine problems.

<details>
<summary>Hint, if you're genuinely stuck</summary>

A missing file on a first run is a normal situation, and a damaged file is an error. Your fix has to tell those two apart. Handling every possible error the same way will pass one check and fail another.
</details>
