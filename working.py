import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^([0-9:]+AM) to ([0-9:]+PM)$", s)
    if match:
        print("rigtig")





if __name__ == "__main__":
    main()
