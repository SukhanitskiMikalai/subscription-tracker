expenses = []

def add_expense(): ## функция 1
    name = input("Expense name: ")
    amount = float(input("Amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)

def show_expenses(): ## функция 2
    for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense['name']} - {expense['amount']} PLN")

def show_monthly_total():  ## функция 3
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Monthly total: {total} PLN")

def delete_expense():
    show_expenses()

    number = int(input("Ente expense number: "))
    index = number - 1

    expenses.pop(index)

def search_expense():
    search = input("Search: ")

    for expense in expenses:
        if search.lower() in expense["name"].lower():
            print(f"{expense['name']} - {expense['amount']} PLN")

while True:
    print("\n=== Subscription Tracker ===")
    print("1. Add expense")
    print("2. Show expense")
    print("3. Show monthly total")
    print("4. Delete expense")
    print("5. Search expense")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":  ## вызов 1-ой функции
        add_expense()  

    elif choice == "2":  ## вызов 2-ой функции 
        show_expenses()

    elif choice == "3":  ## вызов 3-ой функции
        show_monthly_total()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        search_expense()

    elif choice == "0":
        break

    else:
        print("Invalid option")
