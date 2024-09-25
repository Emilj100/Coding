month = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

while True:
    user_input = input("Date: ")
    if user_input.find("/") != -1:
        mm, dd, yyyy = user_input.strip().split("/")
        if mm.isalpha():
            continue
        mm = int(mm)
        dd = int(dd)
        if mm >= 13:
            continue
        if dd >= 32:
            continue
        else:
            print(f"{yyyy}-{mm:02}-{dd:02}")
            break
    else:
        mm, dd, yyyy = user_input.replace(",", "").strip().split(" ")
        if mm in month:
            mm = month[mm]
        if dd.isalpha():
            continue
        mm = int(mm)
        dd = int(dd)
        if dd >= 1 and dd <= 31:
            print(f"{yyyy}-{mm:02}-{dd:02}")
            break
        else:
            continue
