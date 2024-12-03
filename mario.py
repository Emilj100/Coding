n = int(input("Size: "))

x = -1
y = 0
for _ in range(n):
    x += 1
    y += 1
    for _ in range(x):
        print(" ", end="")
    for _ in range(y):
        print("#", end="")
    print()
