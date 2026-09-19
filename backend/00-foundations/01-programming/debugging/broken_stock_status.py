"""
This program is supposed to classify a product's stock level into one
of three statuses: "Out of Stock", "Reorder Now", or "Well Stocked".

A quantity exactly equal to the threshold should count as needing a
reorder, not as well stocked, the shop would rather reorder a little
early than run out entirely.

Run this file. The checks below will tell you if something's wrong.
Do not rewrite this from scratch, find the one line causing the wrong
answer and fix only that.
"""


def get_status(quantity, threshold=5):
    if quantity == 0:
        return "Out of Stock"
    elif quantity < threshold:
        return "Reorder Now"
    else:
        return "Well Stocked"


print("Test 1:", get_status(0))
assert get_status(0) == "Out of Stock"

print("Test 2:", get_status(3))
assert get_status(3) == "Reorder Now"

print("Test 3:", get_status(5))
assert get_status(5) == "Reorder Now"

print("Test 4:", get_status(10))
assert get_status(10) == "Well Stocked"

print("All tests passed.")
