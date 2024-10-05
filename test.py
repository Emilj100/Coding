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

data = []

try:
    with open(user_input) as file:
        table = csv.DictReader(file, fieldnames=["Regular Pizza", "Small", "Large"])
        for row in table:
            data.append(list(row.values()))


    print(tabulate.tabulate(data, tablefmt="grid"))



except FileNotFoundError:
    sys.exit("File does not exist")


