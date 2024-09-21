def main():
    user_input = input("Please write a name in camelCase")
    user_input = uppercase(user_input)
    print(user_input)


def uppercase(case):
    case = case.isupper()
    return case

main()
