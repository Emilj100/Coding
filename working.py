import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match_1 = re.search(r"^(([0-9]+):([0-9]+) AM) to (([0-9]+):([0-9]+) PM)$", s)
    match_2 = re.search(r"^(([0-9]+):([0-9]+) PM) to (([0-9]+):([0-9]+) AM)$", s)
    match_3 = re.search(r"^(([0-9]+) PM) to (([0-9]+) AM)$", s)
    match_4 = re.search(r"^(([0-9]+) AM) to (([0-9]+) PM)$", s)


    if match_1:

        number_1_am_match_1 = match_1.group(2)
        number_2_am_match_1 = match_1.group(3)
        number_2_pm_match_1 = match_1.group(6)

        if int(match_1.group(2)) == 12:
            number_1_am_match_1 = match_1.group(2).replace("12", "00")

        if int(match_1.group(5)) == 1:
            number_1_pm_match_1 = match_1.group(5).replace("1", "13")

        elif int(match_1.group(5)) == 2:
            number_1_pm_match_1 = match_1.group(5).replace("2", "14")

        elif int(match_1.group(5)) == 3:
            number_1_pm_match_1 = match_1.group(5).replace("3", "15")

        elif int(match_1.group(5)) == 4:
            number_1_pm_match_1 = match_1.group(5).replace("4", "16")

        elif int(match_1.group(5)) == 5:
            number_1_pm_match_1 = match_1.group(5).replace("5", "17")

        elif int(match_1.group(5)) == 6:
            number_1_pm_match_1 = match_1.group(5).replace("6", "18")

        elif int(match_1.group(5)) == 7:
            number_1_pm_match_1 = match_1.group(5).replace("7", "19")

        elif int(match_1.group(5)) == 8:
            number_1_pm_match_1 = match_1.group(5).replace("8", "20")

        elif int(match_1.group(5)) == 9:
            number_1_pm_match_1 = match_1.group(5).replace("9", "21")

        elif int(match_1.group(5)) == 10:
            number_1_pm_match_1 = match_1.group(5).replace("10", "22")

        elif int(match_1.group(5)) == 11:
            number_1_pm_match_1 = match_1.group(5).replace("11", "23")

        elif int(match_1.group(5)) == 12:
            number_1_pm_match_1 = match_1.group(5).replace("12", "00")

        return f"{int(number_1_am_match_1):02}:{number_2_am_match_1} to {number_1_pm_match_1}:{number_2_pm_match_1}"


    elif match_2:
        number_1_am_match_2 = match_2.group(5)
        number_2_am_match_2 = match_2.group(6)
        number_2_pm_match_2 = match_2.group(3)

        if int(match_2.group(5)) == 12:
            number_1_am_match_2 = match_2.group(5).replace("12", "00")

        elif int(match_2.group(2)) == 1:
            number_1_pm_match_2 = match_2.group(2).replace("1", "13")

        elif int(match_2.group(2)) == 2:
            number_1_pm_match_2 = match_2.group(2).replace("2", "14")

        elif int(match_2.group(2)) == 3:
            number_1_pm_match_2 = match_2.group(2).replace("3", "15")

        elif int(match_2.group(2)) == 4:
            number_1_pm_match_2 = match_2.group(2).replace("4", "16")

        elif int(match_2.group(2)) == 5:
            number_1_pm_match_2 = match_2.group(2).replace("5", "17")

        elif int(match_2.group(2)) == 6:
            number_1_pm_match_2 = match_2.group(2).replace("6", "18")

        elif int(match_2.group(2)) == 7:
            number_1_pm_match_2 = match_2.group(2).replace("7", "19")

        elif int(match_2.group(2)) == 8:
            number_1_pm_match_2 = match_2.group(2).replace("8", "20")

        elif int(match_2.group(2)) == 9:
            number_1_pm_match_2 = match_2.group(2).replace("9", "21")

        elif int(match_2.group(2)) == 10:
            number_1_pm_match_2 = match_2.group(2).replace("10", "22")

        elif int(match_2.group(2)) == 11:
            number_1_pm_match_2 = match_2.group(2).replace("11", "23")

        elif int(match_2.group(2)) == 12:
            number_1_pm_match_2 = match_2.group(2).replace("12", "00")

        return f"{number_1_pm_match_2}:{number_2_pm_match_2} to {int(number_1_am_match_2):02}:{number_2_am_match_2}"

    elif match_3:

        number_1_am_match_3 = match_3.group(4)

        if int(match_3.group(4)) == 12:
            number_1_am_match_3 = match_3.group(2).replace("12", "00")

        if int(match_3.group(2)) == 1:
            number_1_pm_match_3 = match_3.group(2).replace("1", "13")

        if int(match_3.group(2)) == 2:
            number_1_pm_match_3 = match_3.group(2).replace("2", "14")

        if int(match_3.group(2)) == 3:
            number_1_pm_match_3 = match_3.group(2).replace("3", "15")

        if int(match_3.group(2)) == 4:
            number_1_pm_match_3 = match_3.group(2).replace("4", "16")

        if int(match_3.group(2)) == 5:
            number_1_pm_match_3 = match_3.group(2).replace("5", "17")

        if int(match_3.group(2)) == 6:
            number_1_pm_match_3 = match_3.group(2).replace("6", "18")

        if int(match_3.group(2)) == 7:
            number_1_pm_match_3 = match_3.group(2).replace("7", "19")

        if int(match_3.group(2)) == 8:
            number_1_pm_match_3 = match_3.group(2).replace("8", "20")

        if int(match_3.group(2)) == 9:
            number_1_pm_match_3 = match_3.group(2).replace("9", "21")

        if int(match_3.group(2)) == 10:
            number_1_pm_match_3 = match_3.group(2).replace("10", "22")

        if int(match_3.group(2)) == 11:
            number_1_pm_match_3 = match_3.group(2).replace("11", "23")

        if int(match_3.group(2)) == 12:
            number_1_pm_match_3 = match_3.group(2).replace("12", "00")

        return f"{number_1_pm_match_3} to {number_1_am_match_3}"

    elif match_4:

        number_1_am_match_4 = match_4.group(2)

        if int(match_4.group(2)) == 12:
            number_1_am_match_4 = match_4.group(2).replace("12", "00")

        if int(match_4.group(4)) == 1:
            number_1_pm_match_4 = match_4.group(4).replace("1", "13")

        if int(match_4.group(4)) == 2:
            number_1_pm_match_4 = match_4.group(4).replace("2", "14")

        if int(match_4.group(4)) == 3:
            number_1_pm_match_4 = match_4.group(4).replace("3", "15")

        if int(match_4.group(4)) == 4:
            number_1_pm_match_4 = match_4.group(4).replace("4", "16")

        if int(match_4.group(4)) == 5:
            number_1_pm_match_4 = match_4.group(4).replace("5", "17")

        if int(match_4.group(4)) == 6:
            number_1_pm_match_4 = match_4.group(4).replace("6", "18")

        if int(match_4.group(4)) == 7:
            number_1_pm_match_4 = match_4.group(4).replace("7", "19")

        if int(match_4.group(4)) == 8:
            number_1_pm_match_4 = match_4.group(4).replace("8", "20")

        if int(match_4.group(4)) == 9:
            number_1_pm_match_4 = match_4.group(4).replace("9", "21")

        if int(match_4.group(4)) == 10:
            number_1_pm_match_4 = match_4.group(4).replace("10", "22")

        if int(match_4.group(4)) == 11:
            number_1_pm_match_4 = match_4.group(4).replace("11", "23")

        if int(match_4.group(4)) == 12:
            number_1_pm_match_4 = match_4.group(4).replace("12", "00")

        return f"{number_1_am_match_4} to {number_1_pm_match_4}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
