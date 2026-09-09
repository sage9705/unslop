# A shop wants an automatic stock status for each product. Write a program that takes a stock quantity and a reorder threshold, then prints one of:

# "Out of stock" if quantity is 0
# "Reorder now" if quantity is at or below the threshold
# "Stock healthy" otherwise

stock_quantity = 10
reorder_threshold = 5

if stock_quantity == 0:
    print("Out of stock")
elif stock_quantity <= reorder_threshold:
    print("Reorder now")
else:
    print("Stock healthy")
    
    