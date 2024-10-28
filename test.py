import re

height = input("Height: ")

if height := re.fullmatch(r"[0-9]{3}( )?(cm)?", height, re.IGNORECASE):
        print("valid")

else:
        print("invalid")

print('Invalid input: Please enter "Male" or "Female"')
