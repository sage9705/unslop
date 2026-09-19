"""
This program is supposed to build a separate "today's specials" list
from the shop's main inventory, without changing the main inventory
itself.

Run this file. The checks below will tell you if something's wrong.
Do not rewrite this from scratch, find the one line causing the wrong
answer and fix only that.
"""


def build_specials_list(main_inventory):
    specials = main_inventory
    specials.append("Discounted Bread")
    return specials


main_inventory = ["Rice bag", "Sugar", "Cooking oil"]
original_copy = list(main_inventory)

specials = build_specials_list(main_inventory)

print("Main inventory:", main_inventory)
print("Specials:", specials)

assert main_inventory == original_copy, "main_inventory should not change when building the specials list"
assert "Discounted Bread" in specials, "the specials list should still contain the new item"

print("All tests passed.")
