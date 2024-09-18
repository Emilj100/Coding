def main():
    name = input("Hi there")
    if "ello" in name:
        print("$0")
    elif funktion(name):
        print("$20")
    else:
        print("$100")


def funktion(x):
    return x.startswith("H")


main()


