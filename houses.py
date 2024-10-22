students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house" "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco"m "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)
