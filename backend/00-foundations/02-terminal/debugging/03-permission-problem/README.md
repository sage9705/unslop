# Debugging: Permission Problem

*`00-foundations/02-terminal/debugging/03-permission-problem/`, part of [Unslop](https://github.com/sage9705/unslop)*

This one is most meaningful on Mac or Linux. On Windows, read through it, the underlying idea still matters even if the exact mechanics differ.

## Reproduce It

Copy `greet.py` from this folder into an empty directory somewhere, then try to run it directly:

```bash
./greet.py
```

Read what comes back.

## Investigate

The file is right there. `ls` proves it exists. Read the exact wording of the error closely, it's telling you something more specific than "missing."

```bash
ls -l greet.py
```

Compare what you see there to a file you already know can run directly.

## Fix It

Get `./greet.py` to run successfully without changing a single line inside the file itself.

## Verifying Your Fix

Copy `verify.py` from this folder into the same directory, and run it there:

```bash
python verify.py
```

<details>
<summary>Hint, if you're genuinely stuck</summary>

A file being readable and a file being runnable are two different permissions. One command grants the second one.
</details>

## Cleaning Up

Once the check passes, delete `greet.py`, `verify.py`, and `ran.txt`.
