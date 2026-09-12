# A shop wants to build a "clearance items" list based on its main inventory, without affecting the main inventory itself. Write a program that:

# 1. Creates a main inventory list of five products.
# 2. Attempts to build a clearance list using plain assignment, adds an item to it, and prints the main inventory to show the bug.
# 3. Fixes it using `.copy()`, adds an item to the clearance list, and prints the main inventory again to confirm it's now unaffected.

main_inventory = ["apple", "banana", "orange", "grape", "kiwi"]
clearance_items = main_inventory  # this creates a reference to the same list
clearance_items.append("mango")  # add an item to the clearance list
print("Main inventory after adding to clearance list:", main_inventory) 

# fix: use .copy() to create an independent copy
main_inventory = ["apple", "banana", "orange", "grape", "kiwi"]
clearance_items = main_inventory.copy()  # this creates an independent copy of the list
clearance_items.append("mango")  # add an item to the clearance list
print("Main inventory after adding to clearance list:", main_inventory) 
