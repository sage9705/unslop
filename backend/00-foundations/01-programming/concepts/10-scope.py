# Write two separate functions, `apply_shop_discount(total)` and `apply_loyalty_discount(total)`, 
# each of which creates its own local variable called `discount` and returns a discounted total using a different percentage. 
# Call both functions with the same starting total and confirm the two `discount` variables never interfere with each other.

# Then write a small experiment that tries to read one function's local variable from outside of it, and observe the error.

def apply_shop_discount(total):
    discount = 0.10  # 10% shop discount
    discounted_total = total * (1 - discount)
    return discounted_total

def apply_loyalty_discount(total):
    discount = 0.15  # 15% loyalty discount
    discounted_total = total * (1 - discount)
    return discounted_total

# test the functions
total = 100.00
shop_discounted = apply_shop_discount(total)
loyalty_discounted = apply_loyalty_discount(total)

print(f"Original total: ${total:.2f}")
print(f"Shop discounted total: ${shop_discounted:.2f}")
print(f"Loyalty discounted total: ${loyalty_discounted:.2f}")

# try to access the local variables from outside the functions (this will cause an error)
# print(discount)  # This will raise a NameError

