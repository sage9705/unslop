# A shop tracks stock quantities for its products. Write a program that:

# 1. Loops through a list of `(product_name, quantity)` pairs.
# 2. Prints `"REORDER: {product_name}"` for anything at or below a threshold of 5.
# 3. Counts and prints how many products need reordering in total.


stock_list = [
    ("Milk", 10),           
    ("Bread", 3),           
    ("Eggs", 12),           
    ("Cheese", 1),          
    ("Yogurt", 8)           
]

reorder_threshold = 5
reorder_count = 0

for product_name, quantity in stock_list:
    if quantity <= reorder_threshold:
        print(f"REORDER: {product_name}")
        reorder_count += 1

print(f"Total products needing reordering: {reorder_count}")