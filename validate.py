import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(com|edu|gov|net)$", email):
    print("Valid")
else:
    print("Invalid")


