import csv

with open("favorites.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        favorite = row[1]
        print(favorite)


