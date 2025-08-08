from utils.get_expenses import get_expenses
import json
from datetime import datetime

def add_expense(description, amount):
    expenses = get_expenses()
    
    if expenses == []:
        id = 1
    else:
        id = max(expense['id'] for expense in expenses) + 1
        
    new_expense = {
        "id": id,
        "date": datetime.now().isoformat(),
        "description": description,
        "amount": amount
    }
    
    expenses.append(new_expense)
    
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
        
    print(f"Expense added succesfully (ID: {id})")