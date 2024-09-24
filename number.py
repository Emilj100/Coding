def main():
    x = get_int("What's x? ")
    y = get_int("What's y? ")
    print(f"x is {x} and y is {y}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
