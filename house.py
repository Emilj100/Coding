name = input("What's your name? ")

match name:
    case "Harry" :
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
