def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    a = d.removeprefix("$")

    z = float(a)

    int(z)

    return z


def percent_to_float(p):
    b = p.removeprefix("$")

    c = float(b)

    x = int() * int(c)

    return x



main()
