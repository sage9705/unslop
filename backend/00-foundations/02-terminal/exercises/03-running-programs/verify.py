"""
Copy this file into 01-programming/ and run it from there:

    python verify.py
"""

import filecmp
import os


def self_check():
    for filename in ("run_from_root.txt", "run_from_inside.txt"):
        if not os.path.exists(filename):
            print(f"{filename} not found. Did you redirect both runs correctly?")
            return

    identical = filecmp.cmp("run_from_root.txt", "run_from_inside.txt", shallow=False)

    if identical:
        print("Both runs produced identical output.")
        print("All checks passed.")
    else:
        print("The two output files differ. Something ran differently depending on where you stood.")


self_check()
