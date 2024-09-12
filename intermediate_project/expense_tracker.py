# Simple Expense Tracker

class ExpenseManager:
    def __init__(self, filename):
        # Initialize an empty dictionary to store expenses and load existing expenses from file
        self.expenses = {}
        self.filename = filename
        self.load_expenses()

    def load_expenses(self):
        """
        Load expenses from the file.
        """
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    date, amount, description = line.strip().split(',')
                    if date not in self.expenses:
                        self.expenses[date] = []
                    self.expenses[date].append({'amount': float(amount), 'description': description})
        except FileNotFoundError:
            self.expenses = {}

    def save_expenses(self):
        """
        Save expenses to the file.
        """
        with open(self.filename, 'w') as file:
            for date, entries in self.expenses.items():
                for entry in entries:
                    file.write(f"{date},{entry['amount']},{entry['description']}\n")

    def add_expense(self, date, amount, description):
        """
        Add a new expense.
        """
        if date not in self.expenses:
            self.expenses[date] = []
        self.expenses[date].append({'amount': amount, 'description': description})
        self.save_expenses()
        print(f"Expense on '{date}' added successfully!")

    def view_expenses(self):
        """
        View all expenses.
        """
        if not self.expenses:
            print("No expenses found.")
        else:
            for date, entries in self.expenses.items():
                print(f"\nDate: {date}")
                for entry in entries:
                    print(f"  Amount: ${entry['amount']:.2f}, Description: {entry['description']}")

    def search_expenses(self, date):
        """
        Search expenses for a specific date.
        """
        if date in self.expenses:
            print(f"Expenses on {date}:")
            for entry in self.expenses[date]:
                print(f"  Amount: ${entry['amount']:.2f}, Description: {entry['description']}")
        else:
            print(f"No expenses found for {date}.")

    def update_expense(self, date, index, amount, description):
        """
        Update an existing expense entry.
        """
        if date in self.expenses and 0 <= index < len(self.expenses[date]):
            self.expenses[date][index]['amount'] = amount
            self.expenses[date][index]['description'] = description
            self.save_expenses()
            print(f"Expense on '{date}' updated successfully!")
        else:
            print(f"Expense not found on {date} at index {index}.")

    def delete_expense(self, date, index):
        """
        Delete an expense entry.
        """
        if date in self.expenses and 0 <= index < len(self.expenses[date]):
            del self.expenses[date][index]
            if not self.expenses[date]:
                del self.expenses[date]
            self.save_expenses()
            print(f"Expense on '{date}' deleted successfully!")
        else:
            print(f"Expense not found on {date} at index {index}.")


def main():
    expense_manager = ExpenseManager("expenses.txt")

    while True:
        print("\nExpense Tracker\n")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses by Date")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            amount = float(input("Enter the amount: "))
            description = input("Enter a description: ")
            expense_manager.add_expense(date, amount, description)

        elif choice == '2':
            expense_manager.view_expenses()

        elif choice == '3':
            date = input("Enter the date to search (YYYY-MM-DD): ")
            expense_manager.search_expenses(date)

        elif choice == '4':
            date = input("Enter the date of the expense to update (YYYY-MM-DD): ")
            index = int(input("Enter the expense index to update: "))
            amount = float(input("Enter new amount: "))
            description = input("Enter new description: ")
            expense_manager.update_expense(date, index, amount, description)

        elif choice == '5':
            date = input("Enter the date of the expense to delete (YYYY-MM-DD): ")
            index = int(input("Enter the expense index to delete: "))
            expense_manager.delete_expense(date, index)

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


main()
