# Programming Checkpoint

*`00-foundations/01-programming/checkpoint.md`, part of [Unslop](https://github.com/sage9705/unslop)*

## What This Is

This isn't a test anyone grades. It's a checkpoint you run on yourself, honestly, before moving on. If any part of it feels shaky, that's useful information, not a failure, go back to the relevant file in `concepts/` or `problem-solving/` and spend more time there. Read the docs of specific language features(Python) you need for any implementation. Nobody is behind schedule here.

The bar is simple: you should be able to sit down with a blank file, solve a small real problem, and explain what you did without reading it off the screen.

---

## Part 1: Explain

Answer these in your own words, out loud or in writing, without looking anything up first. If you get stuck on one, that tells you exactly where to go back and review.

1. What's the difference between a value and a variable?
2. Why does `"5" + 5` raise an error, and what does that have to do with real bugs in real software?
3. What's the difference between a parameter and an argument?
4. Why would two different functions be able to use a local variable with the same name without conflict?
5. What actually happens when you write `specials = inventory` instead of `specials = inventory.copy()`?
6. Why is a dictionary lookup still fast even when the dictionary has fifty thousand entries, while scanning a list gets slower as it grows?
7. What's the difference between catching a specific exception like `ValueError` and using a bare `except:`?
8. Given a messy, half formed request like "make the shop run better," what are the first three questions you'd ask before writing any code?

---

## Part 2: Build Something New

Every project so far, the Till Calculator, the Stock Reorder Alert, the Customer Feedback Analyzer, the Shop Inventory and Sales Tracker, has already been described for you in some amount of detail. This one hasn't.

**The problem:** At the end of the day, a shop's till should hold exactly the amount of cash the system says it sold, minus any refunds given during the day. In practice it rarely lines up exactly. Build a small program that reconciles the till.

Your program should:

1. Take the system's recorded total sales for the day, a single number.
2. Take a list of refunds given during the day, each a separate amount.
3. Calculate what the till should contain: recorded sales minus the total of all refunds.
4. Take the amount of cash actually counted in the till at closing.
5. Compare the two, and report one of three outcomes: **Balanced** (matches exactly), **Over** (more cash than expected), or **Short** (less cash than expected), along with the exact difference.
6. If the difference is more than a small threshold you choose, say 5 units of currency, flag it as needing manual review instead of just reporting the number.

Work through this the way the rest of this folder has taught you to:

- Understand the problem first, the way `problem-solving/01-understanding-the-problem.md` describes, before writing anything.
- Decompose it into pieces, the way `problem-solving/02-decomposition.md` describes.
- Sketch pseudocode for the trickier part, the balanced versus over versus short logic, before writing real Python.
- Build it with functions, not one long block of code.
- Handle at least one realistic failure case gracefully, what happens if the cash counted is entered as something that isn't a valid number?

**Then, deliberately break it.** Introduce one bug on purpose, an off by one in your threshold check, a variable reset in the wrong place, whatever you like. Don't fix it yet. Trace through your own code by hand, the way `problem-solving/04-tracing-programs.md` describes, and find it the way you would if you hadn't just planted it yourself. Then fix it.

> Build this one yourself, no AI. That's the Golden Rule, see the [section README](./README.md#the-golden-rule-zero-ai-code-generation).

---

## Part 3: The Final Question

Close the file. Don't look at it.

Can you explain, from memory, what your program does, how it's structured, and why you made the decisions you made?

If yes, you're ready to move on. If not, that's not a problem, it's just information. Go back, spend more time with whichever part felt uncertain, and come back to this checkpoint when it feels solid. There's no clock running.

---

## What's Next

Once this genuinely feels solid, move on to `00-foundations/02-terminal/`, and from there, the rest of the Foundations path.

Everything you just practiced, breaking a vague problem into a clear one, building it piece by piece, tracing your own logic, handling failure gracefully, is the same skill you'll be using when the problems get bigger: an HTTP server instead of a till, a database instead of a catalog dictionary, a production incident instead of a self planted bug. The scale changes. The way you think about it doesn't.
