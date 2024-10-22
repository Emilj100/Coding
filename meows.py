def meow(n: int) -> str:
    """meow n times."""
    return "meow\n" * n



number = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
