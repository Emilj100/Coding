from validator_collection import validators

user_email = input("What's your email address? ")

try:
    email_address = validators.email(user_email)
    print("Valid")

except ValueError:
    print("Invalid")
