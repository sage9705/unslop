# Exercise: Running Programs

*`00-foundations/02-terminal/exercises/03-running-programs/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Task

Run the Till Calculator two different ways, and confirm both produce identical output.

**First run**, from `01-programming/` itself, without changing directories, using its path directly:

```bash
python examples/till-calculator/main.py > run_from_root.txt
```

**Second run**, after moving into its own folder:

```bash
cd examples/till-calculator
python main.py > ../../run_from_inside.txt
cd ../..
```

The `>` sends each run's normal output into a file instead of your screen, exactly the redirection covered in [`concepts/09-pipes-and-redirection.md`](../../concepts/09-pipes-and-redirection.md).

## Verifying Your Work

Copy `verify.py` from this folder into `01-programming/`, then run it from there:

```bash
python verify.py
```

It compares the two output files directly. Same program, same result, regardless of where you stood when you ran it, or which path you used to reach it.

## Concepts You'll Need

- [`concepts/04-paths.md`](../../concepts/04-paths.md)
- [`concepts/05-running-programs.md`](../../concepts/05-running-programs.md)

## Cleaning Up

Once both checks pass, delete `run_from_root.txt` and `run_from_inside.txt`.
