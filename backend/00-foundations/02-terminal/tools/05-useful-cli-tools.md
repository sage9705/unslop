# Useful CLI Tools

*`00-foundations/02-terminal/tools/05-useful-cli-tools.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Reference**

A handful of everyday commands that don't fit neatly under navigation, file management, searching, or processes, but show up constantly anyway.

---

## The Commands

| Command | What It Does | Example |
|---|---|---|
| `cat <file>` | Prints an entire file's contents straight to the screen | `cat README.md` |
| `less <file>` | Opens a file for scrolling through, one screen at a time | `less main.py` |
| `echo "<text>"` | Prints text back to the screen, most useful combined with redirection | `echo "Hello"` |
| `history` | Shows a list of commands you've recently run | `history` |
| `clear` | Clears everything currently shown in the terminal window | `clear` |

---

## Walking Through It

A quick look at a README without opening an editor:

```bash
$ cat examples/till-calculator/README.md
```

For anything longer than a screen's worth of text, `less` is far more comfortable:

```bash
$ less examples/shop-inventory-tracker/inventory.py
```

Scroll with the arrow keys or the space bar, and press `q` to exit back to your prompt.

---

## Common Mistakes

- Running `cat` on a long file floods the screen with everything at once, scrolled straight past. `less` handles that far better.
- Not knowing how to exit `less` is a genuinely common first moment of panic. The key is `q`.
- Forgetting these commands exist at all, and opening a full text editor for something a one line command would have answered in a second.

---

## One Habit Worth Keeping

Every command across this whole `tools/` folder has a manual page. Whenever one behaves in a way you didn't expect, `man <command>`, or `<command> --help` if `man` isn't available, explains exactly what it does and every option it accepts, straight from the tool itself.

---

## What You Need to Understand

- `cat` dumps a whole file at once, `less` lets you scroll through it
- `echo` prints text, and becomes genuinely useful once combined with redirection
- `man` and `--help` answer almost every "what does this command actually do" question

---

## Exercise

Use `cat` to read one shop example's `README.md` in full. Then use `less` to scroll through its `main.py`, and exit cleanly with `q`.

---

## Checkpoint

1. When would you reach for `less` instead of `cat`?
2. How do you exit `less` once you're inside it?
3. What's the fastest way to find out what a command you've never used before actually does?
