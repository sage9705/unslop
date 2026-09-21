"""
Copy this file into 01-programming/ and run it from there:

    python verify.py
"""

import os


def self_check():
    if not os.path.exists("output.txt"):
        print("output.txt not found. Did you redirect the program's output into it?")
        return

    with open("output.txt") as f:
        content = f.read()

    if "CORNER SHOP RECEIPT" in content:
        print("output.txt contains the expected receipt.")
        print("All checks passed.")
    else:
        print("output.txt exists, but doesn't look like the Till Calculator actually ran.")


self_check()
