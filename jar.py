class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity

    def __str__(self):
        for _ in self.capacity:
            return "🍪"

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...


def main():
    amount = input("How many cookies in jar? ")
    amount = Jar(int(amount))

main()
