# Navigation

*`00-foundations/02-terminal/tools/01-navigation.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Reference**

Three commands cover almost all of everyday movement around a filesystem: knowing where you are, seeing what's around you, and moving somewhere else. This builds directly on `concepts/03-files-and-directories.md` and `concepts/04-paths.md`, this doc is the practical side of those same ideas.

---

## The Commands

| Command | What It Does | Example |
|---|---|---|
| `pwd` | Prints the full path of the directory you're currently standing in | `pwd` |
| `ls` | Lists the contents of the current directory | `ls` |
| `ls -l` | Lists contents with detail: permissions, size, last modified date | `ls -l` |
| `ls -a` | Lists contents including hidden files, the ones starting with a dot | `ls -a` |
| `cd <path>` | Moves into a different directory | `cd examples` |
| `cd ..` | Moves up one directory | `cd ..` |
| `cd ~` | Jumps straight to your home directory | `cd ~` |
| `cd -` | Jumps back to whichever directory you were just in | `cd -` |

---

## Walking Through It

Starting from the top of `01-programming/`:

```bash
$ pwd
/home/yourname/unslop/01-programming

$ ls
README.md    checkpoint.md    concepts    debugging    examples    exercises    problem-solving

$ cd examples
$ pwd
/home/yourname/unslop/01-programming/examples

$ ls
README.md    customer-feedback-analyzer    shop-inventory-tracker    stock-reorder-alert    till-calculator

$ cd till-calculator
$ ls
README.md    main.py

$ cd ../..
$ pwd
/home/yourname/unslop/01-programming
```

Every one of those `cd` calls used a relative path, moving from wherever the shell already happened to be standing. `cd ../..` moved up two levels in one line, `examples/till-calculator` back to `01-programming`.

---

## Common Mistakes

- On most systems, `examples` and `Examples` are two completely different names. Typing the wrong case is one of the most common first reasons `cd` fails.
- `ls` on its own only shows regular files and folders. Anything starting with a dot, like a hidden configuration file, only appears with `ls -a`.
- Running `cd` with nothing after it usually sends you straight back to your home directory on many systems, which can feel like you got lost if you weren't expecting it.

---

## What You Need to Understand

- `pwd` answers "where am I right now"
- `ls` answers "what's here"
- `cd` moves you somewhere else, using either a relative or an absolute path

---

## Exercise

Starting from `01-programming/`, using only `pwd`, `ls`, and `cd`, navigate all the way down to `exercises/03-functions/`. Confirm you've arrived with `pwd`, then find your way back to `01-programming/` using relative paths only.

---

## Checkpoint

1. What's the difference between what `pwd` and `ls` each tell you?
2. What does `cd ..` do, and how is it different from `cd -`?
3. Why would `cd Examples` fail even if a folder named `examples` genuinely exists right there?
