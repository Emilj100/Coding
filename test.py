import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regulært udtryk for at matche alle fire gyldige tidsformater
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

    # Udtræk timer og minutter fra regulære udtryksgrupper
    start_hour, start_minute, start_period = int(match.group(1)), match.group(2), match.group(3)
    end_hour, end_minute, end_period = int(match.group(4)), match.group(5), match.group(6)

    # Sæt minutter til '00', hvis de ikke er angivet
    start_minute = int(start_minute) if start_minute else 0
    end_minute = int(end_minute) if end_minute else 0

    # Tjek for gyldige timer og minutter
    if not (0 <= start_minute < 60 and 0 <= end_minute < 60):
        raise ValueError("Invalid minute value")
    if not (1 <= start_hour <= 12 and 1 <= end_hour <= 12):
        raise ValueError("Invalid hour value")

    # Konverter starttiden til 24-timers format
    start_hour = convert_to_24_hour(start_hour, start_period)
    end_hour = convert_to_24_hour(end_hour, end_period)

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

def convert_to_24_hour(hour, period):
    if period == 'AM' and hour == 12:
        return 0  # Midnat
    elif period == 'PM' and hour != 12:
        return hour + 12  # PM-konvertering til 24-timers format
    return hour

if __name__ == "__main__":
    main()
