def track_assembly_production_basic():
    total_defective = 0
    units = int(input("How many units? "))
    for i in range(units):
        quality = input("D or O? ")
        if quality == "D":
            total_defective = total_defective + 1
    print("Defective:", total_defective)

track_assembly_production_basic()