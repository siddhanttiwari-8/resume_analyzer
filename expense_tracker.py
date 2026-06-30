import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# ----------------------------
# CREATE FILE IF NOT EXISTS
# ----------------------------
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "description", "amount"])

# ----------------------------
# ADD EXPENSE
# ----------------------------
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter category (Food, Travel, Study, etc): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, description, amount])

    print("\n✅ Expense added successfully!\n")

# ----------------------------
# VIEW ALL EXPENSES
# ----------------------------
def view_expenses():
    print("\n📄 ALL EXPENSES\n")

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# ----------------------------
# MONTHLY TOTAL
# ----------------------------
def monthly_total():
    total = 0

    current_month = datetime.now().strftime("%Y-%m")

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["date"].startswith(current_month):
                total += float(row["amount"])

    print(f"\n📊 Total spending this month: ₹{total}\n")

# ----------------------------
# CATEGORY WISE TOTAL
# ----------------------------
def category_total():
    category = input("Enter category to analyze: ")

    total = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["category"].lower() == category.lower():
                total += float(row["amount"])

    print(f"\n📌 Total spent on {category}: ₹{total}\n")

# ----------------------------
# MENU
# ----------------------------
def menu():
    init_file()

    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Total")
        print("4. Category Wise Total")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_total()
        elif choice == "4":
            category_total()
        elif choice == "5":
            print("Exiting.... Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

# ----------------------------
# RUN PROGRAM
# ----------------------------
if __name__ == "__main__":
    menu()
