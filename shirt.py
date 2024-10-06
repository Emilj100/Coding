import sys
import csv



def main():
    user_input = sys.argv
    user_input = correct_input(user_input)
    old_file = sys.argv[1].lower()
    new_file = sys.argv[2].lower()



def correct_input(user_input):
    part_1, part_2 = user_input.split(" ")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif not part_1.endswith(".jpg", "jpeg", "png") and not part_2.endswith(".jpg", "jpeg", "png"):
        sys.exit("Invalid output")

    else:
        return user_input

main()
