"""
Stock Reorder Alert

Scans a shop's inventory and flags anything that needs reordering.
This is the reference example for concepts 04 and 05 (conditionals and
loops), using the dictionary lookups introduced in concept 08 instead
of scanning a list, for the reasons covered in
problem-solving/05-complexity-basics.md.

Run it with:
    python main.py
"""


def check_stock(inventory, threshold):
    """Loop through the inventory and report items needing reorder.

    inventory is a dict of {product_name: quantity}.
    Returns a list of product names that need reordering.
    """
    reorder_list = []

    for product_name, quantity in inventory.items():
        if quantity == 0:
            print(f"OUT OF STOCK:  {product_name}")
            reorder_list.append(product_name)
        elif quantity <= threshold:
            print(f"REORDER:       {product_name} ({quantity} left)")
            reorder_list.append(product_name)

    return reorder_list


if __name__ == "__main__":
    inventory = {
        "Rice bag": 12,
        "Sugar": 3,
        "Cooking oil": 0,
        "Flour": 20,
        "Bread": 4,
    }

    threshold = 5

    reorder_list = check_stock(inventory, threshold)

    print()
    if reorder_list:
        print(f"{len(reorder_list)} product(s) need attention: {', '.join(reorder_list)}")
    else:
        print("Everything is well stocked.")
