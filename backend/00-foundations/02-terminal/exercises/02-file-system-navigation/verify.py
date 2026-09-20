"""
Copy this file into 01-programming/ and run it from there:

    python verify.py
"""

import os


def self_check():
    checks = [
        ("field-notes/ exists", os.path.isdir("field-notes")),
        ("field-notes/day1.md exists", os.path.isfile("field-notes/day1.md")),
        ("field-notes/day2.md exists", os.path.isfile("field-notes/day2.md")),
        ("field-notes/day3-final.md exists", os.path.isfile("field-notes/day3-final.md")),
        ("field-notes/day3.md no longer exists (renamed, not copied)", not os.path.isfile("field-notes/day3.md")),
    ]

    all_passed = True
    for label, passed in checks:
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {label}")
        if not passed:
            all_passed = False

    print()
    if all_passed:
        print("All checks passed.")
    else:
        print("Some checks failed, see above.")


self_check()
