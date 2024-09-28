import sys
from pyfiglet import Figlet

figlet = input(Figlet("Input: "))

figlet.getFonts()

figlet.setFont(font="-f")

print(figlet.renderText(sys.argv[2]))
