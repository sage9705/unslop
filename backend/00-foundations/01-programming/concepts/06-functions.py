# Build the core of the Till Calculator project. Write a function `calculate_total(price, quantity, discount_percent=0, tax_rate=0.125)` that:

# 1. Calculates the subtotal.
# 2. Applies the discount, if any.
# 3. Adds tax on top of the discounted amount.
# 4. Returns the final total.

# Call it with at least three different combinations of arguments, including one that uses the default discount, and predict each result before running it

def calculate_total(price, quantity, discount_percent=0, tax_rate=0.125):
    subtotal = price * quantity
    discount = subtotal * (discount_percent / 100)
    discounted_total = subtotal - discount
    tax = discounted_total * tax_rate
    total = discounted_total + tax
    return total

print(f"The total price is ${calculate_total(3.2, 23):.2f}")
print(f"The total price is ${calculate_total(3.2, 23, 10):.2f}")
print(f"The total price is ${calculate_total(3.2, 23, 0.5, 0.2):.2f}")
    