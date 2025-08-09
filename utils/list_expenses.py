from utils.get_expenses import get_expenses

def list_expenses(category = None):
    expenses = get_expenses()
    if category:
        expenses = [expense for expense in expenses if expense['category'] == category]
    if expenses == []:
        print("No expenses found.")
        return
    for expense in expenses:
        print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")