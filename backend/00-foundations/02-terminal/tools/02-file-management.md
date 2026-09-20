# File Management

*`00-foundations/02-terminal/tools/02-file-management.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Reference**

Creating, copying, moving, and deleting files and directories, entirely from the terminal, without a graphical file browser in sight.

---

## The Commands

| Command | What It Does | Example |
|---|---|---|
| `mkdir <name>` | Creates a new, empty directory | `mkdir drafts` |
| `mkdir -p <path>` | Creates a directory, and any missing parent directories, in one go | `mkdir -p drafts/2024` |
| `touch <file>` | Creates a new, empty file, or updates an existing file's timestamp | `touch notes.md` |
| `cp <source> <destination>` | Copies a file | `cp main.py main_backup.py` |
| `cp -r <source> <destination>` | Copies an entire directory and everything inside it | `cp -r till-calculator till-calculator-backup` |
| `mv <source> <destination>` | Moves a file or directory, or renames it if the destination is just a new name | `mv notes.md draft-notes.md` |
| `rm <file>` | Deletes a file, permanently | `rm notes.md` |
| `rm -r <directory>` | Deletes a directory and everything inside it, permanently | `rm -r drafts` |

---

## Walking Through It

Copying an existing shop example to experiment on, without touching the original:

```bash
$ cd examples
$ cp -r till-calculator till-calculator-experiment
$ cd till-calculator-experiment
$ ls
README.md    main.py
```

From here, edit `main.py` freely, run `python main.py`, break things on purpose, and none of it touches the real `till-calculator/`. Once finished:

```bash
$ cd ..
$ rm -r till-calculator-experiment
```

---

## Common Mistakes

- `cp` and `rm` both refuse to touch a directory unless you add `-r`. Forgetting it is the single most common reason either command "doesn't work."
- `rm` has no undo and no recycle bin. Once it runs, the file is gone. Get comfortable running `ls` on the exact path first, especially before `rm -r`, to confirm exactly what's about to be deleted.
- There's no separate "rename" command. Moving a file to a new name in the same folder, `mv oldname.py newname.py`, is how renaming actually works.

---

## What You Need to Understand

- `mkdir` and `touch` create, `cp` duplicates, `mv` relocates or renames, `rm` deletes permanently
- directories need the `-r` flag with both `cp` and `rm`
- deletion from the terminal is immediate and permanent

---

## Exercise

Create a new directory anywhere outside `01-programming/`, called `sandbox`. Copy one shop example into it. Rename the copied `main.py` to `experiment.py`. Confirm the rename with `ls`. Then delete the entire `sandbox` directory in one command.

---

## Checkpoint

1. What's the difference between `cp` and `mv`?
2. Why does `rm drafts` fail on a directory, while `rm -r drafts` succeeds?
3. How do you rename a file, given there's no dedicated rename command?
