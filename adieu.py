import inflect




while True:
    p = inflect.engine()
    try:
        user_input = input("Name: ")


    except EOFError:
        mylist = p.join((user_input))
        print(mylist)
