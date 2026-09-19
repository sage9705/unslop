"""
This program is supposed to apply whichever discount rate benefits the
customer more, the loyalty rate or the bulk rate, never both.

Run this file. The checks below will tell you if something's wrong.
Do not rewrite this from scratch, find the one thing causing the wrong
answer and fix only that.
"""


def calculate_final_price(price, quantity, loyalty_rate, bulk_rate):
    subtotal = price * quantity
    best_rate = min(loyalty_rate, bulk_rate)
    return subtotal * (1 - best_rate)


print("Test 1:", calculate_final_price(10, 20, 0.05, 0.10))
assert round(calculate_final_price(10, 20, 0.05, 0.10), 2) == 180.0, "the larger discount rate should apply"

print("Test 2:", calculate_final_price(5, 3, 0.10, 0.02))
assert round(calculate_final_price(5, 3, 0.10, 0.02), 2) == 13.5, "the larger discount rate should apply"

print("All tests passed.")
