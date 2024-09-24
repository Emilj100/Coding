while True:
    try:
        x, y = (input("Fraction: ").split("/"))
        x = int(x)
        y = int(y)
        procent = round((x / y) * 100)

        if x > y:
            pass
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
