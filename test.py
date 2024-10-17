from datetime import date
import inflect
import sys
import re


def main():
    birth_date = input("Date of Birth (YYYY-MM-DD): ").strip()
    print(age_in_minutes(birth_date))


def age_in_minutes(birth_date_str):
    # Regex til at sikre korrekt inputformat
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", birth_date_str):
        sys.exit("Invalid date")

    # Konverter fødselsdato til et date-objekt
    try:
        year, month, day = map(int, birth_date_str.split("-"))
        birth_date = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

    # Hent dagens dato
    today = date.today()

    # Beregn forskellen i dage
    delta = today - birth_date
    total_days = delta.days

    # Beregn antallet af minutter
    total_minutes = total_days * 24 * 60

    # Brug inflect til at konvertere tal til ord
    p = inflect.engine()
    minutes_in_words = p.number_to_words(total_minutes, andword="")

    # Returner resultatet
    return f"{minutes_in_words.capitalize()} minutes"


if __name__ == "__main__":
    main()
