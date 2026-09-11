# A shop needs to track its product list for the day. Write a program that:

# 1. Starts with a list of five product names already in stock.
# 2. Adds a new product that just arrived.
# 3. Removes a product that's been discontinued.
# 4. Prints the final list and how many products are on it.

# Then create a tuple representing one completed sale, `(item_name, price, quantity)`, and try to change one of its values to confirm it raises an error.


products = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]
products.append("Fig") # method to add a new product
products.remove("Cherries") # method to remove a discontinued product
print(f"Final product list: {products}")
print(f"Number of products: {len(products)}")

# create a tuple representing a completed sale
sale = ("Bananas", 1.5, 10)
print(f"Sale details: {sale}")

# try to change one of its values to confirm it raises an error
sale[1] = 2.0  # this will raise a TypeError because tuples are immutable
print(f"Updated sale details: {sale}")