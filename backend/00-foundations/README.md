# 00 - Foundations

## Overview

Welcome to **00 - Foundations**.

This is where you build the basic programming skills, tools, and mental models you'll need for the rest of Unslop. The goal is to become comfortable enough with programming, the terminal, files, Git, and debugging that you can start learning backend development.

The philosophy is simple:

> **Learn what you need, build something with it, and deepen your understanding as you go.**

---

## Language and Curriculum Progression

Unslop uses **Python as the primary language** for Foundations and the early backend curriculum.

Python keeps the early stages focused on programming and backend concepts. Later, you'll learn **vanilla JavaScript** and **Node.js**. At that point, JavaScript becomes a second perspective on programming, runtimes, asynchronous execution, and backend development.

```text
FOUNDATIONS
Python

        ↓

EARLY BACKEND
Python
HTTP • Networking • APIs • Databases

        ↓

BACKEND FUNDAMENTALS
Authentication • Testing • Deployment
Performance • Security

        ↓

JAVASCRIPT
Vanilla JavaScript
Language fundamentals and browser-independent JavaScript

        ↓

NODE.JS
JavaScript outside the browser
Runtime • Files • Networking • Modules

        ↓

ASYNC JAVASCRIPT
Promises • Event Loop • Non-blocking I/O

        ↓

JAVASCRIPT BACKEND
APIs • Middleware • Async systems

        ↓

FUTURE FRONTEND
Browser • DOM • Fetch • Client-side state
```

The languages are tools for understanding the curriculum.

---

# The Learning Model

Unslop uses **progressive disclosure**.

You will not be asked to understand every layer of a computer, operating system, or network before you are allowed to build something.

Instead, you'll start with a simple problem and gradually discover the concepts underneath it.

For example:

```text
Build a server
       │
       ├── "What is localhost?"
       │
       ├── Learn localhost
       │
       ├── "What is a port?"
       │
       ├── Learn ports
       │
       └── Return to the server
```

Later, the same server gives you another question:

```text
Server
   │
   └── "How does another computer find me?"
                  │
                  ├── IP addresses
                  ├── DNS
                  └── networking
```

You learn the **next layer when you have enough context to understand it**.

---

# The Core Learning Loop

Every major topic follows roughly the same pattern:

```text
              ┌───────────────┐
              │     BUILD     │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   ENCOUNTER   │
              │    A PROBLEM  │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │  LEARN WHAT   │
              │  YOU NEED     │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │     RETURN    │
              │   & APPLY     │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ BREAK / DEBUG │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   EXPLAIN IT  │
              └───────────────┘
```

The goal is not simply to make the program work. The goal is to eventually understand **why it works**.

---

# Progressive Depth

Not every concept needs to be learned to the same depth.

A concept can be approached at four levels:

| Level                    | Goal                                |
| ------------------------ | ----------------------------------- |
| **Recognition**    | Know what the concept is            |
| **Mental Model**   | Understand why it exists            |
| **Operational**    | Observe and reason about it         |
| **Implementation** | Build or debug a simplified version |

For example, when networking is first introduced, you may only need to understand that:

> TCP provides a reliable way for two programs to exchange data.

Much later, you can revisit TCP and learn about connections, byte streams, retransmission, and ordering.

---

# Concept Debt

Sometimes you'll encounter something that is important but **not important yet**.

Instead of stopping the entire curriculum to learn everything about it, Unslop allows you to temporarily defer the deeper explanation.

For example:

> At this point, you only need to understand that HTTP uses a transport protocol. We will come back to TCP in greater depth later.

You can think of this as **concept debt**.

```text
KNOWN NOW
    │
    ├── CURRENTLY NEEDED
    │
    └── DEFERRED
            │
            └── REVISIT LATER
```

The important part is that the concept is not forgotten. It is revisited when you have enough context to understand it.

---

# Foundations Roadmap

```text
┌───────────────────────┐
│  01  Programming      │
│  Learn to write code  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  02  Terminal         │
│  Work with your       │
│  machine directly     │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  03  Files & Data     │
│  Work with and store  │
│  information          │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  04  Git              │
│  Track and manage     │
│  your work            │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  05  Debugging        │
│  Learn to investigate │
│  problems             │
└───────────┬───────────┘
            │
            ▼
      Foundations
       Checkpoint
            │
            ▼
       01-first-server
```

---

# 01 - Programming

### Purpose

Build enough programming fluency to reason about code.

### Topics

* variables and values
* types
* conditionals
* loops
* functions
* collections
* objects
* scope
* errors
* basic program structure
* problem decomposition

### Build

Small programs that gradually become more complex.

### Suggested pacing

**1–2 weeks**

### You should leave this section able to:

* write a small program from a blank file;
* explain basic control flow;
* break a problem into smaller functions;
* work with collections and structured data;
* make changes without needing generated code.

---

# 02 - Terminal

### Purpose

Become comfortable interacting with your computer without depending entirely on a graphical interface.

### Topics

* shell basics
* navigation
* files and directories
* paths
* running programs
* processes
* environment variables
* standard input/output/error
* basic command-line tools

### Suggested pacing

**3–5 days**

### You should leave this section able to:

* navigate a project from the terminal;
* create, move, copy, and remove files;
* run programs;
* inspect basic process information;
* understand basic command output.

You do not need to become a shell expert. You need to be comfortable using the tools you'll rely on later.

---

# 03 - Files & Data

### Purpose

Understand how programs represent, read, write, and persist information.

### Topics

* text files
* structured data
* JSON
* parsing
* serialization
* reading and writing files

### Core mental model

```text
Program Data
     │
     │ serialize
     ▼
   JSON/Text
     │
     │ store
     ▼
    File

File
     │
     │ parse
     ▼
Program Data
```

