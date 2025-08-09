import argparse

from utils.list_expenses import list_expenses
from utils.verify_json_file import verify_json_file
from utils.add_expense import add_expense
from utils.delete_expense import delete_expense

verify_json_file("expenses.json")

parse = argparse.ArgumentParser(prog="Expense Tracker", description="A simple command-line expense tracker.", epilog="Developed by jmlc643")

subparsers = parse.add_subparsers(dest='command', help='Available commands')

add_parser = subparsers.add_parser('add', help='Add a new expense')
add_parser.add_argument('--description', help='Description of the expense', type=str, required=True)
add_parser.add_argument('--category', help='Category of the expense', type=str, required=True)
add_parser.add_argument('--amount', help='Amount of the expense', type=float, required=True)

list_parser = subparsers.add_parser('list', help='List all expenses')
list_parser.add_argument('--category', help='Category of the expense', type=str)

delete_parser = subparsers.add_parser('delete', help='Delete an expense')
delete_parser.add_argument('--id', help='ID of the expense to delete', type=int, required=True)

args = parse.parse_args()

if args.command == 'add':
    add_expense(args.description, args.amount, args.category)
if args.command == 'list':
    if args.category:
        list_expenses(category=args.category)
    else:
        list_expenses()
if args.command == 'delete':
    delete_expense(args.id)