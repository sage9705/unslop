# Unslop Backend

## What You're Getting Into

This is a guided journey into **understanding what is actually happening when a backend system runs**. It is not a collection of tutorials designed to help you memorize framework commands or copy working API code. You will build things. Then, when something doesn't make sense, you'll stop and investigate why.

The goal is to move beyond:

> "I know how to use this."

toward:

> "I know what problem this solves, what is happening underneath it, and how to reason about it when it breaks."

That's the kind of understanding that makes it possible to keep learning long after a particular framework or technology becomes outdated.

## What You'll Build

You won't be handed a giant backend project on day one. You'll start small. You'll write programs, create a simple server, make requests, return responses, and gradually turn that small application into something that looks much more like a real backend system.

As you progress, the same growing application will become a place to explore ideas such as:

- HTTP and APIs
- servers, processes, ports, and localhost
- IP addresses, DNS, and networking
- databases and SQL
- application architecture
- authentication and authorization
- security
- asynchronous programming and concurrency
- testing and debugging
- performance
- caching and background jobs
- observability
- Docker and deployment
- TLS and reverse proxies

You don't need to understand all of that before you begin. In fact, **you're not supposed to.**

## The Way You'll Learn

Unslop follows a dynamic cycle: start with a working program, hit a question, pivot sideways to learn the mechanism, then return to build and break it.

```text
                  ┌──────────────────────────────┐
                  │          1. BUILD            │
                  │   Write real, working code   │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │    2. ENCOUNTER A PROBLEM    │
                  │  "Why does localhost work?"  │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                     ─── PIVOT UNDERNEATH ───
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │     3. LEARN THE CONCEPT     │
                  │   Processes, ports & sockets │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                    ─── RETURN TO APPLICATION ───
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │       4. USE & BREAK IT      │
                  │ Port conflicts, kill signals │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │      5. DEBUG & EXPLAIN      │
                  │ Reason through the failure   │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │   6. GO DEEPER (when ready)  │
                  │ Revisit at the network layer │
                  └──────────────────────────────┘
```

So instead of being told, "Today you are going to learn ports," you might first build a server and wonder:

> "Why does `localhost:3000` work?"

That question becomes the reason to learn about processes and ports:

```text
       APPLICATION TRACK                         SYSTEMS UNDER THE HOOD
┌─────────────────────────────┐
│   Build a simple HTTP API   │
│   server.listen(3000)       │
└──────────────┬──────────────┘
               │
               │  "Why does :3000 work?"
               ▼
        [ PIVOT OUT ] ───────────────────────────▶ ┌───────────────────────────┐
                                                   │     OPERATING SYSTEM      │
                                                   │ Processes (PIDs), ports,  │
                                                   │ and socket table bindings │
                                                   └─────────────┬─────────────┘
                                                                 │
                                                    [ RETURN ]   │
               ┌─────────────────────────────────────────────────┘
               ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ DEEPER MENTAL MODEL                                                          │
│ You now understand what server.listen(3000) actually asks the OS to do:      │
│ create socket → bind(:3000) → listen() → accept incoming connections         │
└──────────────────────────────────────────────────────────────────────────────┘
```

Later, another question might lead you into IP addresses, DNS, TCP, sockets, or TLS. The deeper material **is being introduced when you have a reason to care about it.**


## You Will Not Learn Everything at Once

Backend development has a lot of layers between the user's click and the byte written to disk:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ CLIENT                                                                 │
│   Browser / Mobile App / curl                                          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │  DNS Lookup (domain → IP)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ NETWORK & TRANSPORT                                                    │
│   TCP Stream (reliable bytes) + TLS (encryption & trust)               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │  HTTP/1.1 or HTTP/2 Wire Request
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ REVERSE PROXY / GATEWAY                                                │
│   Nginx / Caddy ─ TLS Termination, Routing, Port Forwarding            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │  Local Port Binding (:3000)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ APPLICATION RUNTIME                                                    │
│   Node.js Process (Event Loop, Memory Heap)                            │
│     ├── Router & Middleware (Auth, Validation, Headers)                │
│     └── Handlers & Business Logic                                      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │  SQL via TCP Connection (:5432)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ DATABASE & PERSISTENCE                                                 │
│   PostgreSQL Engine ─ Query Planner, B-Trees, Disk Storage             │
└────────────────────────────────────────────────────────────────────────┘
```

Early on, you may only need to understand a few of those layers. That's intentional. Unslop teaches the **minimum necessary abstraction first**, then revisits important ideas later at greater depth.

You may sometimes hear:

> "You don't need to understand this part yet. We'll come back to it."

It's part of the learning journey. Learning to work responsibly with incomplete knowledge is itself an important engineering skill.

## Expect to Get Stuck

You should expect things to break. A server won't start. A request will return an unexpected status code. A database query will behave differently from what you expected. Two requests will interfere with each other. An application that worked locally won't work after deployment. Those moments are not interruptions to the learning process. **They are the learning process.**

You'll be encouraged to investigate problems rather than immediately reach for a solution. The aim is to develop the habit of reasoning through failures:

```text
                  ┌──────────────────────────────┐
                  │       1. THE ANOMALY         │
                  │   What did I actually see?   │
                  │ (500 Error / Connection Ref) │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │       2. THE EXPECTATION     │
                  │  What was supposed to happen?│
                  │  (200 OK + JSON payload)     │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │      3. GATHER EVIDENCE      │
                  │  Check status, logs, headers │
                  │  Inspect process state & port│
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │     4. ISOLATE BOUNDARY      │
                  │  Network? OS? Application?   │
                  │  Route handler? Database?    │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │      5. TEST HYPOTHESIS      │
                  │  Make a targeted fix and     │
                  │  confirm WHY it worked       │
                  └──────────────────────────────┘
