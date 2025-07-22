# project-02-expense-tracker
# Expense Tracker CLI

A simple command-line interface (CLI) tool to track, update, delete, and summarize your expenses using a CSV file for storage.

## Features

- Add new expenses with description and amount
- Update existing expenses by ID
- Delete expenses by ID
- View all expenses in a formatted table
- Get a summary of total expenses
- View expenses filtered by a specific month

## Requirements

- Python 3.x

## Usage

Run the program with Python and use the command-line arguments to perform actions:

### Add a new expense
python expense.py --add --description "Lunch" --amount 10.50

### Update an existing expense by ID
python expense.py --update --id 2 --update_description "Dinner" --update_amount 15.00

### Delete an expense by ID
python expense.py --delete --id 3

### View summary of all expenses
python expense.py --summary

### View all expenses
python expense.py --all

### View expenses for a specific month
python expense.py --month 07
(This shows expenses for July.)

### Data Storage
All expenses are stored in expense_tracker.csv in the same directory as the script.

### Each expense has:

ID (unique incremental integer)

Date (last updated date)

Description

Amount

### Notes
The CSV file is created automatically when you add your first expense.

When deleting or updating, specify the expense by its ID.

The month filter expects the month as a two-digit string (e.g., "01" for January).

### License
This project is open source and free to use.
