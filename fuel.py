try:
    z = (input("Fraction: "))
    x, y = z.split("/")
    x = int(x)
    y = int(y)

except ValueError:
    ...
except ZeroDivisionError:
    ...

fuel = {
    "1/4": "25%",
    "2/4": "50%",
    "3/4": "75",
    "4/4": "F",
}

if z in fuel:
    print(fuel[z])
