# Inspecting Processes

*`00-foundations/02-terminal/tools/04-inspecting-processes.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Reference**

Seeing what's actually running on your machine right now, and stopping something that won't stop on its own. This is the practical side of `concepts/06-processes.md`.

---

## The Commands

| Command | What It Does | Example |
|---|---|---|
| `ps` | Lists processes running in your current terminal session | `ps` |
| `ps aux` | Lists every process running on the whole machine, with detail | `ps aux` |
| `top` | Shows a live, constantly updating view of running processes | `top` |
| `htop` | A friendlier, colored version of `top`, if it happens to be installed | `htop` |
| `kill <PID>` | Asks a process to stop, giving it a chance to shut down cleanly | `kill 4821` |
| `kill -9 <PID>` | Forces a process to stop immediately, no cleanup | `kill -9 4821` |

Every process has a process ID, a **PID**, a number the operating system assigns it the moment it starts. That number is what you hand to `kill`.

---

## Walking Through It

A small script with a genuine infinite loop, saved as `stuck.py`, is a safe way to practice this without touching anything real:

```python
while True:
    pass
```

Run it, and it never returns control of that terminal window:

```bash
$ python stuck.py
(nothing happens, the terminal just sits here)
```

Open a second terminal, and find it:

```bash
$ ps aux | grep python
yourname   4821   0.0  0.1   ...   python stuck.py
```

`4821` is its PID. Stop it:

```bash
$ kill 4821
```

Switch back to the first terminal, and it's returned control, `stuck.py` is gone.

---

## Common Mistakes

- Reaching for `kill -9` as a first move, out of habit. A plain `kill` gives the process a chance to close any file it had open or finish a cleanup step, `-9` skips all of that entirely. Save `-9` for when a plain `kill` genuinely didn't work.
- Misreading the PID column and stopping the wrong process. Always double check the command name shown next to the PID before killing anything.
- Forgetting that `Ctrl+C` is the everyday way to stop whatever's running directly in front of you, in the same terminal window. `kill` matters specifically for a process in a different window, or one you didn't start yourself.

---

## What You Need to Understand

- `ps` and `top` show what's currently running, and give you each process's PID
- `kill <PID>` asks a process to stop, `kill -9 <PID>` forces it
- `Ctrl+C` and `kill` solve the same problem from two different starting points

---

## Exercise

Save a script containing `while True: pass` as `stuck.py`. Run it in one terminal. In a second terminal, find its PID and stop it with a plain `kill`. Confirm the first terminal returns to normal.

---

## Checkpoint

1. What is a PID, and where do you find one?
2. What's the difference between `kill` and `kill -9`?
3. When would `Ctrl+C` not be the right tool, and `kill` would be?
