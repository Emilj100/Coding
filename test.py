cookies = []

def main():
    amount = input("How many cookies in jar? ")
    test(int(amount))
    for cookie in cookies:
        print(cookie, end="")
    print()

def test(amount):
    for _ in range(amount):
        cookies.append("🍪")

main()
