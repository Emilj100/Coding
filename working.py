import re
import sys


def main():
    convert(input("Hours: "))


def convert(s):
    match_1 = re.search(r"^(([0-9]+):([0-9]+) AM) to (([0-9]+):([0-9]+) PM)$", s)
    match_2 = re.search(r"^(([0-9]+):[0-9]+ PM) to ([0-9]+:[0-9]+ AM)$", s)


    if match_1:
        if int(match_1.group(5)) == 1:
            number_1 = match_1.group(5).replace("1", "13")

        elif int(match_1.group(5)) == 2:
            number_1 = match_1.group(5).replace("2", "14")

        elif int(match_1.group(5)) == 3:
            number_1 = match_1.group(5).replace("3", "15")

        elif int(match_1.group(5)) == 4:
            number_1 = match_1.group(5).replace("4", "16")

        elif int(match_1.group(5)) == 5:
            number_1 = match_1.group(5).replace("5", "17")

        elif int(match_1.group(5)) == 6:
            number_1 = match_1.group(5).replace("6", "18")

        elif int(match_1.group(5)) == 7:
            number_1 = match_1.group(5).replace("7", "19")

        elif int(match_1.group(5)) == 8:
            number_1 = match_1.group(5).replace("8", "20")

        elif int(match_1.group(5)) == 9:
            number_1 = match_1.group(5).replace("9", "21")

        elif int(match_1.group(5)) == 10:
            number_1 = match_1.group(5).replace("10", "22")

        elif int(match_1.group(5)) == 11:
            number_1 = match_1.group(5).replace("11", "23")

        elif int(match_1.group(5)) == 12:
            number_1 = match_1.group(5).replace("12", "0")

        print(number_1)


    elif match_2:
        print("ja tak")
    else:
        raise ValueError("NEJ")





if __name__ == "__main__":
    main()
