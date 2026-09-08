# Unslop

> Don't be a vibe coder forever.

With the convenience of generating code effortlessly and spinning up features on the fly using LLMs, it is easy to lose track of how software actually works under the hood. **Unslop** is a framework designed to help developers, esp. junior devs, break dependence on AI code generation and build genuine software engineering fundamentals from scratch.

**Unslop is intended to teach, not merely assign exercises.** The project is designed for novice developers who need to understand the fundamental concepts behind the software they are building before relying on abstractions, frameworks, or AI tools. Exercises are provided at the end of clear explanations of the underlying concepts, why they matter, how the pieces work together, and what is happening under the hood. The goal is not simply to complete a challenge or produce working code, but to build a mental model that allows a learner to explain, reason about, debug, and eventually implement the concept independently.

## Why I'm Making This

AI code generators create a dangerous illusion of competence. Relying on prompts without understanding lower level execution leaves you stranded the moment an AI hallucinates, introduces security bugs, or outputs architecture you cannot debug. I fell into this early stage vibe coding trap myself.

What happens when a developer stops doing the cognitive work of programming before they have developed the ability to do it themselves? They don't become a better developer. They become dependent on AI to write even the most basic code. It fosters lack of geniune programming skills, self-doubt, insecurity, and ultimately leads to imposter syndrome.

A developer can generate an API without understanding HTTP. They can use an ORM without understanding SQL. They can implement authentication without understanding sessions, cookies, tokens, or cryptography. They can write asynchronous code without understanding the event loop. They can fix an error by pasting it into an AI without learning how to diagnose the failure. You get the point.

The code may work. The developer may even look productive. But remove the AI and the underlying capability can disappear.

This project exists to break that dependency. The goal is to build developers who understand the systems they work with, can reason about problems independently, and can take responsibility for the software they ship.

## The Cognitive Case for Learning Without AI

Software engineering is a cognitive discipline. Developers need to be able to decompose problems, reason about control flow, understand data structures, trace execution, design algorithms, read unfamiliar code, debug failures, reason about databases and networks, understand language semantics, and make architectural tradeoffs.

You cannot acquire those abilities simply by looking at "correct code". They are developed through **doing the cognitive work yourself**.

When a junior developer routinely asks an AI to generate the implementation, explain the error, choose the architecture, write the SQL, construct the tests, fix the bug, and explain the resulting code, they can produce working software without necessarily developing the underlying competence required to produce or maintain that software independently.

That is the danger of **cognitive outsourcing**.

Repeatedly outsourcing the thinking involved in a skill can reduce the amount of active cognitive engagement used to practice that skill. Research on generative AI and critical thinking has found associations between confidence in AI and lower reported critical thinking effort.

For software development, that distinction matters. Designing a solution, recalling concepts, tracing execution, debugging failures, reading documentation, and constructing code yourself are part of developing the mental models that makes you an effective engineer.

This project therefore treats **manual implementation as deliberate cognitive training**. AI can be useful later as an engineering tool, but developers should first develop enough independent capability that AI is an accelerator rather than a prerequisite.

## Research and Further Reading

