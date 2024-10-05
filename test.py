import sys
import csv

def main():
    # Tjek om de korrekte antal kommandolinjeargumenter er givet
    user_input = sys.argv
    user_input = correct_input(user_input)

    old_file = sys.argv[1]  # Filen der læses fra
    new_file = sys.argv[2]  # Filen der skrives til

    data = []  # Liste der skal gemme de opdelte data

    # Læs inputfilen og opdel navnene
    try:
        with open(old_file) as file_1:
            reader = csv.DictReader(file_1)

            # Gennemgå hver række i CSV-filen
            for row in reader:
                full_name = row["name"]  # Fuld navn i formatet "efternavn, fornavn"
                house = row["house"]  # Hus

                # Split navnet op i fornavn og efternavn
                last, first = full_name.strip().split(",")
                first = first.strip()
                last = last.strip()

                # Tilføj en ordbog til data-listen med opdelte felter
                data.append({"first": first, "last": last, "house": house.strip()})

    except FileNotFoundError:
        sys.exit(f"Error: File '{old_file}' does not exist")

    # Definer kolonnenavne for outputfilen
    fieldnames = ["first", "last", "house"]

    # Skriv de opdelte data til en ny CSV-fil
    try:
        with open(new_file, "w", newline='') as file_2:
            writer = csv.DictWriter(file_2, fieldnames=fieldnames)
            writer.writeheader()  # Skriv kolonneoverskrifter
            writer.writerows(data)  # Skriv data-rækkerne

    except Exception as e:
        sys.exit(f"Error: Could not write to file '{new_file}'")

def correct_input(user_input):
    # Tjek for det korrekte antal kommandolinjeargumenter
    if len(user_input) > 3:
        sys.exit("Too many command-line arguments")
    elif len(user_input) < 3:
        sys.exit("Too few command-line arguments")
    else:
        return user_input

if __name__ == "__main__":
    main()
