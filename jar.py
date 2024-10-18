class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):

        if self._size + n > self._capacity:
            raise ValueError("Too many cookies!")
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies!")
        self._size -= n


    @property
    def size(self):
        return self._size

    @property
    def capacity(self):
        return self._capacity


def main():
    # Til capacity
    amount = input("What is the max capacity in the cookie jar? ")
    jar = Jar(int(amount))

    # Til deposit
    user_deposit = int(input("How many cookies would you like to deposit? "))
    jar.deposit(user_deposit)

    # Til withdraw
    user_withdraw = int(input("How many cookies would you like to withdraw? "))
    jar.withdraw(user_withdraw)


    print(jar)


if __name__ == "__main__":
    main()
