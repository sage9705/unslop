"""
Copy this file into 01-programming/ and run it from there:

    python verify.py
"""

import os


def count_notimplemented(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            path = os.path.join(root, filename)
            try:
                with open(path, "r", errors="ignore") as f:
                    for line in f:
                        if "NotImplementedError" in line:
                            count += 1
            except (IsADirectoryError, PermissionError):
                continue
    return count


def self_check():
    if not os.path.exists("remaining_todos.txt"):
        print("remaining_todos.txt not found. Did you redirect your grep search into it?")
        return

    with open("remaining_todos.txt") as f:
        lines = [line for line in f if line.strip()]

    expected = count_notimplemented("exercises")

    if len(lines) == expected:
        print(f"remaining_todos.txt contains {len(lines)} matches, matching an independent count.")
        print("All checks passed.")
    else:
        print(f"remaining_todos.txt contains {len(lines)} lines, but an independent count found {expected}.")


self_check()
