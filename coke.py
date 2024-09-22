# Beder brugeren om at indsætte et mønt
coin = int(input("Insert Coin"))

# Viser hvor meget brugeren skylder (Starter med 50 cents)
due = 50


while due >= 0:
    if coin == 25 or coin == 10 or coin == 5:
        print("Amount Due:", due - coin)
      
    else:
        print("forkert")

