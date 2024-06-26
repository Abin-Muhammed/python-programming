from datetime import datetime

# List to store expenses
expenses = []

# Add a new expense
def add_expense():
    category = input("Enter expense category: ").lower()
    description = input("Enter a brief description: ")

    while True:
        try:
            amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Please enter a valid number for the expense amount.")
    
    while True:
        date_input = input("Enter the date of expense (DD-MM-YYYY) or press Enter to use today's date: ")
        if not date_input:
            expense_date = datetime.now().strftime("%d-%m-%Y")
            break
        try:
            expense_date = datetime.strptime(date_input, "%d-%m-%Y").strftime("%d-%m-%Y")
            break
        except ValueError:
            print("Please enter a valid date in DD-MM-YYYY format.")
    
    expense = {
        "category": category,
        "description": description,
        "amount": amount,
        "date": expense_date
    }
    expenses.append(expense)

# Display expenses summary
def display_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\nExpense Summary:")
    category_summary = {}
    total_expense = 0

    for expense in expenses:
        total_expense += expense["amount"]
        if expense["category"] in category_summary:
            category_summary[expense["category"]] += expense["amount"]
        else:
            category_summary[expense["category"]] = expense["amount"]

    print(f"Total Expense: ${total_expense:.2f}")
    print("Category-wise Summary:")
    for category, amount in category_summary.items():
        print(f"{category.capitalize()}: ${amount:.2f}")

# Display monthly summary
def display_monthly_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nMonthly Expense Summary:")
    monthly_summary = {}
    
    for expense in expenses:
        month = expense["date"][3:10]  # Extract the 'MM-YYYY' part of the date
        if month in monthly_summary:
            monthly_summary[month] += expense["amount"]
        else:
            monthly_summary[month] = expense["amount"]

    for month, amount in monthly_summary.items():
        print(f"{month}: ${amount:.2f}")

# Main expense tracker function
def expense_tracker():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. View Monthly Summary")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            display_monthly_summary()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select again.")

    print("Goodbye!")

# Run the expense tracker
expense_tracker()
