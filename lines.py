import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif not sys.argv.endswith(".py"):
    sys.exit("Not a Python file")

