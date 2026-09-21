# Debugging: Command Failed

*`00-foundations/02-terminal/debugging/01-command-failed/`, part of [Unslop](https://github.com/sage9705/unslop)*

## Reproduce It

From inside `01-programming/`, run exactly this:

```bash
pyton examples/customer-feedback-analyzer/main.py
```

Read what comes back.

## Investigate

That error is the shell being completely honest, it looked for a program by that exact name, and it genuinely isn't one. This is the same mechanism covered in [`concepts/02-shell-and-commands.md`](../../concepts/02-shell-and-commands.md).

Work out what's actually wrong before fixing it. Nothing about the file itself is broken.

## Fix It

Run the Customer Feedback Analyzer successfully, redirecting its output into a file called `output.txt`, from inside `01-programming/`.

## Verifying Your Fix

Copy `verify.py` from this folder into `01-programming/`, and run it there:

```bash
python verify.py
```

<details>
<summary>Hint, if you're genuinely stuck</summary>

Read the exact characters in the failed command again, one at a time.
</details>

## Cleaning Up

Once the check passes, delete `output.txt`.
