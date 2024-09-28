import sys
from pyfiglet import Figlet

def main():
    user_input = input("Output: ")
    f = font(sys.argv)
    print(f.renderText(user_input))


def font(f):
    if len(sys.argv) == 2:
        f = Figlet(font='slant')
        return f


main()
