
while True:
    try:
        dollars = float(input("Change: "))
        if dollars > 0:
            break
    except ValueError:
        print("Not an integer")

cents = int(round(dollars * 100))
coins = 0

while cents > 0:

    if cents >= 25:
        coins += 1
        cents -= 25

    elif cents >= 10:
        coins += 1
        cents -= 10

    elif cents >= 5:
        coins += 1
        cents -= 5

    elif cents >= 1:
        coins += 1
        cents -= 1

print(coins)
