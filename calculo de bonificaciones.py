def calculate_overtime_bonus_basic():
    total_bonus = 0
    employee_count = 0
    hours = 0  # Initialize to enter loop
    while hours >= 0:
        hours = int(input("Overtime hours: "))
        if hours > 5:
            bonus = hours * 15
        else:
            bonus = hours * 10
        total_bonus = total_bonus + bonus
        employee_count = employee_count + 1
    print("Total bonus:", total_bonus)
    print("Employees:", employee_count)

calculate_overtime_bonus_basic()