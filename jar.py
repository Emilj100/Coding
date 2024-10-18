class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity  # Privat variabel til kapacitet
        self._size = 0  # Start med 0 cookies i krukken

    def __str__(self):
        return "🍪" * self._size  # Returnér det korrekte antal cookies som en streng

    def deposit(self, n):
        # Tjek om der er plads til flere cookies uden at overskride kapaciteten
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies!")
        self._size += n  # Tilføj cookies til krukken

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies!")
        self._size -= n


    @property
    def size(self):
        return self._size  # Returnér det aktuelle antal cookies i krukken

    @property
    def capacity(self):
        return self._capacity  # Returnér kapaciteten af krukken


def main():
    # Til capacity
    amount = input("What is the max capacity in the cookie jar? ")
    jar = Jar(int(amount))  # Opret en krukke med den ønskede kapacitet

    # Til deposit
    user_deposit = int(input("How many cookies would you like to deposit? "))
    jar.deposit(user_deposit)  # Tilføj cookies til krukken

    # Til withdraw
    user_withdraw = int(input("How many cookies would you like to withdraw? "))
    jar.withdraw(user_withdraw)

    # Print den opdaterede krukke med cookies
    print(jar)


if __name__ == "__main__":
    main()
