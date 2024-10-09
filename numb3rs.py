import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip := re.search(r"^(([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+))$", ip):
        ip_2 = int(ip.group(2))
        ip_3 = int(ip.group(3))
        ip_4 = int(ip.group(4))
        ip_5 = int(ip.group(5))
        if ip_2 >= 0 and ip_2 <= 255:
            return True
        else:
            return False

    else:
        return False


if __name__ == "__main__":
    main()
