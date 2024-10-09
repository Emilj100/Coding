import re
import sys


def main():
    parse(input("HTML: "))


def parse(s):
    if s := re.search(r"(https?://)(?:www\.)(youtube.com)/embed/(.+)", s):
        print(s)




if __name__ == "__main__":
    main()
