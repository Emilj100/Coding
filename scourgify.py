import sys
import tabulate
import csv



def main():
    user_input = sys.argv
    user_input = correct_input(user_input)
    old_file = sys.argv[1]
    new_file = sys.argv[2]

    try:
        with open(user_input) as file:
            


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






