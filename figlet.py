import sys
from pyfiglet import Figlet
from random import choice

if len(sys.argv) == 0:
    user_input = input("Output: ")

    


elif len(sys.argv) == 3:
    user_input = input("Output: ")

    f = Figlet(font=sys.argv[2])

    print(f.renderText(user_input))
