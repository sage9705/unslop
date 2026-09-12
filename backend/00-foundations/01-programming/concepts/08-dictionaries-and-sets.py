# Build the price lookup for the Till Calculator project. Write a program that:

# 1. Creates a small product catalog dictionary with at least four items and their prices.
# 2. Looks up the price of an item that exists, and one that doesn't, using `.get()` with a default of `0`.
# 3. Updates the price of one item.
# 4. Builds a set of customer phone numbers from a list that contains at least one duplicate, and prints how many distinct customers that actually represents.

product_catalog = {
    "apple": 0.50, 
    "banana": 0.30,
    "orange": 0.80,
    "grape": 1.20
}   

# look up the price of an existing item
item_to_lookup = "banana"
price = product_catalog.get(item_to_lookup, 0)
print(f"The price of {item_to_lookup} is ${price:.2f}")

# look up the price of a non-existing item
item_to_lookup = "kiwi"
price = product_catalog.get(item_to_lookup, 0)
print(f"The price of {item_to_lookup} is ${price:.2f}")

# update the price of an item
product_catalog["banana"] = 0.35
print(f"The updated price of banana is ${product_catalog['banana']:.2f}")

# build a set of customer phone numbers
customer_phones = ["123-456-7890", "234-567-8901", "123-456-7890", "345-678-9012"]
distinct_customers = len(set(customer_phones))
print(f"Number of distinct customers: {distinct_customers}")