import re
import sys


def main():
    parse(input("HTML: "))


def parse(s):
    if s := re.search(r"<iframe.+?src=\"(.+)\"></iframe>", s, re.IGNORECASE):
        youtube = s.group(2).replace("youtube.com", "youtu.be/")
        print(s.groups())
    else:
        print(None)




if __name__ == "__main__":
    main()
