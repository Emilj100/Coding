
def main():
    coin = int(input("Insert Coin: "))
    coin = machine(coin)

due = 50

def machine(cash):
    while due >= 0:
        if cash == 25 or cash == 10 or cash == 5:
            return due - cash
        else:
            return False

main()
