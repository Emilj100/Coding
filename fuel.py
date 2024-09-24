while True:
    try:
        x, y = (input("Fraction: ").split("/"))
        x = int(x)
        y = int(y)
        procent = round((x / y) * 100)

        if procent <= 1:
            print("E")
        if procent >= 99:
            print("F")

    except ValueError:
        ...
    except ZeroDivisionError:
        ...

    print(procent, "%", sep="")
