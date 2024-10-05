import sys
import csv



def main():
    user_input = sys.argv
    user_input = correct_input(user_input)
    old_file = sys.argv[1]
    new_file = sys.argv[2]


    data = []

    try:
        with open(old_file) as file_1:
            reader = csv.DictReader(file_1)
            for row in reader:
                full_name = row["name"]
                house = row["house"]

                last, first = full_name.strip().split(",")
                first = first.strip()
                last = last.strip()
                house = house.strip()

                data.append({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit("File does not exist")

    fieldnames = ["first", "last", "house"]

    with open(new_file, "w", newline='') as file_2:
        writer = csv.DictWriter(file_2, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)



def correct_input(user_input):
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        return user_input

main()






