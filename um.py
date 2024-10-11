import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0

    for um in s:
        if um == "um":
            counter += 1

    return counter


if __name__ == "__main__":
    main()
