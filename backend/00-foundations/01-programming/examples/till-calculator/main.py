"""
Till Calculator

Calculates an order total, including a percentage discount and tax, then
prints a receipt and reports whether the customer gave enough cash.

Run it with:
    python main.py
"""


def calculate_subtotal(order):
    subtotal = 0

    for item_name, price, quantity in order:
        subtotal += price * quantity

    return subtotal


def apply_discount(subtotal, discount_percent):
    discount = subtotal * (discount_percent / 100)
    return subtotal - discount


def apply_tax(amount, tax_rate):
    return amount + (amount * tax_rate)


def calculate_total(order, discount_percent=5, tax_rate=0.125):
    subtotal = calculate_subtotal(order)
    discounted_total = apply_discount(subtotal, discount_percent)
    return apply_tax(discounted_total, tax_rate)


def calculate_change(cash_given, total_due):
    return cash_given - total_due


def print_receipt(order, total, cash_given, change):
    print("==================================")
    print("CORNER SHOP RECEIPT")
    print("==================================")

    for item_name, price, quantity in order:
        line_total = price * quantity
        print(f"{item_name:<18}{quantity:>2} x {price:>6.2f} = {line_total:>7.2f}")

    print("----------------------------------")
    print(f"{'TOTAL':<29}{total:>6.2f}")
    print(f"{'CASH GIVEN':<29}{cash_given:>6.2f}")
    print(f"{'CHANGE':<29}{change:>6.2f}")
    print("==================================")

    if change < 0:
        print("Not enough cash given for this order.")
    else:
        print(f"Change due: {change:.2f}")


if __name__ == "__main__":
    order = [
        ("Rice bag", 25.50, 2),
        ("Cooking oil", 18.00, 1),
        ("Sugar", 12.75, 3),
    ]

    total = calculate_total(order)
    cash_given = 100.00
    change = calculate_change(cash_given, total)

    print_receipt(order, total, cash_given, change)
