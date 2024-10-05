import sys
import tabulate
import csv



def main():
    user_input = sys.argv
    user_input = correct_input(user_input)
    old_file = sys.argv[1]
    new_file = sys.argv[2]


    data = []

    try:
        with open(old_file) as file:
            reader = csv.reader(file)
            for row in reader:
                first, last, house = row.split(",")
                data.append(first, last, house)


    except FileNotFoundError:
        sys.exit("File does not exist")


def correct_input(user_input):
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        return user_input

main()






