import csv

with open("favorites.csv") as file:
    reader = csv.DictReader(file)
    scratch, c, python = 0, 0, 0
