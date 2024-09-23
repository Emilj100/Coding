def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
# Sikre at de 2 første tegn er bogstaver
      #Sikre at der maks er 6 tegn i nummberpladen

def is_valid(s):
    if not s[0:2].isalpha():
        return False
    if len(s) > 6 or len(s) < 2:
         return False



    found_digit = False

    for c in s:
        if c == "," or c == " " or c == ".":
            return False
        if c.isdigit():
            if not found_digit:
                found_digit = True
                if c == "0":
                    return False
        elif found_digit and c.isalpha():
            return False
    return True




main()
