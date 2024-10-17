def main():
    amount = input("How many cookies in jar? ")
    print(test(int(amount)))

def test(amount):
    for _ in range(amount):
        print("🍪")

main()
