import inflect




while True:
    p = inflect.engine()
    try:
        user_input = input("Name: ")
        

    except EOFError:
       print(user_input)
       break
