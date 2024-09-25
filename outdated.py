month = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

while True:
    x, y, z = input("Date: ").replace(",", "").title().replace("/", " ").strip().split(" ")
    if x in month:
        x = month[x]
    if y in month:
        pass
    x = int(x)
    y = int(y)
    if x >= 13:
        pass
    if y >= 32:
        pass
    else:
        print(f"{z}-{x:02}-{y:02}")
        break
