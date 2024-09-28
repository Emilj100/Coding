import sys
from pyfiglet import Figlet
import random



if len(sys.argv) == 2:
    f = Figlet(font=sys.argv[1:])
    print(f.renderText("text to render"))
