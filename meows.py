def meow(n: int) -> str:
    return "meow\n" * n



number = input("Number: ")
meows: str = meow(number)
print(meows)
