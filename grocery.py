dict = [

]

while True:
    try:
        item = input()
        dict[item] = item
    except EOFError:
        print(dict)

