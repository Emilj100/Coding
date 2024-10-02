def main():
    name = input("Hi there ").lower()
    print(value(name))


def value(greeting):
    if greeting.lower().startswith("hello"):
        return f"$0"
    elif greeting.lower().startswith("h"):
        return f"$20"
    else:
        return f"$100"


if __name__ == "__main__":
    main()

