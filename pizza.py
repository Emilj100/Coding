import sys
import tabulate
import csv

user_input = sys.argv[1]

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif not user_input.endswith(".csv"):
    sys.exit("Not a CSV file")

header = []

try:
    with open(user_input) as file:
        table = csv.DictReader(file)
        for row in table:
            header.append({"pizza": row["Regular Pizza"], "Small": row["Small"], "Large":["Large"]})


        print(tabulate.tabulate(table, headers=header, tablefmt="grid"))



except FileNotFoundError:
    sys.exit("File does not exist")


