from datetime import date

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day





def main():
    user_date_year, user_date_month, user_date_day = input("Date of Birth: ").split("-")
    user_date = Date(user_date_year, user_date_month, user_date_day)
    date_now = date.today()
    date_now_year, date_now_month, date_now_day = date_now.split("-")
    print(date_now_year)




if __name__ == "__main__":
    main()
