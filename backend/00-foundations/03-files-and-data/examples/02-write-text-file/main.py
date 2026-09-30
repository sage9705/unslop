"""
Daily Sales Logger

Logs each sale to sales_log.txt as it happens, demonstrating the
difference between "w" mode, which starts a fresh log, and "a" mode,
which adds to an existing one without erasing it. This is the
reference example for concept 05 (writing files).

Run it with:
    python main.py
"""


def start_new_log(filepath):
    """Open the log fresh for a new day, erasing anything already
    there. Meant to be called once, at the start of the day."""
    with open(filepath, "w") as file:
        file.write("item_name,amount\n")


def log_sale(filepath, item_name, amount):
    """Append a single sale to the log, without touching what's
    already there."""
    with open(filepath, "a") as file:
        file.write(f"{item_name},{amount:.2f}\n")


def print_log(filepath):
    """Print the full log as it currently stands."""
    print("=" * 30)
    print("SALES LOG")
    print("=" * 30)
    with open(filepath, "r") as file:
        for line in file:
            print(line.strip())
    print("=" * 30)


if __name__ == "__main__":
    log_path = "sales_log.txt"

    start_new_log(log_path)
    log_sale(log_path, "Rice bag", 51.00)
    log_sale(log_path, "Sugar", 38.25)
    log_sale(log_path, "Cooking oil", 18.00)

    print_log(log_path)

    print()
    print("Logging one more sale, without starting a new log...")
    log_sale(log_path, "Flour", 15.00)

    print_log(log_path)
