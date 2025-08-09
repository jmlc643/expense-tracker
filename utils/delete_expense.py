from utils.get_expenses import get_expenses
import json

def delete_expense(id):
    expenses = get_expenses()
    expenses = [expense for expense in expenses if expense['id'] != id]
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent = 4)
    print(f"Expense deleted successfully (ID: {id})")