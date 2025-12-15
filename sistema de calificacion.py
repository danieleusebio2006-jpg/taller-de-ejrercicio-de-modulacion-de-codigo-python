def analyze_order_ratings_basic():
    total_orders = 0
    total_score = 0
    excellent_orders = 0

    rating = 1  # Initialize to enter the loop

    while rating != 0:
        rating = int(input("Enter rating (1-5, 0 to end): "))
        if rating != 0:
            total_orders = total_orders + 1
            total_score = total_score + rating
            if rating == 5:
                excellent_orders = excellent_orders + 1

    if total_orders > 0:
        average = total_score / total_orders
        print("Total orders:", total_orders)
        print("Average rating:", average)
        print("Excellent orders:", excellent_orders)
    else:
        print("No ratings entered.")

analyze_order_ratings_basic()