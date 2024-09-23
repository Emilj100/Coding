def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
        # Sikre at de 2 første tegn er bogstaver
    if s[0:2].isalpha():
        #Sikre at der maks er 6 tegn i nummberpladen
        if len(s) <= 6:
                return True
    else:
         return False

    for c in s:
         # Tjekker hvornår der er tal i nummerpladen
         found_digit = c.isdigit()
    if found_digit == 0:
              return False
         elif c.isalpha():
              return False




main()
