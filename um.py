import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"\bum\b", s, re.IGNORECASE)
    counter = len(list(match))
    return counter



if __name__ == "__main__":
    main()
