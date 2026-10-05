"""
Exercise: Analyze File Data

Implement the three functions below. See README.md in this folder for
the full problem description.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
SALES_PATH = os.path.join(HERE, "sales_log.txt")


def read_sales(filepath):
    """Read a sales log and return a tuple: (sales, skipped_count)

    sales is a list of (item, amount, payment) tuples, with amount as a
    float.

    Rules:
        the first line is a header, skip it and do not count it
        blank lines are ignored and not counted
        a line is malformed if it doesn't have exactly three fields, or
        its amount isn't a valid number. Skip malformed lines, and count
        each one in skipped_count.
    """
    raise NotImplementedError("TODO: implement read_sales")


def revenue_by_item(sales):
    """Return a dict of {item: total_revenue}, with each total rounded
    to 2 decimal places."""
    raise NotImplementedError("TODO: implement revenue_by_item")


def busiest_payment_method(sales):
    """Return the payment method used in the most sales."""
    raise NotImplementedError("TODO: implement busiest_payment_method")


def self_check():
    sales, skipped = read_sales(SALES_PATH)

    assert len(sales) == 7, f"expected 7 valid sales, got {len(sales)}"
    assert skipped == 2, f"expected 2 skipped lines, got {skipped}"
    assert sales[0] == ("Rice bag", 51.0, "cash")

    expected_revenue = {"Rice bag": 76.5, "Sugar": 76.5, "Cooking oil": 18.0, "Flour": 15.0}
    assert revenue_by_item(sales) == expected_revenue, f"got {revenue_by_item(sales)}"

    assert busiest_payment_method(sales) == "cash"

    print("All checks passed.")


if __name__ == "__main__":
    sales, skipped = read_sales(SALES_PATH)
    print(f"{len(sales)} valid sales, {skipped} skipped")
    print(revenue_by_item(sales))
    print(busiest_payment_method(sales))
    print()
    self_check()
