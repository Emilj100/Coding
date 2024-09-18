expression = input("Expression:")

x, y, z = expression.split(" ")

x = float(x)
z = float(z)

if y == "+":
    name = x + z
elif y == "-":
    name = x - z
elif y == "*":
    name = x * z
else:
    name = x / z

print(name)
