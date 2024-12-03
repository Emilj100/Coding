def main():
    # Indhent gyldigt input fra brugeren
    cents = get_cents()

    # Beregn og print antallet af mønter
    coins = calculate_coins(cents)
    print(coins)


def get_cents():
    """Indhenter gyldigt beløb i dollars og konverterer det til cent."""
    while True:
        try:
            dollars = float(input("Change owed: "))
            if dollars > 0:
                return int(round(dollars * 100))
        except ValueError:
            pass  # Hvis brugeren ikke indtaster et tal, prøv igen


def calculate_coins(cents):
    """Beregner det mindste antal mønter."""
    coin_values = [25, 10, 5, 1]  # Quarters, dimes, nickels, pennies
    coins = 0

    for coin in coin_values:
        coins += cents // coin  # Find ud af hvor mange af denne mønt, der kan bruges
        cents %= coin           # Reducer cents med værdien af de brugte mønter

    return coins


if __name__ == "__main__":
    main()
