def main():
    # Indhent gyldig højde fra brugeren
    height = get_height()

    # Byg pyramiden
    for i in range(1, height + 1):
        # Print mellemrum for højrejustering
        print(" " * (height - i), end="")
        # Print hashes
        print("#" * i)


def get_height():
    """Indhenter en gyldig højde fra brugeren mellem 1 og 8."""
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                return height
        except ValueError:
            pass  # Hvis brugeren ikke indtaster et tal, prøver vi igen


if __name__ == "__main__":
    main()


