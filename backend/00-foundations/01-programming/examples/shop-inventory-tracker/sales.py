def record_sale(catalog, item_name, quantity, daily_total):
    if item_name not in catalog:
        print(f"Sale failed: '{item_name}' is not in the catalog.")
        return daily_total, 0

    item = catalog[item_name]
    if quantity > item["quantity"]:
        print(
            f"Sale failed: Not enough stock for '{item_name}': "
            f"{item['quantity']} available, {quantity} requested."
        )
        return daily_total, 0

    sale_amount = item["price"] * quantity
    item["quantity"] -= quantity
    daily_total += sale_amount
    print(f"Sale recorded: {item_name} x{quantity} = {sale_amount:.2f}")
    return daily_total, sale_amount