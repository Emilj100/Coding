def main():
    name = input("Hi there ").lower()
    print("$", value(name), sep="")


def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

