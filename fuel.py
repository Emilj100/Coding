def main():
    fraction = (input("Fraction: "))
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > 100 or y > 100:
        raise ValueError
    elif x < 0 or y < 0:
        raise ValueError
    elif x > y:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    else:
        percentage = round((x / y) * 100)
        return percentage


def gauge(percentage):
    if percentage <= 1:
        return f"E"
    elif percentage >= 99:
        return f"F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()


