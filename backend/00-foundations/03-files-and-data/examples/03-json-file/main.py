"""
Catalog JSON Converter

Converts the shop's old catalog.txt format into catalog.json, and
reads it back to prove the round trip is exact. This is the reference
example for concepts 07 through 09 (structured data, JSON, and
serialization and deserialization).

Run it with:
    python main.py
"""

import json


def load_old_catalog(filepath):
    """Read the old comma-separated catalog.txt format into a dict."""
    catalog = {}
    with open(filepath, "r") as file:
        for line in file:
            item_name, price, quantity = line.strip().split(",")
            catalog[item_name] = {"price": float(price), "quantity": int(quantity)}
    return catalog


def save_catalog_json(catalog, filepath):
    """Save the catalog as JSON, replacing manual string building
    with json.dump."""
    with open(filepath, "w") as file:
        json.dump(catalog, file, indent=2)


def load_catalog_json(filepath):
    """Load the catalog back from JSON."""
    with open(filepath, "r") as file:
        return json.load(file)


if __name__ == "__main__":
    old_catalog = load_old_catalog("catalog.txt")
    print("Loaded from catalog.txt:")
    print(old_catalog)

    save_catalog_json(old_catalog, "catalog.json")
    print()
    print("Saved as catalog.json")

    reloaded_catalog = load_catalog_json("catalog.json")
    print()
    print("Loaded back from catalog.json:")
    print(reloaded_catalog)

    print()
    print(f"Round trip matches exactly: {reloaded_catalog == old_catalog}")
