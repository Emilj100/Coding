import sys
from pyfiglet import Figlet

if len(sys.argv) > 2:
    user_input = input("Output: ")

    f = Figlet(font=sys.argv[2])

    print(f.renderText(user_input))
