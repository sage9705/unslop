"""
Exercise: Write a File

Implement the two functions below. See README.md in this folder for
the full problem description.
"""

import os
import tempfile


def write_reorder_report(catalog, threshold, filepath):
    """Write a reorder report to filepath and return how many products
    were listed.

    catalog is a dict shaped like:
        {"Sugar": {"price": 12.75, "quantity": 3}, ...}

    The file should contain:
        a first line reading exactly: REORDER REPORT
        then one line per product with quantity at or below threshold,
        in the form: name,quantity
        sorted alphabetically by product name

    Calling this function again must replace the old report, not add
    to it.
    """
    raise NotImplementedError("TODO: implement write_reorder_report")


def append_note(filepath, note):
    """Add one line containing note onto the end of the file at
    filepath, without touching anything already in it."""
    raise NotImplementedError("TODO: implement append_note")


def self_check():
    catalog = {
        "Rice bag": {"price": 25.50, "quantity": 40},
        "Sugar": {"price": 12.75, "quantity": 3},
        "Cooking oil": {"price": 18.00, "quantity": 0},
        "Flour": {"price": 15.00, "quantity": 5},
        "Bread": {"price": 8.50, "quantity": 12},
    }

    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, "reorder_report.txt")

        count = write_reorder_report(catalog, 5, path)
        assert count == 3, f"expected 3 products listed, got {count}"

        with open(path) as file:
            lines = file.read().splitlines()
        assert lines == ["REORDER REPORT", "Cooking oil,0", "Flour,5", "Sugar,3"], f"got {lines}"

        write_reorder_report(catalog, 5, path)
        with open(path) as file:
            lines = file.read().splitlines()
        assert len(lines) == 4, "writing the report a second time should replace it, not add to it"

        append_note(path, "Call the supplier before Friday")
        with open(path) as file:
            lines = file.read().splitlines()
        assert len(lines) == 5, "append_note should add one line"
        assert lines[0] == "REORDER REPORT", "append_note must not erase what was already there"
        assert lines[-1] == "Call the supplier before Friday"

    print("All checks passed.")


if __name__ == "__main__":
    self_check()
