import json

def get_expenses():
    try:
        with open("expenses.json", "r") as file:
            content = file.read().strip()
            if not content:
                expenses = []
            else:
                file.seek(0)
                expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(e)
        
    return expenses