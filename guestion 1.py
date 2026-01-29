while True:
    try:
        voltage = float(input("Enter voltage (V):"))
        current = float(input("Enter current (I): "))

        power = voltage * current
        print("Power (P) =", power, "Watts")
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    choice = input("Do you want to calculate again? (yes/no): ").lower()
    if choice != "yes":
        print("Program ended.")
        break


