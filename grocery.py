dict = {

}


while True:
    try:
        item = input().upper()
        if item not in dict:
            dict[item] = 1
        elif item in dict:
            dict[item] += 1
    except EOFError:
        for item in dict:
            print(dict[item], item)
            break

