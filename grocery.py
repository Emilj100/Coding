dict = {

}


while True:
    try:
        item = input()
    except EOFError:
        for item in dict:
            print(item, dict[item])
        if item not in dict:
            dict[item] += 1

