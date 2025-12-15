def process_bank_transactions_basic():
    balance = 1000
    type = ""
    while type != "FIN":
        type = input("D/R/FIN? ")
        if type == "D":
            amount = int(input("Amount? "))
            balance = balance + amount
        elif type == "R":
            amount = int(input("Amount? "))
            balance = balance - amount
    print("Balance:", balance)

process_bank_transactions_basic()