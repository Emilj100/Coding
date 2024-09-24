while True:
    try:
        x, y = (input("Fraction: ").split("/"))
        x = int(x)
        y = int(y)
        procent = round((x / y) * 100)

    except ValueError:
        ...
    except ZeroDivisionError:
        ...

    print(procent, "%", sep="")
