import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regulært udtryk til at matche en IPv4-adresse i formatet #.#.#.#
    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    match = re.search(pattern, ip)

    # Tjekker om der er et match og om hver oktet er inden for det gyldige interval
    if match:
        for group in match.groups():
            if int(group) < 0 or int(group) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
