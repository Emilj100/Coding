while True:
    try:
        n = int(input("Length: "))
        if n > 0:
            break
    except ValueError:
        pass

for i in range(n):
    print("?", end="")
print()

