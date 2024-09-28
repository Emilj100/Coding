import inflect

# Opret en instans af inflect engine
p = inflect.engine()

# Opret en tom liste til at gemme navnene
names = []

# Læs input fra brugeren indtil EOF (Ctrl+D)
try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    # Når EOFError opstår, formatér listen af navne og udskriv dem med korrekt kommatering
    print(f"Adieu, adieu, to {p.join(names)}")
