"""
Shop Inventory and Sales Tracker

The capstone example for this folder. Ties together concepts 01
through 13: a running catalog, a day of sales recorded against it,
graceful handling of bad input, and a printed summary at the end.
The program is deliberately split into inventory.py, sales.py, and
receipts.py, the same split described in concepts/12-modules.md.

Run it with:
    python main.py
"""

import inventory
import sales
import receipts


def main():
    catalog = {}
    catalog = inventory.add_stock(catalog, "Rice bag", 25.50, 40)
    catalog = inventory.add_stock(catalog, "Sugar", 12.75, 30)
    catalog = inventory.add_stock(catalog, "Cooking oil", 18.00, 15)

    orders = [
        ("Rice bag", 2),
        ("Sugar", 3),
        ("Cooking oil", 1),
        ("Sugar", 50),   # more than what's in stock, should fail gracefully
        ("Flour", 1),    # not in the catalog at all, should fail gracefully
    ]

    daily_total = 0
    sales_log = []

    for item_name, quantity in orders:
        price = inventory.get_price(catalog, item_name)
        daily_total, sale_amount = sales.record_sale(catalog, item_name, quantity, daily_total)
        if sale_amount > 0:
            sales_log.append(receipts.format_receipt_line(item_name, price, quantity))

    print()
    receipts.print_daily_summary(daily_total, sales_log)

    print()
    print("Remaining stock:")
    for item_name, details in catalog.items():
        print(f"  {item_name}: {details['quantity']}")

    inventory.save_catalog(catalog, "catalog.txt")
    print()
    print("Catalog saved to catalog.txt")


if __name__ == "__main__":
    main()
