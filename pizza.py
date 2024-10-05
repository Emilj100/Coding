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

data = [["Cheese","$13.50","$18.95"]
["1 topping","$14.75","$20.95"]
["2 toppings","$15.95","$22.95"]
["3 toppings","$16.95","$24.95"]
["Special","$18.50","$26.95"]
]

try:
    with open(user_input) as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]


    print(tabulate.tabulate(data, headers=header, tablefmt="grid"))



except FileNotFoundError:
    sys.exit("File does not exist")

