try:
    x, y = (input("Fraction: ").split("/"))
    x = int(x)
    y = int(y)

except ValueError:
    ...
except ZeroDivisionError:
    ...
