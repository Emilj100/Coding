import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip := re.search(r"^([1]+\.[1]+\.[1]+\.[1]+)$", ip):
        return True
    else:
        return False



if __name__ == "__main__":
    main()
