def meow(n: int):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meows: str = meow(number)
print(meows)
