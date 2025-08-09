# Expense Tracker

A simple command-line expense tracker application built with Python. This project helps you manage your personal expenses by allowing you to add, list, update, delete, and analyze your spending habits.

This project is based on the [Expense Tracker challenge](https://roadmap.sh/projects/expense-tracker) from [roadmap.sh](https://roadmap.sh/).

## Features

- ✅ **Add expenses** with description, amount, and category
- ✅ **List all expenses** or filter by category
- ✅ **Update existing expenses** by ID
- ✅ **Delete expenses** by ID
- ✅ **View summaries** of total expenses (overall or by month)
- ✅ **Export expenses** to CSV format
- ✅ **Category-based expense tracking**
- ✅ **Automatic expense ID generation**
- ✅ **Data persistence** using JSON storage

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jmlc643/expense-tracker.git
   cd expense-tracker
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The application uses a command-line interface with different subcommands:

### Add an Expense
```bash
python main.py add --description "Lunch at restaurant" --category "Food" --amount 25.50
```

### List Expenses
```bash
# List all expenses
python main.py list

# List expenses by category
python main.py list --category "Food"
```

### Update an Expense
```bash
python main.py update --id 1 --description "Updated description" --amount 30.00 --category "Food"
```
*Note: You can update individual fields by providing only the parameters you want to change.*

### Delete an Expense
```bash
python main.py delete --id 1
```

### View Summary
```bash
# Total summary of all expenses
python main.py summary

# Summary for a specific month (1-12)
python main.py summary --month 7
```

### Export to CSV
```bash
python main.py export --filename "my_expenses.csv"
```

### Help
```bash
# General help
python main.py --help

# Help for specific commands
python main.py add --help
python main.py list --help
```

## Examples

Here are some practical examples of how to use the expense tracker:

```bash
# Add some expenses
python main.py add --description "Coffee" --category "Food" --amount 4.50
python main.py add --description "Gas" --category "Transportation" --amount 45.00
python main.py add --description "Movie tickets" --category "Entertainment" --amount 24.00

# List all expenses
python main.py list

# Get summary for current month
python main.py summary --month 8

# Export to CSV
python main.py export --filename "august_expenses.csv"
```

## Project Structure

```
expense-tracker/
│
├── main.py                 # Main application entry point
├── expenses.json           # JSON file storing expense data
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
│
└── utils/                 # Utility modules
    ├── add_expense.py     # Add expense functionality
    ├── delete_expense.py  # Delete expense functionality
    ├── export_expense.py  # CSV export functionality
    ├── get_expenses.py    # Retrieve expenses from storage
    ├── get_summary.py     # Generate expense summaries
    ├── list_expenses.py   # List and display expenses
    ├── update_expense.py  # Update expense functionality
    └── verify_json_file.py # JSON file validation and creation
```

## Data Format

Expenses are stored in JSON format with the following structure:

```json
[
    {
        "id": 1,
        "description": "Lunch at restaurant",
        "amount": 25.50,
        "category": "Food",
        "date": "2025-08-09T14:30:00.123456"
    }
]
```

## Requirements

- Python 3.6 or higher
- argparse (included in Python standard library)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**jmlc643** - [GitHub Profile](https://github.com/jmlc643)

## Acknowledgments

- This project is based on the [Expense Tracker challenge](https://roadmap.sh/projects/expense-tracker) from [roadmap.sh](https://roadmap.sh/)
- Thanks to the roadmap.sh community for providing excellent learning resources

---

*Built as part of the Backend Development learning path on roadmap.sh*