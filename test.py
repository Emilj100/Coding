import tabulate

user_input = input()

with open(user_input) as file:
    print(tabulate(file))
