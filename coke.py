due = 50


while due > 0:
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin
        if due > 0:
            print("Amount Due:", due)
        else:
            print("Change Owed: ", abs(due))
    else:
        coin = int(input("Insert Coin: "))






