"""
Validated Catalog Store

Loads a JSON-backed catalog, attempts to add several products, some
valid and some deliberately not, and saves only what actually passed
validation. Run it twice in a row to see the store persist between
runs.

Run it with:
    python main.py
"""

import catalog_store

STORE_PATH = "catalog_store.json"


def main():
    catalog = catalog_store.load_store(STORE_PATH)
    print(f"Loaded {len(catalog)} existing product(s) from {STORE_PATH}")

    new_products = [
        ("Rice bag", 25.50, 40),
        ("Sugar", 12.75, 30),
        ("Cooking oil", -18.00, 15),     # invalid: negative price
        ("", 10.00, 5),                  # invalid: empty name
        ("Flour", 15.00, -3),            # invalid: negative quantity
        ("Bread", 8.50, 12),
    ]

    for name, price, quantity in new_products:
        try:
            catalog_store.add_product(catalog, name, price, quantity)
            print(f"Added: {name}")
        except ValueError as error:
            print(f"Rejected: {error}")

    catalog_store.save_store(catalog, STORE_PATH)
    print()
    print(f"Saved {len(catalog)} product(s) to {STORE_PATH}")


if __name__ == "__main__":
    main()
