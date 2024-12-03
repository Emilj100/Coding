n = int(input("Size: "))

x = 0
for _ in range(n):
    x += 1
    for _ in range(n):
        print(" ", end="")
    for _ in range(x):
        print("#", end="")
    print()
