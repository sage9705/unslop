"""
This program is supposed to look up a product's price by name,
regardless of how the name happens to be capitalized.

Run this file. The checks below will tell you if something's wrong.
Do not rewrite this from scratch, find what's causing the wrong
answer and fix only that.
"""

CATALOG = {"Rice bag": 25.50, "Sugar": 12.75, "Cooking oil": 18.00}


def get_price(item_name):
    return CATALOG.get(item_name, 0)


print("Test 1:", get_price("Rice bag"))
assert get_price("Rice bag") == 25.50

print("Test 2:", get_price("rice bag"))
assert get_price("rice bag") == 25.50, "lookup should not be case sensitive"

print("Test 3:", get_price("SUGAR"))
assert get_price("SUGAR") == 12.75, "lookup should not be case sensitive"

print("All tests passed.")
