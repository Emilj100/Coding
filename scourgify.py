import sys
import tabulate
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

                first, last = full_name.split(",")

                data.append(first, last, house)

    except FileNotFoundError:
        sys.exit("File does not exist")

    fieldnames = ["name", "home"]

    with open(new_file, "w") as file_2:
        writer = csv.DictWriter(file_2, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow([data])



def correct_input(user_input):
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        return user_input

main()






