import inflect

items = []

while True:
    p = inflect.engine()
    try:
        user_input = input("Name: ")
        items += [user_input]


    except EOFError:
        mylist = p.join((items))
        print(mylist, end="\n")
        break
