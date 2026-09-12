# Write a function `safe_price_lookup(catalog, item_name)` that:

# 1. Tries to look up `item_name` in the catalog dictionary.
# 2. Catches `KeyError` and returns `None` with a printed message, instead of crashing, if the item isn't found.
# 3. Returns the price normally if the item is found.

# Test it with an item that exists and one that doesn't, and confirm neither call crashes the program.

catalog = {"apple": 1.20, "banana": 0.80, "orange": 1.50}

def safe_price_lookup(catalog, item_name):
    try:
        return catalog[item_name]
    except KeyError:
        print(f"Item '{item_name}' not found in catalog.")
        return None

# testing with an item that exists
price = safe_price_lookup(catalog, "apple")
print(f"Price of apple: ${price:.2f}")

# testing with an item that doesn't exist
price = safe_price_lookup(catalog, "mango")
if price is None:
    print("Price of mango: not found")
else:
    print(f"Price of mango: ${price:.2f}")

