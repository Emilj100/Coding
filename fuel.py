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
        if x > y:
            pass

    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        pass


    print(procent, "%", sep="")
