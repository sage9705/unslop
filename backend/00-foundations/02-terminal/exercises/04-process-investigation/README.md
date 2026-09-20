# Exercise: Process Investigation

*`00-foundations/02-terminal/exercises/04-process-investigation/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Task

`stuck.py`, included in this folder, runs forever on purpose, and writes a timestamp to `heartbeat.txt` once a second while it's alive.

1. Copy `stuck.py` into an empty folder somewhere, and run it:
   ```bash
   python stuck.py
   ```
   Notice it never returns control of that terminal.
2. Open a second terminal. Find `stuck.py`'s process ID.
3. Stop it with a plain `kill`, not `kill -9`.

## Verifying Your Work

Copy `verify.py` into the same folder `heartbeat.txt` was written to, and run it there:

```bash
python verify.py
```

It checks how long ago `heartbeat.txt` last changed. If the process is still alive, that file is updating every second. If it's genuinely stopped, the file goes stale immediately.

## Concepts You'll Need

- [`concepts/06-processes.md`](../../concepts/06-processes.md)
- [`tools/04-inspecting-processes.md`](../../tools/04-inspecting-processes.md)

## Cleaning Up

Once the check passes, delete `stuck.py` and `heartbeat.txt`.
