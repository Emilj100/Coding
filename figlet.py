import sys
from pyfiglet import Figlet

figlet = Figlet()

figlet.getFonts()

figlet.setFont(font="-f")

print(figlet.renderText(sys.argv[2]))
