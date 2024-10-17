

cookies = []

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity

    def __str__(self):
    for _ in range(self.capacity):
        cookies.append("🍪")

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

def main():
    amount = input("How many cookies in jar? ")
    amount = Jar(int(amount))

main()


def main():
    amount = input("How many cookies in jar? ")
    test(int(amount))
    for cookie in cookies:
        print(cookie, end="")
    print()

def test(amount):

main()
