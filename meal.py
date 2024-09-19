def main():
    time = input("What time is it? ")

    time = convert(time)

    print(time)


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()

main()
