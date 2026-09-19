# Paths

*`00-foundations/02-terminal/concepts/04-paths.md`, part of [Unslop](https://github.com/sage9705/unslop)*

> **Fundamental**

## The Question

How do you tell your computer exactly where a file lives?

---

## A Path Is an Address

A path is a written route through the filesystem tree covered in the last doc, a description of exactly how to walk from one point to a specific file or directory. There are two kinds, and knowing which one you're looking at matters constantly.

## Absolute Paths

An absolute path starts from the root of the tree and spells out every single step along the way. No matter where you're currently standing, an absolute path always points at the same exact place.

```text
/home/yourname/unslop/01-programming/examples/till-calculator/main.py
```

## Relative Paths

A relative path starts from wherever you currently happen to be standing, your working directory, and describes the route from there. If your terminal is already sitting inside `till-calculator/`, the relative path to that same file is just:

```text
main.py
```

Your shell is always standing somewhere in the tree at any given moment. That location is exactly what a relative path gets measured against.

---

## `.` and `..`

Two shorthand symbols come up constantly once you start moving around a filesystem from the terminal:

- `.` means right here, the directory you're currently standing in
- `..` means one level up, the directory that contains this one

```mermaid
flowchart TD
    A["01-programming/"] --> B["examples/"]
    B --> C["till-calculator/"]
    C -.. means stay here .-> C
    C -.. .. means go up one level .-> B
```

Standing inside `till-calculator/`, `.` refers to `till-calculator/` itself, and `..` refers to `examples/`, the folder directly above it.

---

## Where This Shows Up

This is the exact idea behind `concepts/12-modules.md` in `01-programming`. When `main.py` wrote `import inventory`, Python used a relative path under the hood to find `inventory.py` sitting right next to it in the same folder. Move that file somewhere else, and that same simple reference breaks immediately.

This is also one of the most common real reasons a program works perfectly on your machine and then fails the moment it runs somewhere else. A path that was absolute and specific to your computer, or a relative path that assumed a working directory that changed, is behind a huge share of "it worked yesterday" bugs in real software. Every time you deploy an application later in Unslop, configuration files reference other files by path, and getting that wrong is a very ordinary way for a deployment to quietly fail.

---

## Try It

From wherever your terminal happens to be open right now, write down on paper what you believe the absolute path to your current location is, and what `..` would point to from there. You'll be able to confirm both exactly once you reach `tools/01-navigation.md`.

---

## What You Need to Understand

- a path describes a route through the filesystem to a specific file or directory
- an absolute path always points to the same place, regardless of where you're standing
- a relative path is measured from your current working directory
- `.` means here, `..` means one level up

---

## Exercise

Pick any file inside your `01-programming` folder. Write out two different paths that both correctly point to it, one absolute, and one relative, imagining your terminal is standing somewhere else inside that same folder.

> Work through this yourself, that's how terminal fluency actually forms. See the [section README](../README.md#the-golden-rule-zero-ai-code-generation) if you need the reminder.

---

## Checkpoint

Explain, in your own words:

1. What's the difference between an absolute path and a relative path?
2. Why does a relative path depend on your working directory, while an absolute path doesn't?
3. What do `.` and `..` each refer to?
4. Why can a path that works perfectly on your own computer fail on someone else's, or on a server?
