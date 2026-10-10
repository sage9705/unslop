# Debugging: Data Loss

*`00-foundations/03-files-and-data/debugging/04-data-loss/`, part of [Unslop](https://github.com/sage9705/unslop)*

Losing data is the most expensive kind of file bug, because nothing crashes at the moment it happens. These two scripts lose data in two different ways.

---

## `broken_daily_log.py`

**The report:** "The power went out at lunchtime and we restarted the till. At closing time, the sales log only had the afternoon in it. The whole morning had vanished."

```bash
python broken_daily_log.py
```

**Investigate:** Look at what happens every time the program starts up. The sales get logged with the right mode. Something else runs first.

**Fix it:** After a restart, every earlier sale must still be there, and the header line must appear exactly once.

<details>
<summary>Hint, if you're genuinely stuck</summary>

`start_day` runs on every startup, including restarts. Think about what its job is, and whether it should do that job when the file already holds a day's work.
</details>

---

## `broken_save_store.py`

**The report:** "A staff member added a product with a strange extra field, and the save failed with an error. We expected that. But the next morning the entire catalog file was damaged, including products that had saved fine for months."

```bash
python broken_save_store.py
```

**Investigate:** The failed save was supposed to change nothing. Trace the order of events inside `save_store`. At what moment does the old content of the file disappear, and at what moment does the program discover the data can't be saved? Revisit [`concepts/12-persistence.md`](../../concepts/12-persistence.md) for a related warning.

**Fix it:** A save that fails must still raise `TypeError`, and must leave the previous file exactly as it was.

<details>
<summary>Hint, if you're genuinely stuck</summary>

The old file is destroyed the instant it's opened for writing. Could the program find out whether the data can be saved before it opens the file?
</details>
