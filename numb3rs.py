import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip := re.search(r"^(([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+))$", ip):
        int(ip.group(2))
        int(ip.group(3))
        int(ip.group(4))
        int(ip.group(5))
        if ip.group(2) > 0 and ip.group(2) < 255:
            if ip.group(3) > 0 and ip.group(3) < 255:
                if ip.group(4) > 0 and ip.group(4) < 255:
                    if ip.group(5) > 0 and ip.group(5) < 255:
                        return True
    else:
        return False


if __name__ == "__main__":
    main()
