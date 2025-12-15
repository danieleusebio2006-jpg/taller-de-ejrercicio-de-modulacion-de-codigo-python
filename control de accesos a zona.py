def control_warehouse_access_basic():
    allowed = 0
    denied = 0
    code = "INV-001"

    employee_code = "" # Initialize to enter the loop

    while employee_code != "SALIR":
        employee_code = input("Enter code (SALIR to exit): ")
        if employee_code != "SALIR":
            if employee_code == code:
                print("Access granted")
                allowed = allowed + 1
            else:
                print("Access denied")
                denied = denied + 1

    print("Allowed:", allowed)
    print("Denied:", denied)

control_warehouse_access_basic()