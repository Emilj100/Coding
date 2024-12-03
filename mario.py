while
    n = int(input("Size: "))


x = n - 1
y = 0
for _ in range(n):
    y += 1
    for _ in range(x):
        print(" ", end="")
    x -= 1
    for _ in range(y):
        print("#", end="")
    print()
