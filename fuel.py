def main():
    percentage = convert()
    




def convert(fraction):
    x, y = (input("Fraction: ").split("/"))
    x = int(x)
    y = int(y)
    if x or y > 100:
        raise ValueError
    elif x or y < 0:
        raise ValueError
    elif x > y:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    else:
        percentage = round((x / y) * 100)
        return percentage


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()


while True:
    try:
        x, y = (input("Fraction: ").split("/"))
        x = int(x)
        y = int(y)
        procent = round((x / y) * 100)

        if y == 0 or x > y:
            raise ValueError
        if procent <= 1:
            print("E")
            break
        if procent >= 99:
            print("F")
            break

    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        print(procent, "%", sep="")
        break
