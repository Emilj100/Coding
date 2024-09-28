import sys
from pyfyglet import Figlet

figlet = Figlet()

print(figlet.renderText(sys.argv[1]))
