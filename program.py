import sys
import csv

# Programmet spørger om brugerens navn
user_name = input("What's your name?")

# Liste til at tjekke om brugeren indtaster et valid input ved linje 11 og 56
user_options = ["1", "2", "3", "4", "5"]

# Programmet skal tjekke om brugerens navn allerede er i en csv fil med brugerens oplysninger.
with open("data.csv") as file:
    if user_name in file:
        while True:
            user_input = input("What would you like to do\n 1. track calories\n 2. See my trainingprogram and calorie intake\n 3. Update my data\n 4. Change my trainingprogram\n 5. Exit\n (Enter: 1,2,3,4 or 5)")

            if user_input == "1":
                    # Start track calories program
                    print("1")

            elif user_input == "2":
                    # Vis brugerens træningsprogrammer og calorie intake
                    print("2")

            elif user_input == "3":
                    # Giv brugeren mulighed for at opdatere sin data, som navn, vægt osv
                    print("3")

            elif user_input == "4":
                    # Bed brugeren om at indtaste hvor mange gange de ønsker at træne om ugen igen.
                    print("4")

            elif user_input == "5":
                # Exit programmet
                sys.exit("5")

            if user_input in user_options:
                break

    else:
        print("Welcome! First we need some data to get the right program for you")
        name = input("Name: ")
        gender = input("Male/Female: ")
        height = input("height: ")
        age = input("age: ")
        weight = input("weight: ")

        print(f"Nice {name}! Let us know a bit more about your goals and how many days you want to train per week.")
        goal = input("What is your goal?\n 1. To lose weight\n 2. Stay at my current weight\n 3. Gain weight\n (Enter 1,2 or 3)")
        training = input("How many days would you like to train per week?")

        print("Great! Thats all we needed. Here is your new program and calorie intake")

        with open("data.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "gender", "height", "age", "weight", "goal", "training"])
            writer.writerow({"name": name, "gender": gender, "height": height, "age": age, "weight": weight, "goal": goal, "training": training})

# Vis brugerens træningsprogram og calorie intake udfra de oplysninger de har skrevet.

# Herefter spørger vi brugeren om det samme som i det allerførste if statement, så det kører i loop indtil brugeren forlader programmet

    while True:
        user_input = input("What would you like to do\n 1. track calories\n 2. See my trainingprogram and calorie intake\n 3. Update my data\n 4. Change my trainingprogram\n 5. Exit\n (Enter: 1,2,3,4 or 5)")

        if user_input == "1":
                # Start track calories program
                print("1")

        elif user_input == "2":
                # Vis brugerens træningsprogrammer og calorie intake
                print("2")

        elif user_input == "3":
                # Giv brugeren mulighed for at opdatere sin data, som navn, vægt osv
                print("3")

        elif user_input == "4":
                # Bed brugeren om at indtaste hvor mange gange de ønsker at træne om ugen igen.
                print("4")

        elif user_input == "5":
            # Exit programmet
            sys.exit("5")

        if user_input in user_options:
            break
