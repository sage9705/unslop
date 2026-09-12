SEPARATOR = "========================================"


def format_receipt_line(item_name, price, quantity):
    total = price * quantity
    return f"{item_name:<18}{quantity:>2} x {price:>6.2f} = {total:>7.2f}"


def print_daily_summary(daily_total, sales_log):
    print(SEPARATOR)
    print("END OF DAY SUMMARY")
    print(SEPARATOR)
    for line in sales_log:
        print(line)
    print("----------------------------------------")
    print(f"DAILY TOTAL                      {daily_total:>7.2f}")
    print(SEPARATOR)