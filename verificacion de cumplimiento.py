def verify_sales_goals_basic():
    goal_met_count = 0
    sales = 1 # Initialize to enter loop
    while sales >= 0:
        sales = int(input("Sales amount: "))
        if sales >= 5000:
            goal_met_count = goal_met_count + 1
    print("Goal met:", goal_met_count)

verify_sales_goals_basic()