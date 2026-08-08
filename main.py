# Expense Tracker - Python Mini Project
# Author: Noor e Fajar (B.E. Electronics Engineering)

import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return
    category = input("Enter category (Food/Travel/Study/Other): ")
    date = datetime.now().strftime("%d-%m-%Y")
    expenses.append({"name": name, "amount": amount, "category": category, "date": date})
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n----- All Expenses -----")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['name']} | Rs. {e['amount']:.2f} | {e['category']} | {e['date']}")

def total_expense(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Expense: Rs. {total:.2f}")

def category_summary(expenses):
    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]
    print("\n----- Category-wise Summary -----")
    for cat, amt in summary.items():
        print(f"{cat}: Rs. {amt:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category-wise Summary")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            print("Thank you for using Expense Tracker. Bye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
