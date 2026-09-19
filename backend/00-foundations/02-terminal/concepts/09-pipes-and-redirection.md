# Pipes and Redirection

*`00-foundations/02-terminal/concepts/09-pipes-and-redirection.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Fundamental**

## The Question

How do you send program output somewhere other than the screen, or pass one program's output directly into another?

---

## Redirection sends output somewhere else

The previous lesson explained that every process has standard input, standard output, and standard error. By default, those streams are connected to the terminal window.

Redirection changes where a stream goes. Instead of showing on the screen, output can be written to a file.

For example, a command's normal output can be redirected into a file so you can keep a copy of it without watching it scroll by.

This is useful for logs, saved reports, and capturing command output for later inspection.

---

## Piping connects programs together

Piping goes one step further. It connects the output of one command directly into the input of another command.

This lets small tools be chained together. One command can filter text, another can count results, and another can sort them, all without creating temporary files.

```mermaid
flowchart LR
    A["Program A"] -- output --> B["Program B"]
    B --> C["Program B's output"]
```

This is one of the most important ideas in the terminal: small programs, designed to do one thing well, can be combined into a larger workflow.

---

## Small commands are usually better for chaining

Terminal tools are often intentionally narrow in purpose. They may list files, search text, filter lines, or count matches. That makes them easy to combine.

Instead of building one giant command that does everything, developers often chain together a few focused commands. The result is easier to understand, easier to debug, and easier to reuse in different situations.

---

## Where this shows up in real debugging

When logs get large, a common workflow is:

- read the log file
- filter for a specific error word
- sort or count the matches
- inspect only the relevant lines

This is a standard way of investigating production problems. It avoids manually scanning thousands of lines by eye and instead uses a pipeline of small tools that do the heavy lifting.

---

## Try it

Think about a program you have run before that produced output you wanted to search through. Imagine taking that output and running it through a filter step so only the lines you care about remain visible.

---

## What you need to understand

- redirection changes where output goes, often into a file
- piping sends one program's output directly into another program's input
- small terminal tools are designed to be chained together for larger workflows

---

## Exercise

Describe, in plain language, how you would both watch a command's output on screen and save a copy of it to a file at the same time. What would redirection alone not do that piping or a combined approach would?

---

## Checkpoint

Explain, in your own words:

1. What is the difference between redirection and piping?
2. Which symbol sends a command's output to a file, and which symbol connects the output of one program to the input of another?
3. Why are terminal commands usually designed to do one small job well instead of handling many tasks at once?
