import sys
from pyfiglet import Figlet

figlet = Figlet()

figlet.getFonts()

figlet.setFont(font=sys.argv[1])

print(figlet.renderText(sys.argv[1]))
