import re
import sys


def main():
    parse(input("HTML: "))


def parse(s):
    if s := re.search(r"<iframe.+?src=\"(.+)\".+></iframe>", s, re.IGNORECASE):
        if "youtube.com/embed/" in s:
        print(s.groups())
    else:
        print(None)




if __name__ == "__main__":
    main()
