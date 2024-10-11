import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"um", s, re.IGNORECASE)
    return match


if __name__ == "__main__":
    main()
