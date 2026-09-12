# A supplier sends stock updates as raw text lines like `"Cooking oil, 18.00, 25"`. Write a program that:

# 1. Splits the line into item name, price, and quantity.
# 2. Strips whitespace from each part.
# 3. Converts price and quantity to the correct types.
# 4. Prints a clean, formatted line: item name, price to two decimal places, and quantity.

# Then test it with a messier line that has extra spaces in different places, and confirm your program still parses it correctly.

stock_update = "Cooking oil, 18.00, 25"
item_name, price_str, quantity_str = stock_update.split(", ")
item_name = item_name.strip()
price = float(price_str.strip())
quantity = int(quantity_str.strip())
print(f"{item_name}: ${price:.2f}, Quantity: {quantity}")

# test with a messier line
stock_update_messy = "  Cooking oil, 18.00, 25  "
item_name, price_str, quantity_str = stock_update_messy.split(", ")
item_name = item_name.strip()
price = float(price_str.strip())
quantity = int(quantity_str.strip())
print(f"{item_name}: ${price:.2f}, Quantity: {quantity}")

