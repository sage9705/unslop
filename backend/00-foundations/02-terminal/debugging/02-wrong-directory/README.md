# Debugging: Wrong Directory

*`00-foundations/02-terminal/debugging/02-wrong-directory/`, part of [Unslop](https://github.com/sage9705/unslop)*

## Reproduce It

Navigate into `01-programming/concepts/`, then run exactly this:

```bash
python main.py
```

Read what comes back.

## Investigate

The command itself is spelled correctly, and `python` exists. Something else is wrong. Check where you actually are, and what's actually sitting there, before assuming the file is missing entirely. This connects directly to [`concepts/04-paths.md`](../../concepts/04-paths.md).

## Fix It

Without leaving `concepts/`, run the Till Calculator successfully, redirecting its output into a file called `output.txt` in `01-programming/`. You don't need to physically move anywhere to do this, the fix is in what you type, not where you stand.

## Verifying Your Fix

Copy `verify.py` from this folder into `01-programming/`, and run it there:

```bash
python verify.py
```

<details>
<summary>Hint, if you're genuinely stuck</summary>

`main.py` is real, it just doesn't live in `concepts/`. What does `01-programming/examples/till-calculator/main.py` look like as a path relative to where you're currently standing?
</details>

## Cleaning Up

Once the check passes, delete `output.txt`.
