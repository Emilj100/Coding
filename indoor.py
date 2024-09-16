x = input("How much would you like to tip? ")

x = x.removesuffix("%")

z = int(x) / int(100)

y = float(z)

print(y)
