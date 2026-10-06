"""
Exercise: Work With JSON

Implement the four functions below. See README.md in this folder for
the full problem description.
"""

import json
import os
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(HERE, "shop_config.json")
CATALOG_PATH = os.path.join(HERE, "catalog.json")


def load_json(filepath):
    """Read the JSON file at filepath and return it as Python data."""
    raise NotImplementedError("TODO: implement load_json")


def save_json(data, filepath):
    """Write data to filepath as JSON, indented with 2 spaces so a
    person can read it."""
    raise NotImplementedError("TODO: implement save_json")


def apply_price_increase(catalog, percent):
    """Return a NEW catalog where every product's price is raised by
    percent, rounded to 2 decimal places. Quantities stay the same.

    The catalog passed in must be left completely unchanged.

    Example: a price of 10.0 with percent=20 becomes 12.0
    """
    raise NotImplementedError("TODO: implement apply_price_increase")


def merge_catalogs(base, updates):
    """Return a NEW catalog containing everything in base, with every
    product in updates added, or replacing the base version if the
    product already exists.

    The base catalog passed in must be left completely unchanged.
    """
    raise NotImplementedError("TODO: implement merge_catalogs")


def self_check():
    config = load_json(CONFIG_PATH)
    assert config["shop_name"] == "Corner Shop"
    assert config["reorder_threshold"] == 5
    assert config["tax_rate"] == 0.125

    catalog = load_json(CATALOG_PATH)
    assert catalog["Sugar"] == {"price": 12.75, "quantity": 30}

    raised = apply_price_increase(catalog, 20)
    expected = {
        "Rice bag": {"price": 30.6, "quantity": 40},
        "Sugar": {"price": 15.3, "quantity": 30},
        "Cooking oil": {"price": 21.6, "quantity": 15},
    }
    assert raised == expected, f"got {raised}"
    assert catalog["Rice bag"]["price"] == 25.5, "apply_price_increase must not change the original catalog"

    updates = {
        "Sugar": {"price": 13.5, "quantity": 30},
        "Flour": {"price": 15.0, "quantity": 22},
    }
    merged = merge_catalogs(catalog, updates)
    assert merged["Sugar"]["price"] == 13.5, "an updated product should replace the old one"
    assert merged["Flour"] == {"price": 15.0, "quantity": 22}
    assert merged["Rice bag"] == {"price": 25.5, "quantity": 40}
    assert "Flour" not in catalog, "merge_catalogs must not change the base catalog"
    assert catalog["Sugar"]["price"] == 12.75, "merge_catalogs must not change the base catalog"

    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, "out.json")
        save_json(merged, path)
        assert load_json(path) == merged, "a saved file should load back identical"
        with open(path) as file:
            text = file.read()
        assert text.startswith('{\n  "'), "save_json should indent with 2 spaces"

    print("All checks passed.")


if __name__ == "__main__":
    self_check()
