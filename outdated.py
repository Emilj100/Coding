x, y, z = input("Date: ").title().replace("/", " ").split(" ")


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

if x in month:
    x = month[x]

print(f"{z}-{y:02}-{x:02}")
