import sys

user_input = sys.argv[1]

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif not user_input.endswith(".py"):
    sys.exit("Not a Python file")

lines = 0


try:
    with open(user_input) as file:
        for row in file:
            row = row.strip()
            if not row.startswith("#"):
                lines += 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(lines)