- [The Impact of Generative AI on Critical Thinking - Microsoft Research / CHI 2025](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/) - A study of 319 knowledge workers that found higher confidence in GenAI was associated with less reported critical thinking effort. It also describes how AI assisted work can shift critical thinking toward verification, response integration, and task stewardship.
- [The Impact of Generative AI on Critical Thinking - CHI 2025 paper / DOI](https://doi.org/10.1145/3706598.3713778) - The peer-reviewed paper behind the Microsoft Research study.
- [Tool, Tutor, or Crutch? - International Journal of STEM Education](https://link.springer.com/article/10.1186/s40594-025-00592-w) - Research examining AI use in programming education and the tension between AI assisted task performance, cognitive offloading, learning, and independent capability.
- [Less Stress, Better Scores, Same Learning - Computers &amp; Education: Artificial Intelligence](https://www.sciencedirect.com/science/article/pii/S2666920X25001778) - A randomized study of 275 introductory programming students that found unrestricted ChatGPT assistance improved exercise performance but did not produce greater gains in knowledge or code comprehension than the no-AI condition.
- [Generative AI Dependency on Programming Among University Students - BMC Psychology](https://link.springer.com/article/10.1186/s40359-026-05011-5) - Examines dependency on generative AI for programming and the outsourcing of processes such as problem analysis, algorithm design, debugging, logical reasoning, and code comprehension.
- [Rethinking AI in Knowledge Work: From Assistant to Tool for Thought - Microsoft Research](https://www.microsoft.com/en-us/research/articles/rethinking-ai-in-knowledge-work-from-assistant-to-tool-for-thought/) - Discusses the broader problem of "outsourced thinking" and how generative AI can change the amount and type of cognitive effort people apply to knowledge work.
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity - METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) - A randomized controlled trial involving 16 experienced open-source developers and 246 real tasks. In that particular setting, developers using early 2025 AI coding tools took 19% longer on average, despite expecting AI to make them faster.
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity - arXiv](https://arxiv.org/abs/2507.09089) - The research paper and methodology for the METR developer productivity experiment.

These studies support a more important concern: **if the cognitive work required to develop a skill is continually outsourced, the learner may get better at operating the tool without developing the underlying skill to the same degree.**

## The Vibe Coder Problem

AI makes it possible to appear much more capable than you actually are.

A developer can generate a backend without understanding HTTP. They can ship database code without understanding indexes or query plans. They can implement authentication without understanding the security model. They can deploy an application without understanding processes, ports, networking, or memory. They can fix bugs without learning how to diagnose them.

This creates a dangerous gap between **producing software** and **understanding software**.

That gap is especially dangerous for junior developers because the early stages of a career are when foundational mental models are being built. If AI performs the reasoning before those models are developed, a developer can accumulate experience with shipping code while failing to accumulate the knowledge required to understand, debug, secure, and extend that code independently.

That is how you end up with developers who can make things work but cannot explain why they work. We can see the prevalence of such developers in the current SWE ecosystem.

**Unslop exists to close that gap.**

## The Principle

**Do not outsource a skill you are still trying to develop.**

If you are learning HTTP, write the HTTP server.

If you are learning SQL, write the queries.

If you are learning authentication, implement the mechanics yourself.

If you are learning debugging, debug the program yourself.

If you are learning algorithms, solve the problem yourself.

If you are learning a programming language, actually learn the language.

The point is not to memorize every obscure API or reinvent every production library. The point is to develop sufficiently strong mental models that you can:

- write meaningful code without an AI generating it for you;
- read and understand unfamiliar code;
- debug without immediately asking a model for the answer;
- recognize when generated code is wrong;
- identify security and architectural problems;
- understand the abstractions provided by frameworks and libraries;
- learn new languages and technologies from documentation;
- reason about tradeoffs instead of blindly accepting generated decisions; and
- take responsibility for the software you ship.

## The Golden Rule

**Zero AI Code Generation.**

No Copilot, no ChatGPT code blocks, no Cursor auto-complete. Every line of code, database query, and route handler must be written, analyzed, and debugged by your head and hands.

This is a **training constraint**, not a claim that AI should never be used professionally. The objective is to develop enough independent competence that AI becomes an optional accelerator rather than a prerequisite for writing and understanding software.

## Scope & Focus

We start deep in the **Backend**.

Why backend first? Because backend development forces you to confront core engineering concepts head-on. Unslop will teach these concepts explicitly rather than treating the repository as a collection of exercises. Learners should understand what is happening, why it is happening, and how the pieces fit together before being asked to implement them. Backend development forces you to confront core engineering concepts head-on: data flow, memory, network protocols, databases, authorization, and algorithmic complexity. Once you understand how systems process, persist, and protect data, frontend concepts become significantly easier to grasp. Well this is my opinion anyway.

- **Phase 1: Backend Core (Current Focus)**

  - Raw HTTP servers, REST APIs, and authentication logic from scratch.
  - SQL and database query optimization without leaning on heavy ORM abstractions.
  - Data structures, system design basics, and proper error handling.
  - Terminal navigation, unit testing, and debugging with native tools.
- **Phase 2: Frontend Fundamentals (Future Expansion)**

  - Vanilla JavaScript, DOM manipulation, and asynchronous browser behavior.
  - Core state management from first principles.
  - CSS layout mechanics without heavy framework crutches.

## Key Objectives

- **Write Code from Scratch:** Construct logic from a blank file to build fluency with syntax, patterns, control flow, and problem solving.
- **Master System Mechanics:** Understand how servers process requests, query databases, manage memory, and communicate over networks without AI safety nets.
- **Develop Debugging Instincts:** Learn to navigate terminal error logs, trace stack traces, reproduce failures, inspect state, and read official documentation directly.
- **Build Cognitive Independence:** Practice solving technical problems without immediately delegating the reasoning process to a generative model.
- **Understand Abstractions:** Learn the underlying mechanics before relying on frameworks, ORMs, libraries, or AI coding agents that abstract those mechanics away.
- **Build Professional Competence:** Develop enough command of your language, runtime, tools, and core framework concepts to make engineering decisions rather than merely accepting generated ones.

## AI Should Be an Accelerator, Not Your Brain

**Unslop is not anti-AI.**

AI is an extremely powerful engineering tool. Experienced developers can use it to accelerate implementation, explore alternatives, automate repetitive work, generate tests, investigate unfamiliar APIs, and perform many other useful tasks.

But there is an important difference between:

> "AI makes me faster because I already understand what I'm doing."

and:

> "I can only make progress because AI tells me what to do."

The first is leverage. The second, dependency.

**Build the competence first. Add the leverage afterward.**

The purpose of this project is to make sure that when a developer eventually turns AI back on, they are still the engineer in the driver's seat and not a vibe coder who barely knows what an HTTP Request is.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sage9705/unslop.git
   cd unslop
   ```
2. **Disable AI Assistant Extensions:**

   Turn off GitHub Copilot, Cursor AI, Supermaven, or any auto-complete plugins in your editor before working on any exercise.
3. **Start a Backend Exercise:**

   Navigate to the `/backend` directory and select your first challenge.

## License

This project is open-source and available under the [MIT License](LICENSE).
