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
            return False




if s[0:2].isalpha():
     if len(s) <= 6:
         return True


main()
