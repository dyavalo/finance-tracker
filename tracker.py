import csv
import os
from datetime import datetime

FILE = "transactions.csv"

def init_file():
    if not os.path.exists(FILE):
        with open(FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Type", "Amount", "Description"])

def add_transaction(entry_type, amount, desc):
    init_file()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, entry_type, amount, desc])
    print("Transaction added.")

def view_summary():
    init_file()
    total_income = 0
    total_expense = 0
    with open(FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            if len(row) < 3: continue
            if row[1] == "Income":
                total_income += float(row[2])
            elif row[1] == "Expense":
                total_expense += float(row[2])
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Balance: ${total_income - total_expense:.2f}")

def view_all():
    init_file()
    with open(FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

if __name__ == "__main__":
    while True:
        print("\nOptions: 1. Add Income 2. Add Expense 3. View Summary 4. View All 5. Exit")
        choice = input("Choose: ")
        if choice == '1':
            amount = float(input("Amount: "))
            desc = input("Description: ")
            add_transaction("Income", amount, desc)
        elif choice == '2':
            amount = float(input("Amount: "))
            desc = input("Description: ")
            add_transaction("Expense", amount, desc)
        elif choice == '3':
            view_summary()
        elif choice == '4':
            view_all()
        elif choice == '5':
            break
