def add_stock(catalog, item_name, price, quantity):
    catalog[item_name] = {"price": price, "quantity": quantity}
    return catalog


def get_price(catalog, item_name):
    if item_name not in catalog:
        return None
    return catalog[item_name]["price"]


def save_catalog(catalog, filename):
    with open(filename, "w") as catalog_file:
        for item_name, details in catalog.items():
            catalog_file.write(
                f"{item_name}|{details['price']}|{details['quantity']}\n"
            )


def load_catalog(filename):
    catalog = {}

    with open(filename) as catalog_file:
        for line in catalog_file:
            item_name, price, quantity = line.strip().split("|")
            catalog[item_name] = {
                "price": float(price),
                "quantity": int(quantity),
            }

    return catalog