import re
import sys


def main():
    parse(input("HTML: "))


def parse(s):
    if s := re.search(r"(https?://)(?:www\.)?(youtube.com)/embed/([^\"]+)", s):
        youtube = s.group(2).replace("youtube.com", "youtu.be/")
        print(s.group(1), youtube, s.group(3), sep="")
    else:
        print(None)




if __name__ == "__main__":
    main()
