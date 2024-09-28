import inflect

dict = [

]


while True:
    p = inflect.engine()
    try:
        user_input = input("Name: ")
        dict[user_input] = 1


    except EOFError:
        mylist = p.join((dict))
        print(mylist)
