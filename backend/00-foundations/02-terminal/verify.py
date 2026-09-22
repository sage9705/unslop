"""
Copy this file into 01-programming/ and run it from there:

    python verify.py
"""

import os


def count_py_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        count += sum(1 for f in files if f.endswith(".py"))
    return count


def count_readme_files(root):
    count = 0
    for dirpath, dirs, files in os.walk(root):
        count += sum(1 for f in files if f == "README.md")
    return count


def self_check():
    if not os.path.exists("audit_report.txt"):
        print("audit_report.txt not found. Did you complete step 1?")
        return

    with open("audit_report.txt") as f:
        content = f.read()
        lines = content.splitlines()

    checks_passed = True

    expected_py_count = count_py_files("examples")
    found_py_lines = sum(1 for line in lines if line.strip().endswith(".py"))
    check1 = found_py_lines == expected_py_count
    print(f"[{'PASS' if check1 else 'FAIL'}] found {found_py_lines} .py file lines in the report, expected {expected_py_count}")
    checks_passed = checks_passed and check1

    expected_readme_count = count_readme_files(".")
    check2 = str(expected_readme_count) in lines
    print(f"[{'PASS' if check2 else 'FAIL'}] report contains the README.md count ({expected_readme_count})")
    checks_passed = checks_passed and check2

    check3 = "DAILY TOTAL" in content
    print(f"[{'PASS' if check3 else 'FAIL'}] shop-inventory-tracker's output was appended")
    checks_passed = checks_passed and check3

    check4 = "Audit run by" in content
    print(f"[{'PASS' if check4 else 'FAIL'}] the auditor line was appended")
    checks_passed = checks_passed and check4

    print()
    if checks_passed:
        print("All checks passed.")
    else:
        print("Some checks failed, see above.")


self_check()
