import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip := re.search(r"^(([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+))$", ip):
        ip_2 = int(ip.group(2))
        ip_3 = int(ip.group(3))
        ip_4 = int(ip.group(4))
        ip_5 = int(ip.group(5))
        if ip_2 >= 0 and ip_2 <= 255:
            if ip_3 >= 0 and ip_3 <= 255:
                if ip_4 >= 0 and ip_4 <= 255:
                    if ip_5 >= 0 and ip_5 <= 255:
                        return True
        else:
            return False


if __name__ == "__main__":
    main()
