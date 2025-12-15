def control_inventory_basic():
    stock = 50
    replenishment_point = 10
    sales = 0 # Initialize to enter loop
    while True:
        sales = int(input("Sales amount: "))
        stock = stock - sales
        if stock <= replenishment_point:
            print("Urgent Replenishment Notice")
            break
    print("Final stock:", stock)

control_inventory_basic()