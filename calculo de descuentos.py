def calculate_sales_discount_basic():
    total = 0
    price = 0
    while price != "FIN":
        price = input("Price? (FIN to end) ")
        if price != "FIN":
            quantity = int(input("Quantity? "))
            total = total + int(price) * quantity
    if total > 1000:
        total = total * 0.9
    elif total > 500:
        total = total * 0.95
    print("Total:", total)

calculate_sales_discount_basic()