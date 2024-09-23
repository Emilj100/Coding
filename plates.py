def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2] not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]:
        return True
    else:
        return False

main()
