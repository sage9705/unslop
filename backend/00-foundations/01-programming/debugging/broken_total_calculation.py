"""
This program is supposed to add up a list of quantities that arrived
exactly the way they would from a web form, as text, not numbers.

Run this file. The checks below will tell you if something's wrong.
Do not rewrite this from scratch, find what's causing the crash and
fix only that.
"""


def total_quantity(quantity_list):
    total = 0
    for quantity in quantity_list:
        total = total + quantity
    return total


print("Test:", total_quantity(["10", "5", "20"]))
assert total_quantity(["10", "5", "20"]) == 35

print("All tests passed.")
