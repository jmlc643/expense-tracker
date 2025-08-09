from utils.get_expenses import get_expenses
import json

def update_expense(id, description=None, amount=None, category=None):
    try:
        id = int(id)
    except ValueError:
        print("The ID must be an integer.")
        return
    expenses = get_expenses()
    expense_founded = False
    for expense in expenses:
        if expense['id'] == id:
            if description is not None:
                expense['description'] = description
            if amount is not None:
                expense['amount'] = amount
            if category is not None:
                expense['category'] = category
            expense_founded = True
            break
    if not expense_founded:
        print(f"Expense with ID {id} not found.")
        return
    try:
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent = 4)
    except Exception as e:
        print(f"Error updating expense: {e}")