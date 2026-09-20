# Exercise: Environment Variables

*`00-foundations/02-terminal/exercises/05-environment-variables/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Task

1. Copy `read_env.py` from this folder into an empty folder somewhere.
2. Set an environment variable called `SHOP_NAME` to any shop name you like, in the same terminal session:
   ```bash
   export SHOP_NAME="Corner Shop"
   ```
   On Windows PowerShell, the equivalent is:
   ```powershell
   $env:SHOP_NAME = "Corner Shop"
   ```
3. In that same terminal, run:
   ```bash
   python read_env.py
   ```
   It reads `SHOP_NAME` from its environment and writes a greeting into `greeting.txt`.

## Verifying Your Work

Copy `verify.py` into the same folder, and run it there:

```bash
python verify.py
```

It reads `greeting.txt` and checks whether it shows the shop name you set, or the fallback default, which tells you plainly whether `SHOP_NAME` was actually inherited by the Python process.

## Concepts You'll Need

- [`concepts/07-environment-variables.md`](../../concepts/07-environment-variables.md)

## Cleaning Up

Once the check passes, delete `read_env.py`, `verify.py`, and `greeting.txt`.
