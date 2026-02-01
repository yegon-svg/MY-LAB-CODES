while True:
    try:
        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (I): "))

        power = voltage * current
        print(power, "Watts")
    except ValueError:
        print("")

    choice = input("Do you want to calculate again? (yes/no): ").lower()
    if choice != "yes":
        break

