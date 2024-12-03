
while True:
    try:
        dollars = float(input("Change: "))
        if dollars > 0:
            break
    except ValueError:
        print("Not an integer")

cents = int(round(dollars * 100))
coins = 0
print(cents)

while cents > 0:

    if cents >= 0.25:
        coins += 1
        cents -= 0.25

    elif cents >= 0.10:
        coins += 1
        cents -= 0.10

    elif cents >= 0.05:
        coins += 1
        cents -= 0.05

    elif cents >= 0.01:
        coins += 1
        cents -= 0.01

print(coins)
