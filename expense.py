import csv
import argparse
from datetime import datetime
import os


def main():
    # Main Arguments
    parser = argparse.ArgumentParser(description="Track your expenses. ")
    parser.add_argument("--add", action="store_true", help="add a new expense")
    
    parser.add_argument("--summary", action="store_true", help= "get a summary of all expenses")
    parser.add_argument("--delete", action="store_true",help= "delete an expense")
    parser.add_argument("--update",action="store_true",help="update an expense")
    parser.add_argument("--month",type=str,help= "get summary of expenses of a specific month")
    parser.add_argument("--all",action="store_true",help= "get all expenses")


    # Only used with --add
    parser.add_argument("--amount", type=float,help="amount of the expense")
    parser.add_argument("--description", type=str,help="description of the expense")

    # Ony used with --update
    parser.add_argument("--update_amount",type=float,help="updated amount of the expense")
    parser.add_argument("--update_description",type=str,help="update the description of the expense")
    
    # used with --update and --delete
    parser.add_argument("--id", type=int, help="ID of the expense to update or delete")


    args = parser.parse_args()
    if args.add:
        add_expense(args)
    elif args.update:
        update_expense(args)
    elif args.delete:
        delete_expense(args)
    elif args.summary:
        view_summary()
    elif args.month:
        view_month(args)
    elif args.all:
        view_all()
        

    
    
def add_expense(args):
    
    if args.description is None or args.amount is None:
        print("Error: --description and -- amount need to be inputted with --add")
        return
    date = datetime.now().strftime("%Y-%m-%d")
    x =  (args.description)
    y = (args.amount)
    file_empty = not os.path.exists("expense_tracker.csv") or os.stat("expense_tracker.csv").st_size == 0
    file_path = "expense_tracker.csv"
    next_id = 1
    if not file_empty:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            ids = [int(row["ID"]) for row in reader if row["ID"].isdigit()]
            if ids:
                next_id = max(ids) + 1

    with open("expense_tracker.csv", 'a', newline='') as csvfile:
        fieldnames = [ 'ID','Date(last updated)', 'Description','Amount']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    
        if file_empty:
            writer.writeheader()
        writer.writerow({'ID': next_id,'Date(last updated)': date, 'Description':x, 'Amount': y})


def update_expense(args):
    if args.id is None:
        print("Error: --id must be provided with --update")
        return
    date = datetime.now().strftime("%Y-%m-%d")
    rows = []
    found = False
    with open("expense_tracker.csv", "r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row["ID"]) == args.id:
                found = True
                row["Description"] = args.update_description or row["Description"]
                row["Amount"] = args.update_amount or row["Amount"]
                row["Date(last updated)"] = date
            rows.append(row)

    if not found:
        print("Expense with that ID not found.")
        return

    with open("expense_tracker.csv", "w", newline='') as csvfile:
        fieldnames = ['ID', 'Date(last updated)', 'Description', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)





def delete_expense(args):
    if args.id is None:
        print("Error: --id must be provided with --delete")
        return

    with open("expense_tracker.csv", "r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        expenses = list(reader)

    # Find and remove the expense with matching ID
    new_expenses = []
    found = False
    for row in expenses:
        if int(row["ID"]) == args.id:
            found = True
            continue  # skip this row (deletes it)
        new_expenses.append(row)

    if not found:
        print("Expense with that ID not found.")
        return

    with open("expense_tracker.csv", "w", newline='') as csvfile:
        fieldnames = ['ID', 'Date(last updated)', 'Description', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_expenses)

def view_all():
    try:
        with open("expense_tracker.csv", 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print(f"{'ID':<5} {'Date':<15} {'Description':<20} {'Amount':>10}")
            print("-" * 55)
            for row in reader:
                print(f"{row['ID']:<5} {row['Date(last updated)']:<15} {row['Description']:<20} ${float(row['Amount']):>9.2f}")
    except FileNotFoundError:
        print("No expenses found yet.")


def view_summary():
    try:
        with open("expense_tracker.csv", 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            x = 0
            for row in reader:
                y = float(row["Amount"])
                x = x + y
            print(f"${x:.2f}")
    except FileNotFoundError:
        print("No Expenses found yet")

def view_month(args):
    try:
        total = 0
        with open("expense_tracker.csv",'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                y = row["Date(last updated)"]
                x,y,z = y.split("-")
                if args.month == y:
                    x = row["Amount"]
                    x = float(x)
                    total = total+x
            
            print(f"${total:.2f}")
    except FileNotFoundError:
        print("No Expenses found yet")

if __name__ == "__main__":
    main()