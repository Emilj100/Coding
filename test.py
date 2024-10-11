import validators

def main():
    email = input("Email: ").strip()
    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")

def validate_email(email):
    # Brug validators biblioteket til at kontrollere, om e-mailen er gyldig
    return validators.email(email)

if __name__ == "__main__":
    main()
