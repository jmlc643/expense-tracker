import argparse

from utils.get_summary import summary
from utils.list_expenses import list_expenses
from utils.update_expense import update_expense
from utils.verify_json_file import verify_json_file
from utils.add_expense import add_expense
from utils.delete_expense import delete_expense
from utils.export_expense import export_to_csv

verify_json_file("expenses.json")

parse = argparse.ArgumentParser(prog="Expense Tracker", description="A simple command-line expense tracker.", epilog="Developed by jmlc643")

subparsers = parse.add_subparsers(dest='command', help='Available commands')

# ADD PARSER
add_parser = subparsers.add_parser('add', help='Add a new expense')
add_parser.add_argument('--description', help='Description of the expense', type=str, required=True)
add_parser.add_argument('--category', help='Category of the expense', type=str, required=True)
add_parser.add_argument('--amount', help='Amount of the expense', type=float, required=True)

# LIST PARSER
list_parser = subparsers.add_parser('list', help='List all expenses')
list_parser.add_argument('--category', help='Category of the expense', type=str)

# UPDATE PARSER
update_parser = subparsers.add_parser('update', help='Update an existing expense')
update_parser.add_argument('--id', help='ID of the expense to update', type=int, required=True)
update_parser.add_argument('--description', help='Description of the expense', type=str)
update_parser.add_argument('--category', help='Category of the expense', type=str)
update_parser.add_argument('--amount', help='Amount of the expense', type=float)

# DELETE PARSER
delete_parser = subparsers.add_parser('delete', help='Delete an expense')
delete_parser.add_argument('--id', help='ID of the expense to delete', type=int, required=True)

# SUMMARY
summary_parser = subparsers.add_parser('summary', help='Get a summary of expenses')
summary_parser.add_argument('--month', help='Month to filter expenses (Number of Month)', type=int)

# EXPORT EXPENSES
export_parser = subparsers.add_parser('export', help='Export expenses to a CSV file')
export_parser.add_argument('--filename', help='Name of the CSV file to export to', type=str, required=True)

args = parse.parse_args()

if args.command == 'add':
    add_expense(args.description, args.amount, args.category)
if args.command == 'list':
    if args.category:
        list_expenses(category=args.category)
    else:
        list_expenses()
if args.command == 'update':
    update_expense(args.id, args.description, args.amount, args.category)
if args.command == 'delete':
    delete_expense(args.id)
if args.command == 'summary':
    summary(month=args.month)
if args.command == 'export':
    export_to_csv(args.filename)