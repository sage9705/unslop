# Debugging

*`00-foundations/01-programming/debugging/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What This Folder Is

Every program in `broken_*.py` here already runs. That's the point. None of them crash on the first line, and most of them don't crash at all, they just quietly do the wrong thing, the way real bugs actually behave. Your job isn't to write new code, it's to find out why a program that looks fine is producing a wrong answer, and fix it.

Run the file, read the output carefully, and treat the failing test as the bug report telling you what went wrong.

---

## The Three Categories

| Folder                                    | The Bug Looks Like                                                             | Why It's Hard to Spot                                                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| [`01-logic-errors/`](./01-logic-errors/) | The program runs and gives an answer, but the answer is wrong                  | The code doesn't look broken at a glance, the mistake is in the reasoning.                                                |
| [`02-state-errors/`](./02-state-errors/) | A variable holds the wrong value at some point in the program's life           | The bug is in when a value gets set, reset, or shared                                                                    |
| [`03-data-errors/`](./03-data-errors/)   | The program misbehaves because the data wasn't shaped the way the code assumed | The code is often correct in isolation, it's the mismatch between the code's assumptions and the real data that breaks it |

---

## How to Work Through One

1. Read the broken file's commented instructions. It tells you what the function or script is supposed to do.
2. Run the file and read the output. The failing `assert` or wrong printed result is the clue that tells you what is actually happening versus what should happen.
3. **Trace the code by hand before changing anything**, the way [`problem-solving/04-tracing-programs.md`](../problem-solving/04-tracing-programs.md) describes. Guessing and rerunning is slower than it feels.
4. Form a hypothesis about where the logic diverges from what's intended. Check it against the code.
5. Make the smallest change that fixes the cause.
6. Run the file again and check whether the output now matches the expected result.

There's a `README.md` in each subfolder with a short hint if you're stuck after genuinely trying, but each one describes the *symptom*, not the fix. Reading the hint before attempting step 3 defeats the purpose.
