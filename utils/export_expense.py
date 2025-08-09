from utils.get_expenses import get_expenses
import csv

def export_to_csv(filename):
    filename = f"{filename}.csv"
    expenses = get_expenses()
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Description', 'Category', 'Amount', 'Date'])
        for expense in expenses:
            writer.writerow([expense['id'], expense['description'], expense['category'], expense['amount'], expense['date']])
        print(f"Expenses exported to {filename} successfully.")