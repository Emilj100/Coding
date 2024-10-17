from datetime import date, datetime
import inflect
import sys

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "oktober", "november", "december"]

def main():
    date1 = today()
    date2 = user_input()


    days = date1 - date2
    days, useless= str(days).split(" days")
    minutes = int(days) * 24 * 60

    minutes = inflect.engine().number_to_words(int(minutes), andword="")
    print(f"{minutes.capitalize()} minutes")

def today():
    date_now = date.today()

    date_now_year, date_now_month, date_now_day = str(date_now).split("-")
    date1 = datetime(int(date_now_year), int(date_now_month), int(date_now_day))
    return date1


def user_input():
    try:
        user_date_year, user_date_month, user_date_day = input("Date of Birth: ").lower().split("-")
        date2 = datetime(int(user_date_year), int(user_date_month), int(user_date_day))
        return date2

    except ValueError:
        sys.exit("Wrong input")


if __name__ == "__main__":
    main()
