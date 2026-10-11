"""
Run this from the folder that holds your import_prices.py:

    python verify.py

It checks the files your program produced, then launches your program
from a different directory, to confirm it still finds everything.
"""

import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PRICE_LIST = os.path.join(HERE, "price_list.json")
REJECTED = os.path.join(HERE, "rejected_lines.txt")
PROGRAM = os.path.join(HERE, "import_prices.py")

EXPECTED_PRICES = {
    "Matches": {"price": 1.5, "unit": "box"},
    "Sugar": {"price": 11.5, "unit": "kg"},
    "Rice bag": {"price": 24.0, "unit": "bag"},
    "Flour": {"price": 13.25, "unit": "kg"},
    "Tomato paste": {"price": 6.75, "unit": "tin"},
}
EXPECTED_REJECTED_NAMES = ["Cooking oil", "Bread", "Salt"]


def price_list_problem():
    if not os.path.exists(PRICE_LIST):
        return "price_list.json was not found"
    try:
        with open(PRICE_LIST, "r") as file:
            data = json.load(file)
    except ValueError:
        return "price_list.json is not valid JSON"
    if data != EXPECTED_PRICES:
        return f"price_list.json holds {data}, expected {EXPECTED_PRICES}"
    return None


def rejected_problem():
    if not os.path.exists(REJECTED):
        return "rejected_lines.txt was not found"
    with open(REJECTED, "r") as file:
        lines = [line for line in file.read().splitlines() if line.strip()]
    if len(lines) != len(EXPECTED_REJECTED_NAMES):
        return f"rejected_lines.txt has {len(lines)} lines, expected {len(EXPECTED_REJECTED_NAMES)}"
    for name in EXPECTED_REJECTED_NAMES:
        if not any(name in line for line in lines):
            return f"rejected_lines.txt has no line mentioning {name}"
    return None


def program_problem():
    if not os.path.exists(PROGRAM):
        return "import_prices.py was not found next to verify.py"
    result = subprocess.run(
        [sys.executable, PROGRAM],
        cwd=tempfile.gettempdir(),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        last_line = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else "no error text"
        return f"running from another directory failed: {last_line}"
    return price_list_problem() or rejected_problem()


def self_check():
    checks = [
        ("price_list.json has exactly the expected products", price_list_problem),
        ("rejected_lines.txt lists exactly the bad lines", rejected_problem),
        ("the program still works when launched from another directory", program_problem),
    ]

    all_passed = True
    for label, check in checks:
        problem = check()
        status = "PASS" if problem is None else "FAIL"
        print(f"[{status}] {label}")
        if problem is not None:
            print(f"       {problem}")
            all_passed = False

    print()
    if all_passed:
        print("All checks passed.")
    else:
        print("Some checks failed, see above.")


self_check()
