name = input("What is the answer to the great question of life, the universe, and everything?")

match name:
    case "42" | "forty Two" | "forty-two":
        print("Yes")
    case _:
        print("No")