This idea will appear again later when working with HTTP requests and databases.

### Build

A small file-backed notes or task application.

### Suggested pacing

**3–5 days**

---

# 04 - Git

### Purpose

Learn the basic workflow used to manage software projects and their history.

### Topics

* repositories
* working tree
* staging
* commits
* diffs
* branches
* merging
* remotes

### Core mental model

```text
Your Changes
      │
      ▼
Working Directory
      │
      ▼
Staging Area
      │
      ▼
Commit History
      │
      ▼
Remote Repository
```

### Practice

You should:

1. create a repository;
2. make commits;
3. inspect changes;
4. create a branch;
5. merge branches;
6. resolve a basic conflict.

### Suggested pacing

**2–3 days**

Git then becomes part of every later project.

---

# 05 - Debugging

### Purpose

Learn how to investigate problems instead of guessing your way through them. Debugging is one of the most important skills in programming.

A working program is useful. A developer who can determine **why it stopped working** is much more valuable.

### Topics

* reading errors
* stack traces
* reproducing problems
* inspecting state
* logging
* breakpoints
* forming hypotheses
* verifying fixes

### The debugging process

```text
Something is wrong
        │
        ▼
   Reproduce it
        │
        ▼
  Describe what
  should happen
        │
        ▼
  Compare with what
    actually happens
        │
        ▼
  Form a hypothesis
        │
        ▼
    Gather evidence
        │
        ▼
       Test
        │
        ▼
      Fix it
        │
        ▼
    Verify the fix
```

### Suggested pacing

**4–7 days**

Later, this same method will be used to debug:

* HTTP requests;
* database queries;
* authentication;
* concurrency;
* production systems.

---

# Foundations Project

At the end of Foundations, combine everything into one small project.

## Example: Task Manager

A simple command-line application that can:

```text
┌─────────────────────────────┐
│        TASK MANAGER         │
├─────────────────────────────┤
│ add task                    │
│ list tasks                  │
│ complete task               │
│ delete task                 │
└─────────────────────────────┘
```

The application should:

* accept user input;
* validate input;
* manipulate application state;
* persist data to a file;
* handle invalid input;
* use Git;
* contain tests or verification steps;
* include at least one deliberate debugging exercise.

The goal is to prove that you can build and reason about a small program independently.

---

# Foundations Checkpoint

Before moving on, you should be able to answer questions such as:

### Programming

* What happens when a function is called?
* How does control flow move through a program?
* How would you break a problem into smaller pieces?

### Terminal

* What is a process?
* How do you find a running program?
* How do you navigate a project from the terminal?

### Files & Data

* What is serialization?
* What is parsing?
* Why might a program use JSON?

### Git

* What is a commit?
* What is a branch?
* What does a diff show?

### Debugging

* How do you reproduce a bug?
* What is a stack trace?
* How do you distinguish a symptom from a cause?
* Why should you form a hypothesis before changing code?

If you can answer these questions **and demonstrate the skills in practice**, move on.

---

# Suggested Pacing

The following assumes roughly **8–10 focused hours per week**.

| Section                    |       Suggested Time |
| -------------------------- | -------------------: |
| Programming                |           1–2 weeks |
| Terminal                   |            3–5 days |
| Files & Data               |            3–5 days |
| Git                        |            2–3 days |
| Debugging                  |            4–7 days |
| Final Project & Checkpoint |            1–2 days |
| **Total**            | **3–5 weeks** |

These are guidelines. Take longer when necessary. The purpose of this curriculum is to build durable understanding, not to finish as quickly as possible.

---

# Where Foundations Leads

Once you complete Foundations, you'll begin building actual backend systems.

The progression looks like this:

```text
┌─────────────────────────────┐
│        FOUNDATIONS          │
│ Programming • Tools        │
│ Files • Git • Debugging     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       FIRST SERVER          │
│ Client • Server • HTTP      │
│ Requests • Responses        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    SERVER & NETWORKING      │
│ Processes • Ports • IP      │
│ DNS • TCP • Sockets         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      BACKEND SYSTEMS        │
│ APIs • SQL • Databases      │
│ Auth • Security • Testing   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       PRODUCTION            │
│ Deployment • TLS            │
│ Observability • Performance │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     JAVASCRIPT + NODE       │
│ Language • Runtime • Async  │
│ Event Loop • Node Backend   │
└─────────────────────────────┘
```

Notice what is **not** happening here:

You are not spending the first few weeks studying every layer of computing before touching a server. You build the server first.

Then, when a question appears, you learn the system underneath it.

---

# The Bigger Picture

Eventually, Unslop should allow you to understand a system like this:

```text
                         INTERNET
                             │
                             ▼
                         DNS / IP
                             │
                             ▼
                        HTTP / TLS
                             │
                             ▼
                      ┌─────────────┐
                      │ Web Server  │
                      │ / Proxy     │
                      └──────┬──────┘
                             │
                             ▼
                      ┌─────────────┐
                      │ Application │
                      │   Server    │
                      └──────┬──────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
           PostgreSQL      Cache        Queue
                │                         │
                │                         ▼
                │                       Worker
                │
                ▼
              Data
```

You won't learn this diagram all at once. You'll build it piece by piece. Each time you encounter a new box, you'll have enough context to understand why it exists. Each time you revisit an old box, you'll understand it at a deeper level.

That is the approach behind Unslop:

> **Start simple. Build something useful. Follow your questions. Learn what is underneath. Revisit it later with a better mental model.**

The objective is to become capable of **figuring things out without needing someone else or an AI to do the thinking for you.**

You can skip foundations if you already have a working knowledge of basic programming concepts.
