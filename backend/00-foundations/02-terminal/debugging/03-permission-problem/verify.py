"""
Run this from the same folder greet.py is in:

    python verify.py
"""

import os


def self_check():
    if not os.path.isfile("greet.py"):
        print("greet.py not found in this folder.")
        return

    executable = os.access("greet.py", os.X_OK)
    ran = os.path.isfile("ran.txt")

    print(f"[{'PASS' if executable else 'FAIL'}] greet.py is marked executable")
    print(f"[{'PASS' if ran else 'FAIL'}] greet.py actually ran directly and produced ran.txt")

    print()
    if executable and ran:
        print("All checks passed.")
    else:
        print("Not fixed yet, see above.")


self_check()
