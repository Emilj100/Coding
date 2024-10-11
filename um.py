import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"\bum\b", s, re.IGNORECASE)
    counter = list(match)
    test = len(counter)
    return test



if __name__ == "__main__":
    main()
