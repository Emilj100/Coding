

cookies = []

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        for _ in range(self.capacity):
            cookies.append("🍪")

    def __str__(self):
        "".join(cookies)
        return str(cookies)



def main():
    amount = input("How many cookies in jar? ")
    amount = Jar(int(amount))
    print(amount)

main()
