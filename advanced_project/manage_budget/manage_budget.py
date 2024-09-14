budget = {}

def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    if category in budget:
        budget[category] += amount
    else:
        budget[category] = amount
    print("Expense added successfully.")

def view_budget():
    print("Current Budget:")
    for category, amount in budget.items():
        print(category + ": " + str(amount))

def generate_report():
    total_expenses = sum(budget.values())
    print("Monthly Report:")
    print("Total Expenses: " + str(total_expenses))
    for category, amount in budget.items():
        print(category + ": " + str(amount))

def save_budget():
    with open("budget.txt", "w") as f:
        for category, amount in budget.items():
            f.write(category + ":" + str(amount) + "\n")
    print("Budget saved to file.")

def load_budget():
    global budget
    try:
        with open("budget.txt", "r") as f:
            for line in f:
                category, amount = line.strip().split(":")
                budget[category] = float(amount)
        print("Budget loaded from file.")
    except FileNotFoundError:
        print("No budget file found.")

while True:
    print("Personal Budgeting Tool")
    print("1. Add expense")
    print("2. View budget")
    print("3. Generate monthly report")
    print("4. Save budget")
    print("5. Load budget")
    print("6. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_budget()
    elif choice == "3":
        generate_report()
    elif choice == "4":
        save_budget()
    elif choice == "5":
        load_budget()
    elif choice == "6":
        break
    else:
        print("Invalid option. Please choose again.")
