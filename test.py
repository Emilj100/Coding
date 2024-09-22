def main():
    camel_case = input("Please write a name in camelCase")
    camel_case = uppercase(camel_case)
    print(camel_case, end="", sep="")

def uppercase(case):
    for c in case:
        if c.isupper():
            print("_", end="")
            c = c.lower()
            return c
        else:
            print(c, end="")



main()
