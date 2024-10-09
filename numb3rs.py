import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip := re.search(r"^(([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+))$", ip):
        if ip.group(2) == 0-250:
            if ip.group(3) == 0-250:
                if ip.group(4) == 0-250:
                    if ip.group(5) == 0-250:
                        return True
    else:
        return False


if __name__ == "__main__":
    main()
