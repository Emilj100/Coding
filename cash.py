
while True:
    try:
        dollars = float(input("Change: "))
        if dollars > 0:
            break
    except ValueError:
        print("Not an integer")

coins = 0

while dollars > 0:

    if dollars >= 0.25:
        coins += 1
        dollars -= 0.25

    elif dollars >= 0.10:
        coins += 1
        dollars -= 0.10

    elif dollars >= 0.05:
        coins += 1
        dollars -= 0.05

    elif dollars >= 0.01:
        coins += 1
        dollars -= 0.01

print(coins)
