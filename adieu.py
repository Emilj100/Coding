import inflect


p = inflect.engine()

while True:
    try:
        user_input = input("Name: ")

    except EOFError:
       mylist = p.join(user_input)
       print(mylist)

