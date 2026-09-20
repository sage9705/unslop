# Exercise: Terminal Navigation

*`00-foundations/02-terminal/exercises/01-terminal-navigation/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Task

Starting from `01-programming/`, using only `pwd`, `ls`, and `cd`, navigate down into `debugging/02-state-errors/`. Don't type the whole path in one line, actually move through it step by step, the way `tools/01-navigation.md` walked through `examples/till-calculator/`.

Once you believe you've arrived, confirm it.

## Verifying Your Location

Save `verify.py` from this folder somewhere convenient, outside of `01-programming/` itself, your home directory works fine. Whenever you believe you've reached the target directory, run it by its full path, for example:

```bash
python /full/path/to/verify.py
```

It checks your current working directory directly, and tells you whether you're standing exactly where the task asked.

## Concepts You'll Need

- [`concepts/03-files-and-directories.md`](../../concepts/03-files-and-directories.md)
- [`concepts/04-paths.md`](../../concepts/04-paths.md)
- [`tools/01-navigation.md`](../../tools/01-navigation.md)
