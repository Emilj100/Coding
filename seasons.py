from datetime import date

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __sub__(self, other):



def main():
    user_date_year, user_date_month, user_date_day = input("Date of Birth: ").split("-")
    user_date = Date(user_date_year, user_date_month, user_date_day)
    date_now =
    date_now = date(self.year, self.month, self.day)



if __name__ == "__main__":
    main()
