due = 50


while due > 0:
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin
        print("Amount Due:", due)
    else:
        coin = int(input("Insert Coin: "))

while due <= 0:
    if due == 0:
        due + coin
        print("Change Owed: ", due)





