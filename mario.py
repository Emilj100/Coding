while True:
    n = int(input("Size: "))
    if n > 0 and n < 9:
        break


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
