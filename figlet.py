import sys
from pyfiglet import Figlet


user_input = input("Output: ")

if len(sys.argv) == 2:
    f = Figlet(font='slant')
    print(f.renderText(user_input))
