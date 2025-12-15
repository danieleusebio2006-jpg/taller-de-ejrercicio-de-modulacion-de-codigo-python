def collect_survey_data_basic():
    total_age = 0
    count = 0
    age = 1 # Initialize to enter loop
    while age != 0:
        age = int(input("Enter age: "))
        if 25 <= age <= 45:
            total_age = total_age + age
            count = count + 1
    if count > 0:
        average_age = total_age / count
        print("Average age:", average_age)
    else:
        print("No valid ages entered.")

collect_survey_data_basic()