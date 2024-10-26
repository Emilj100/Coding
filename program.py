import sys

# Programmet spørger om brugerens navn
user_name = input("What's your name?")

# Liste til at tjekke om brugeren indtaster et valid input ved linje 11
user_options = ["1", "2", "3", "4", "5"]

# Programmet skal tjekke om brugerens navn allerede er i en csv fil med brugerens oplysninger (Brug evt. While True loop eller lign for at sikre at brugeren indtaster 1,2,3,4 eller 5. Tjek gerne dine noter for at finde ud af hvordan man).
if user_name in ...:
    while True:
        user_input = input("What would you like to do\n 1. track calories\n 2. See my trainingprogram and calorie intake\n 3. Update my data\n 4. Change my trainingprogram\n 5. Exit\n (Enter: 1,2,3,4 or 5)")
        if not user_input in user_options:
            break
        elif user_input == "1":
            # Start track calories program

        elif user_input == "2":
            # Vis brugerens træningsprogrammer og calorie intake

        elif user_input == "3":
            # Giv brugeren mulighed for at opdatere sin data, som navn, vægt osv

        elif user_input == "4":
            # Bed brugeren om at indtaste hvor mange gange de ønsker at træne om ugen igen.

        elif user_input == "5":
            # Exit programmet
            sys.exit()
        else:
            # Find ud af hvordan du beder brugeren om at indtaste igen indtil han indtaster et valid input

else:
    print("Welcome! First we need some data to get the right program for you")
    name = input("Name: ")
    gender = input("Male/Female: ")
    height = input("height: ")
    age = input("age: ")
    weight = input("weight: ")

    print("Nice! Let us know a bit more about your goals and how many days you want to train per week.")
    goal = input("What is your goal?\n 1. To lose weight\n 2. Stay at my current weight\n 3. Gain weight\n (Enter 1,2 or 3)")
    training_days = input("How many days would you like to train per week?")

    print("Great! Thats all we needed. Here is your new program and calorie intake")

# Vis brugerens træningsprogram og calorie intake udfra de oplysninger de har skrevet.

# Herefter spørger vi brugeren om det samme som i det allerførste if statement, så det kører i loop indtil brugeren forlader programmet

# Liste til at tjekke om brugeren indtaster et valid input ved linje 11
user_options = ["1", "2", "3", "4", "5"]

# Programmet skal tjekke om brugerens navn allerede er i en csv fil med brugerens oplysninger (Brug evt. While True loop eller lign for at sikre at brugeren indtaster 1,2,3,4 eller 5. Tjek gerne dine noter for at finde ud af hvordan man).
if user_name in ...:
    user_input = input("What would you like to do\n 1. track calories\n 2. See my trainingprogram and calorie intake\n 3. Update my data\n 4. Change my trainingprogram\n 5. Exit\n (Enter: 1,2,3,4 or 5)")
    if user_input in user_options:
        if user_input == "1":
            # Start track calories program

        elif user_input == "2":
            # Vis brugerens træningsprogrammer og calorie intake

        elif user_input == "3":
            # Giv brugeren mulighed for at opdatere sin data, som navn, vægt osv

        elif user_input == "4":
            # Bed brugeren om at indtaste hvor mange gange de ønsker at træne om ugen igen.

        elif user_input == "5":
            # Exit programmet
            sys.exit()
    else:
        # Find ud af hvordan du beder brugeren om at indtaste igen indtil han indtaster et valid input
