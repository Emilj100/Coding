# Beder brugeren om at indsætte et mønt


# Viser hvor meget brugeren skylder (Starter med 50 cents)
due = 50


while due > 0:
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin
        print("Amount Due:", due)
    else:
        print("Prøv igen")
        break


