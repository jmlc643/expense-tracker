import argparse

from utils.verify_json_file import verify_json_file
from utils.add_expense import add_expense

verify_json_file("expenses.json")

parse = argparse.ArgumentParser(prog="Expense Tracker", description="A simple command-line expense tracker.", epilog="Developed by jmlc643")

subparsers = parse.add_subparsers(dest='command', help='Available commands')

# Subcomando para agregar gastos
add_parser = subparsers.add_parser('add', help='Add a new expense')
add_parser.add_argument('--description', help='Description of the expense', type=str, required=True)
add_parser.add_argument('--amount', help='Amount of the expense', type=float, required=True)

args = parse.parse_args()

if args.command == 'add':
    add_expense(args.description, args.amount)