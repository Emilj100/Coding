try:
    x, y = int(input("Fraction: ")).split("/")
except ValueError:
    ...
except ZeroDivisionError:
    ...
print(y)
