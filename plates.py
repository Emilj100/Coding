def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
     # Sikre at de 2 første tegn er bogstaver
    if not s[0:2].isalpha():
        return False

    found_digit = False

    for c in s:
        if c.isdigit():
            if not found_digit:
                found_digit = True
                if c == "0":
                    return False
        elif found_digit and c.isalpha():
            return False
    return True

if __name__ == "__main__":
    main()

