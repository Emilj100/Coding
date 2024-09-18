expression = ("Expression:")

x, y, z = expression.split(" ")

x = float(x)
y = float(y)

if y == "+":
    name = x + z

print(name)
