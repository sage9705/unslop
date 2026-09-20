# Exercise: Pipes and Redirection

*`00-foundations/02-terminal/exercises/06-pipes-and-redirection/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Task

From inside `01-programming/`:

1. Search for every remaining `NotImplementedError` across `exercises/`, and redirect the result into a file instead of the screen:
   ```bash
   grep -rn "NotImplementedError" exercises > remaining_todos.txt
   ```
2. Run that same search again, this time piped into a second `grep` that just counts the matches, without opening the file at all:
   ```bash
   grep -rn "NotImplementedError" exercises | grep -c "NotImplementedError"
   ```
   Take note of the number it prints.

## Verifying Your Work

Copy `verify.py` from this folder into `01-programming/`, and run it there:

```bash
python verify.py
```

It reads `remaining_todos.txt`, independently counts every `NotImplementedError` across `exercises/` itself, and confirms the two numbers actually agree.

## Concepts You'll Need

- [`tools/03-searching.md`](../../tools/03-searching.md)
- [`concepts/09-pipes-and-redirection.md`](../../concepts/09-pipes-and-redirection.md)

## Cleaning Up

Once the check passes, delete `remaining_todos.txt`.
