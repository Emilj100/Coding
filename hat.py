from datetime import datetime, timedelta

# Opretter to datetime-objekter
date1 = datetime(2024, 10, 1)
date2 = datetime(2024, 10, 10)

# Beregner forskellen mellem datoerne
difference = date2 - date1
print(f"Difference between dates: {difference}")
print(f"Days: {difference.days}, Seconds: {difference.seconds}")
