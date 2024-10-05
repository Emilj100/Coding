import csv
import sys
from tabulate import tabulate

def main():
    # Check if there is exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")

    filename = sys.argv[1]

    # Check if the file is a CSV file
    if not filename.endswith(".csv"):
        sys.exit("File must be a CSV.")

    try:
        # Read the CSV file and store the rows
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Get the first row as headers
            table = [row for row in reader]  # Remaining rows as table data

        # Output the table formatted as ASCII art using tabulate
        print(tabulate(table, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist.")

if __name__ == "__main__":
    main()
