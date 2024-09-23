due = 50


while due > 0:
    print("Amount Due:", due)
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin
    else:
        coin = int(input("Insert Coin: "))

if due < 0:
    print("Change Owed:", abs(due))
else:
    print("Change Owed: 0")






