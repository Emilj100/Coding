def main():
    name = input("Hi there")
    if funktion(name):
        print("True")
    else:
        print("False")



def funktion(x):
    return x.startswith("H")

main ()


