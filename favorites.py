import csv

with open("favorites.csv") as file:
    reader = csv.DictReader(file)
    counts = {}

    for row in reader:
        favorite = row["language"]
