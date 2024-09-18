def main():
    name = input("Hi there")
    if funktion(name):
        print("$20")
    elif dollars(name):
        print("$0")
    else:
        print("$100")



def funktion(x):
    return x.startswith("H")

def dollars(z):
    return z.endswith("ello")



main()


