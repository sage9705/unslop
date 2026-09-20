# Exercise: File System Navigation

*`00-foundations/02-terminal/exercises/02-file-system-navigation/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Task

From inside `01-programming/`, using only the terminal:

1. Create a new directory called `field-notes`, directly inside `01-programming/`.
2. Inside `field-notes/`, create three empty files: `day1.md`, `day2.md`, and `day3.md`.
3. Rename `day3.md` to `day3-final.md`.

## Verifying Your Work

Copy `verify.py` from this folder into `01-programming/`, then run it from there:

```bash
python verify.py
```

It checks that `field-notes/` exists with the right files inside, and specifically that `day3.md` was renamed rather than just copied alongside a new file.

## Concepts You'll Need

- [`tools/02-file-management.md`](../../tools/02-file-management.md)

## Cleaning Up

Once every check passes, delete the whole `field-notes/` directory in one command before moving on.
