import sys
from pyfiglet import Figlet


user_input = input("Output: ")

f = Figlet(font=sys.argv[2])

print(f.renderText(user_input))
