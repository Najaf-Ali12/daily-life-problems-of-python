#EXPENSE TRACKER:
#DEVELOP A BASIC TOOL TO TRACK DAILY EXPENSES.USERS INPUT
#SPENDING AMOUNTS,CATEGORIES AND DATE.

# Create an empty list to store expenses
expenses = []

# Function to add a new expense
def add_expense():
    print("Add a new expense:")
    amount = float(input("  How much did you spend? "))  # Ask for the amount spent
    category = input("  What category does it belong to? (e.g., food, transport, entertainment) ")# Ask for the category
    date=input("enter the date of your spending")
    expenses.append({"amount": amount, "category": category,"date":date})  # Add the expense to the list
    print("Expense added!")

# Function to view all expenses
def view_expenses():
    print("\nYour expenses:")
    for expense in expenses:
        print("- Amount:", expense["amount"], "Category:", expense["category"],"date:",expense["date"])  # Print each expense

# Main program loop
while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("What do you want to do? (Enter 1, 2, or 3) ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break  # Exit the program
    else:
        print("Invalid choice. Please try again.")
