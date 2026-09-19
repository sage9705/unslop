"""
This program is supposed to add up a full week of daily sales figures
into one running total.

Run this file. The checks below will tell you if something's wrong.
Do not rewrite this from scratch, find the one line causing the wrong
answer and fix only that.
"""


def calculate_weekly_total(daily_sales):
    for amount in daily_sales:
        total = 0
        total = total + amount
    return total


daily_sales = [100, 200, 150]
print("Test:", calculate_weekly_total(daily_sales))
assert calculate_weekly_total(daily_sales) == 450, "the weekly total should be the sum of every day, not just the last one"

print("All tests passed.")
