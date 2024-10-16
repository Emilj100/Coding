from datetime import date

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"


    def __sub__(self, other):
        year = self.year - other.year
        month = self.month - other.month
        day = self.day - other.day
        return Date(year, month, day)



def main():
    user_date_year, user_date_month, user_date_day = input("Date of Birth: ").split("-")
    user_date = Date(int(user_date_year), int(user_date_month), int(user_date_day))
    date_now = date.today()
    date_now_year, date_now_month, date_now_day = str(date_now).split("-")
    date_now = Date(int(date_now_year), int(date_now_month), int(date_now_day))
    minutes = date_now - user_date
    print(minutes)



if __name__ == "__main__":
    main()
