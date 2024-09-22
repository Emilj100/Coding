def main():
    camel_case = input("Please write a name in camelCase")
    snake_case = uppercase(camel_case)
    print(snake_case)

def uppercase(case):
    result = ""
    for c in case:
        if c.isupper():
            result += "_"
            result += c.lower()
        else:
            result += c

    return result




main()
