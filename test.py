def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        percentage = round((x / y) * 100)

        return percentage
    except ValueError:
        raise ValueError("Invalid input. X and Y must be integers, and X must be less than or equal to Y.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Y cannot be 0.")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
