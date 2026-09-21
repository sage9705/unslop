# Debugging: Process Problem

*`00-foundations/02-terminal/debugging/04-process-problem/`, part of [Unslop](https://github.com/sage9705/unslop)*

## Reproduce It

Copy `stubborn.py` from this folder into an empty directory somewhere, and run it:

```bash
python stubborn.py
```

It writes to `heartbeat.txt` once a second, the same way `exercises/04-process-investigation/stuck.py` did. In a second terminal, find its PID and stop it the exact way that worked before:

```bash
kill <PID>
```

Check `heartbeat.txt`. It's still updating.

## Investigate

A plain `kill` is a request, not a command the operating system forces through. A process can choose to ignore it. This one does, on purpose, so you can see what that actually looks like.

## Fix It

Stop it for real.

## Verifying Your Fix

Copy `verify.py` from this folder into the same directory, and run it there:

```bash
python verify.py
```

<details>
<summary>Hint, if you're genuinely stuck</summary>

`tools/04-inspecting-processes.md` covers a second, more forceful version of `kill`, one that skips giving the process any say in the matter at all.
</details>

## Cleaning Up

Once the check passes, delete `stubborn.py`, `verify.py`, and `heartbeat.txt`.
