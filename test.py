import re

height = input("Height: ")

if height := re.fullmatch(r"[0-9]{3}( )?(cm)?"):
        print("valid")

else:
print("invalid")
