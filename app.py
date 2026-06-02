expenses = []

while True:
    print("\n=== Subscription Tracker ===")
    print("1. Add expense")
    print("2. Show expense")
    print("3. Shoe monthly total")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))

        expense = {
            "name": name,
            "amount": amount
        }

        expenses. append(expense)

    elif choice == "2":
        for expense in expenses:
            print(f"{expense['name']} - {expense['amount']} PLN")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Monthly total: {total} PLN")

    elif choice == "0":
        break

    else:
        print("Invalid option")
