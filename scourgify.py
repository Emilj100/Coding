import sys
import tabulate
import csv

def main():



def correct_input(user_input):
    if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")






user_input = sys.argv[1]

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif not user_input.endswith(".csv"):
    sys.exit("Not a CSV file")
