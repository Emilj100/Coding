

cookies = []

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        for _ in range(self.capacity):
            cookies.append("🍪")

    def __str__(self):
        return "".join(cookies)

    def deposit(self, n):
        cookies_in_jar = 0
        cookies_in_jar += int(n)
        if int(cookies_in_jar) < int(self.capacity):
            return cookies_in_jar
        else:
            raise ValueError





def main():
    # Til capacity
    amount = input("What is the max capacity in the cookie jar? ")
    amount = Jar(int(amount))
    print(amount)
    # Til deposit
    user_deposit = input("How many cookies would you like to deposit? ")
    deposit_object = Jar()
    cookies_in_jar = deposit_object.deposit(user_deposit)
    print(cookies_in_jar)


main()
