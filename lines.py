import sys

user_input = sys.argv[1]

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif not user_input.endswith(".py"):
    sys.exit("Not a Python file")

else:

    try:
        with open(user_input) as file:

    except FileNotFoundError:
        sys.exit("File does not exist")