```

Over time, debugging should become less like guessing and more like reasoning.

## This Is More Than Learning to Code

You will certainly write code. Code is the vehicle.

You will also learn to:

- form mental models
- ask better technical questions
- inspect systems
- read errors and logs
- use tools to gather evidence
- understand trade-offs
- recognize the boundaries of your knowledge
- explain systems in your own words
- investigate unfamiliar abstractions independently

The curriculum is designed around the idea that **working code is not enough**. If an AI, framework, library, or tutorial gives you code that works but you cannot explain why it works, there is still something left to learn.

## One Growing System

Rather than treating every topic as an isolated exercise, the backend curriculum is designed around a growing application.

It starts simple and gradually acquires more capabilities, expanding across four architectural phases:

```text
STAGE 1: THE LOCAL PROCESS
┌─────────────────────────┐
│     First Server        │ ◀── Local HTTP requests (:3000)
│   (in-memory state)     │
└─────────────────────────┘

STAGE 2: ADDING PERSISTENCE
┌─────────────────────────┐         TCP (:5432)          ┌─────────────────────────┐
│       API Server        │ ───────────────────────────▶ │       PostgreSQL        │
│   (routes, validation)  │ ◀─────────────────────────── │  (tables, foreign keys) │
└─────────────────────────┘                              └─────────────────────────┘

STAGE 3: BACKGROUND WORK & CACHE
                                  ┌─────────────────────────┐
                            ┌───▶ │       PostgreSQL        │ (relational records)
                            │     └─────────────────────────┘
┌────────────────────────┐  │     ┌─────────────────────────┐
│       API Server       ├──┼───▶ │       Redis Cache       │ (fast session lookups)
│  (auth, rate limiting) │  │     └─────────────────────────┘
└────────────────────────┘  │     ┌─────────────────────────┐
                            └───▶ │       Job Queue         │
                                  └────────────┬────────────┘
                                               │ (async jobs)
                                               ▼
                                  ┌─────────────────────────┐
                                  │      Worker Process     │ (emails, file export)
                                  └─────────────────────────┘

STAGE 4: THE COMPLETE PRODUCTION TOPOLOGY
                         [ Client Request ]
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │ DNS → IP Resolution   │
                     └───────────┬───────────┘
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │ TLS Termination &     │
                     │ Reverse Proxy (Nginx) │
                     └───────────┬───────────┘
                                 │ :3000 (Internal)
                                 ▼
                     ┌───────────────────────┐
                     │ Application Process   │
                     │ (Node.js Event Loop)  │
                     └─────┬───────────┬─────┘
            SQL (:5432)    │           │   Cache / Jobs (:6379)
         ┌─────────────────┘           └─────────────────┐
         ▼                                               ▼
┌──────────────────┐                            ┌──────────────────┐
│    PostgreSQL    │                            │      Redis       │
│  (Disk Storage)  │                            │ (Cache & Queues) │
└──────────────────┘                            └────────┬─────────┘
                                                         │
                                                         ▼
                                                ┌──────────────────┐
                                                │   Async Worker   │
                                                └──────────────────┘
```

The application becomes the object you use to understand the systems around it. Concepts should connect to something you've already built rather than existing only as isolated definitions.

## Don't Worry About the Entire Roadmap

There is a lot ahead. You will encounter unfamiliar terminology. Some topics will feel surprisingly easy. Others will take time. That's normal. 

You are not expected to memorize the entire backend ecosystem.

The target is something more useful:

> **You should become capable of understanding the next thing you encounter.**

By the end, the important question isn't whether you remember every command or framework API.

It's whether you can look at a backend system, identify its major boundaries, and start reasoning about what is happening when something goes wrong.

## What Success Looks Like

Success isn't:

> "I finished all the exercises."

It's closer to this:

You encounter an unfamiliar backend system. Something breaks. Instead of immediately asking someone or an AI to tell you what to change, you can begin investigating.

You know what questions to ask.

You know what evidence to collect.

You have enough understanding of the underlying system to narrow down the problem.

And when you eventually find the answer, you understand **why** it was the answer.

For example, when a production deployment returns a `502 Bad Gateway`, you won't blindly prompt an AI with *"Why is my API returning 502?"* Instead, you isolate the failure boundary by boundary:

```text
               An API returns 502 Bad Gateway
                             │
                             ▼
┌────────────────────────────────────────────────────────┐
│ 1. Did the reverse proxy receive the request?          │
│    Inspect Nginx access & error logs                   │
└────────────────────────────┬───────────────────────────┘
                             ▼
┌────────────────────────────────────────────────────────┐
│ 2. Is the backend process running?                     │
│    Check systemd / ps / process monitor                │
└────────────────────────────┬───────────────────────────┘
                             ▼
┌────────────────────────────────────────────────────────┐
│ 3. Is it bound to the expected local port?             │
│    Check socket bindings with ss or lsof               │
└────────────────────────────┬───────────────────────────┘
                             ▼
┌────────────────────────────────────────────────────────┐
│ 4. What do the application logs say?                   │
│    Look for uncaught exceptions or startup crashes     │
└────────────────────────────┬───────────────────────────┘
                             ▼
┌────────────────────────────────────────────────────────┐
│ 5. Is an upstream dependency failing?                  │
│    Check PostgreSQL connection pool & socket timeouts  │
└────────────────────────────────────────────────────────┘
```

That is the kind of backend developer Unslop is trying to help you become.

---

### Start Small

Don't worry about the whole journey.

Open the first lesson.

Build the first thing.

Be curious when something doesn't make sense.

**The deeper layers will reveal themselves when you have a reason to understand them.**
