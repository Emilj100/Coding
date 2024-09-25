dict = [

]

while True:
    try:
        item = input()
    except EOFError:
        print(dict)
    if item not in dict:
        dict[item] = 1

