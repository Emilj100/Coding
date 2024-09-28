import sys
from pyfiglet import Figlet
from random import choice

if len(sys.argv) == 1:
    user_input = input("Output: ")

    random_font = choice(["slant", "rectangles", "alphabet", "acrobatic", "alligator2"])

    f = Figlet(font=random_font)

    print(f.renderText(user_input))


elif len(sys.argv) == 3:
    user_input = input("Output: ")

    f = Figlet(font=sys.argv[2])

    print(f.renderText(user_input))
