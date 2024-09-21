def main():
    camel_case = input("Please write a name in camelCase")
    camel_case = uppercase(camel_case)

def uppercase(case):
    for c in case:
        print(c, end="")
        c.isupper()
        if c.isupper():
            print("godt")
        else:
            print("nej")





main()
