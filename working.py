import re
import sys


def main():
    convert(input("Hours: "))


def convert(s):
    match_1 = re.search(r"^([0-9:]+ AM) to ([0-9:]+ PM)$", s)
    match_2 = re.search(r"^([0-9:]+ PM) to ([0-9:]+ AM)$", s)


    if match_1:
        
    elif match_2:
        print("ja tak")
    else:
        raise ValueError("NEJ")





if __name__ == "__main__":
    main()
