from utils.get_expenses import get_expenses
from datetime import datetime

def summary(month = None):
    expenses = get_expenses()
    if month:
        expenses = [expense for expense in expenses if datetime.fromisoformat(expense['date']).month == month]
    
    if not expenses:
        if month:
            print(f"No expenses found for month {month}")
        else:
            print("No expenses found")
        return
    
    total = sum(expense['amount'] for expense in expenses)
    
    month_names = ["", "January", "February", "March", "April", "May", "June", 
                      "July", "August", "September", "October", "November", "December"]

    if month:
        print(f"Total expenses for {month_names[month]}: ${total:.2f}")
    else:
        print(f"Total expenses: ${total:.2f}")