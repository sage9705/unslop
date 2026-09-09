# A customer buys three different items at a shop. Write a program that:

# 1. Calculates the subtotal for all three items.
# 2. Applies a 5% discount if the subtotal is over 100.
# 3. Adds a 12.5% tax on top of the discounted total.
# 4. Prints the final amount the customer owes.

# Then calculate the change due if the customer pays with a specific amount of cash.

item1_price = 45.00
item2_price = 30.00
item3_price = 35.00

subtotal = item1_price + item2_price + item3_price

# You haven't learnt about conditional statements yet, we'll cover them in the next lesson. 
if subtotal > 100:
    discounted_total = subtotal - (subtotal * 0.05)
else:
    discounted_total = subtotal

final_amount = discounted_total + (discounted_total * 0.125)

print("Final amount the customer owes:", final_amount)

# calculate change due if the customer pays with a specific amount of cash
cash_paid = 200.00
change_due = cash_paid - final_amount
print("Change due:", change_due)