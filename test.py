def main():
    camel_case = input("Please write a name in camelCase")
    camel_case = uppercase(camel_case)

def uppercase(case):
    for c in case:
        if c.isupper():
            print("_", end="")
            c.lower()
            print(c, sep="")
        else:
            print(c, end="")



main()
