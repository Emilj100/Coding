import re

name = input("Name: ")

if name := re.fullmatch(r"[a-zA-Z]", name):
        print("test")

print("hej")
