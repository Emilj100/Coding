import pillow
import sys
import csv



def main():
    user_input = sys.argv
    user_input = correct_input(user_input)
    old_file = sys.argv[1]
    new_file = sys.argv[2]


def correct_input(user_input):
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        return user_input
