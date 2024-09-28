import sys
from pyfiglet import Figlet


user_input = input("Output: ")

f = Figlet(font='slant')

print(f.renderText(user_input))
