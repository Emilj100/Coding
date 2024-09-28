import sys
from pyfiglet import Figlet
from random import choice

if not sys.argv[1] == "-f" or sys.argv[1] == "--font":
    sys.exit("invalid usage")

elif len(sys.argv) == 1:
    user_input = input("Output: ")

    random_font = choice(["slant", "rectangles", "alphabet", "acrobatic", "alligator2"])

    f = Figlet(font=random_font)

    print(f.renderText(user_input))


elif len(sys.argv) == 3:
    user_input = input("Output: ")

    f = Figlet(font=sys.argv[2])

    print(f.renderText(user_input))
