# Beder brugeren om at indsætte et mønt
coin = int(input("Insert Coin: "))

# Viser hvor meget brugeren skylder (Starter med 50 cents)
due = 50


while due > 0:
    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin
        print("Amount Due:", due)
        coin = int(input("Insert Coin: "))
        due = due - coin
    else:
        print("Prøv igen")
        break


