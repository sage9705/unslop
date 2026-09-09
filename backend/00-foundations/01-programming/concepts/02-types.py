# A customer's order comes in from an online form, which means every field arrives as text. Write a program that:

# 1. Stores a unit price as text, `"15.75"`, exactly as it would arrive from a form.
# 2. Converts it to a float.
# 3. Stores a quantity as text, `"4"`, and converts it to an int.
# 4. Calculates and prints the total cost, along with its type.

# Then try breaking it on purpose. Store the price as ​"fifteen seventy five"​ instead and see what error you get.

unit_price = "8.5"
unit_price = float(unit_price)

quantity = "53"
quantity = int(quantity)

total_cost = unit_price * quantity
print("Total cost is", total_cost)
print("The type of total_cost is", type(total_cost))


