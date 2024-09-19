def main():
    user = input("What time is it? ")
    if breakfast(user):
        print("breakfast time")
    elif lunch(user):
        print("lunch time")
    elif dinner(user):
        print("dinner time")
    else:
        print("")


def breakfast(time):
    hours, minutes = time.split(":")
    if hours == "7" or "8":
        return True
    else:
        return False

def lunch(time):
    hours, minutes = time.split(":")
    if hours == "12" or "13":
        return True
    else:
        return False

def dinner(time):
    hours, minutes = time.split(":")
    if hours == "18" or "19":
        return True
    else:
        return False

main()
