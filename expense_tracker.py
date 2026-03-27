import csv
from datetime import datetime


# Add expense (UPDATED with category)
def add_expense(desc, amount, category):
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount, category, datetime.now().strftime("%Y-%m-%d")])


# View all expenses
def view_expenses():
    try:
        with open("expenses.csv", "r") as f:
            for row in csv.reader(f):
                print(f"Description: {row[0]}, Amount: {row[1]}, Category: {row[2]}, Date: {row[3]}")
    except FileNotFoundError:
        print("No expenses found.")


# Search expenses by category (NEW)
def search_category(category):
    found = False
    try:
        with open("expenses.csv", "r") as f:
            for row in csv.reader(f):
                if row[2].lower() == category.lower():
                    print(row)
                    found = True
        if not found:
            print("No matching expenses found.")
    except FileNotFoundError:
        print("No data available.")


# Total spent per category (NEW)
def total_per_category():
    totals = {}

    try:
        with open("expenses.csv", "r") as f:
            for row in csv.reader(f):
                category = row[2]
                amount = int(row[1])

                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount

        print("\nTotal Spending per Category:")
        for cat, total in totals.items():
            print(cat, ":", total)

    except FileNotFoundError:
        print("No data available.")


# Monthly total (NEW)
def monthly_total(month):
    total = 0

    try:
        with open("expenses.csv", "r") as f:
            for row in csv.reader(f):
                if row[3].startswith(month):  # YYYY-MM
                    total += int(row[1])

        print("Monthly Total:", total)

    except FileNotFoundError:
        print("No data available.")


# ================= MENU =================
while True:
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Total per Category")
    print("5. Monthly Total")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        desc = input("Enter description: ")
        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        add_expense(desc, amount, category)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category = input("Enter category: ")
        search_category(category)

    elif choice == "4":
        total_per_category()

    elif choice == "5":
        month = input("Enter month (YYYY-MM): ")
        monthly_total(month)

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")