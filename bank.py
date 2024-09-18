name = input("Hi there")

name = name.startswith("H")

match name:
    case "Hello" | "forty two" | "forty-two":
        print("$0")
    case "H":
        print("$20")
    case _:
        print("$100")
