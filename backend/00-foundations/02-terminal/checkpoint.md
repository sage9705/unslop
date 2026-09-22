# Terminal Checkpoint

*`00-foundations/02-terminal/checkpoint.md`, part of [Unslop](https://github.com/sage9705/unslop)*

## What This Is

This isn't graded. Run it on yourself, honestly, before moving on. If something feels shaky, that's useful information, go back to the relevant file in `concepts/` or `tools/` and spend more time there.

The bar is simple: can you sit down at a terminal, with no graphical file browser open, and get a real task done?

---

## Part 1: Explain

Answer these without looking anything up first.

1. What's the difference between the terminal and the shell?
2. What's the difference between an absolute path and a relative path?
3. What actually happens to a program the moment you run it?
4. If you run the same script twice at once, what do you get, and do the two copies share anything?
5. Where does an environment variable live, compared to a variable inside your Python code?
6. What are the three channels every process opens by default, and which one does `print()` use?
7. What's the difference between redirecting a command's output and piping it into another command?
8. Given a command that fails, what's the difference between "command not found," "no such file or directory," and "permission denied," and what does each one actually tell you about the cause?

---

## Part 2: The Shop System Audit

A new developer is joining the shop project. Put together a short audit of the codebase for them, entirely from the terminal, using `01-programming/` as the target.

From inside `01-programming/`:

1. Use `find` to list every `.py` file inside `examples/`, and redirect that list into a new file called `audit_report.txt`.
2. Count how many `README.md` files exist anywhere inside `01-programming/`, using `find` piped into `wc -l` (a tool that counts lines, new here, but exactly what it sounds like), and append that number onto `audit_report.txt`. Appending uses `>>` instead of `>`, the one piece of new syntax this task needs, `>` would have overwritten everything you just wrote in step 1.
3. Without moving into its folder, run `examples/shop-inventory-tracker/main.py` directly by its path, and append its output onto `audit_report.txt` too.
4. Set an environment variable called `AUDITOR` to your own name. Then write a short script, a few lines, that reads `AUDITOR` from its environment and appends one line to `audit_report.txt`: `Audit run by <your name>`.
5. Write and run a script that runs forever on purpose, the same shape as `stuck.py` from `exercises/04-process-investigation/`. In a second terminal, confirm it's genuinely running with `ps`, then stop it.

## Verifying Your Work

Copy `verify.py` from this folder into `01-programming/`, and run it there:

```bash
python verify.py
```

It checks `audit_report.txt` directly, your file list, your count, your appended program output, and your auditor line, each against an independent check of the real folder.

---

## Part 3: The Final Question

Close everything. Don't look at `audit_report.txt` or your terminal history.

Can you explain, from memory, what each of those five steps actually did, and why `>>` mattered in step 2 specifically?

If yes, you're ready to move on. If not, that's fine, it's just information. Spend more time with whichever step felt shaky, and come back when it feels solid.

---

## What's Next

Once this genuinely feels solid, move on to `00-foundations/03-files-and-data/`.

Everything practiced here, finding your way around a project, running something from anywhere, investigating a process, reading an environment, chaining small tools together, stops being a terminal exercise soon and starts being how you actually work: deploying code, reading a server's logs, restarting something that crashed. The scale changes. The habits don't.
