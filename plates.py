def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for c in s:
        found_digit = c.isdigit()
        if found_digit == 0:
            break
        elif found_digit.isalpha():
            return False




main()
