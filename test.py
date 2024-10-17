cookies = []

def main():
    amount = input("How many cookies in jar? ")
    test(int(amount))
    print(cookies)

def test(amount):
    for _ in range(amount):
        cookies.append("🍪")

main()
