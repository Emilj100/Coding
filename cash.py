dollars = int(input("Change: "))

coins = 0

while dollars > 0:

    if dollars >= 25:
        coins += 1
        dollars -= 25

    elif dollars >= 10:
        coins += 1
        dollars -= 10

    elif dollars >= 5:
        coins += 1
        dollars -= 5

    elif dollars >= 1:
        coins += 1
        dollars -= 1

print(coins)
