import sys
import csv
import re

# Dict til at have alle vores brugere.
users = {}

# Liste til at tjekke om brugeren indtaster et valid input ved linje 11 og 56
user_options = ["1", "2", "3", "4", "5"]

class User:
    def __init__(self, name, gender, height, age, weight, goal, training):
        self.name = name
        self.gender = gender
        self.height = height
        self.age = age
        self.weight = weight
        self.goal = goal
        self.training = training

    # Gemmer nye brugere til vores csv. Bliver brugt i create_user funktionen
    def save_to_csv(self):
        with open("data.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "gender", "height", "age", "weight", "goal", "training"])
            writer.writerow({"name": self.name, "gender": self.gender, "height": self.height, "age": self.age, "weight": self.weight, "goal": self.goal, "training": self.training})

    # Når programmet starter bliver denne funktion kaldt. Den tager alle brugere fra CSV filen og indlæser dem i vores dict. Herefter kan vi tage den enkelte brugers objekt og gør brug af det hvis de allerede findes i programmet
    @staticmethod
    def get_all_users():
        with open("data.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                users_name = row["name"]
                users[users_name] = User(row["name"], row["gender"], row["height"], row["age"], row["weight"], row["goal"], row["training"])

    def show_user_data(self):
        if self.goal == "1":
            goal = "Lose weight"
        elif self.goal == "2":
            goal = "Stay at my current weight"
        elif self.goal == "3":
            goal = "Gain weight"
        return f"Name: {self.name}\nGender: {self.gender}\nHeight: {self.height}\nAge: {self.age}\nWeight: {self.weight}\nGoal: {goal}\nTraining: Training {self.training} times per week"


    # Denne funktion tjekker om brugeren allerede eksistere i programmet. Vi bruger den i starten af vores main funktion
    @staticmethod
    def check_user(user_name):
        for _ in users:
            if user_name in users:
                return True
        return False

    def calorie_intake(self):
        if self.gender == "male":
            bmr = (10 * int(self.weight)) + (6.25 * int(self.height)) - (5 * int(self.age)) + 5
        if self.gender == "female":
            bmr = (10 * int(self.weight)) + (6.25 * int(self.height)) - (5 * int(self.age)) - 161

        if self.training == "1" or self.training == "2" or self.training == "3":
            training_days = 1.375
        elif self.training == "4" or self.training == "5":
            training_days = 1.55
        elif self.training == "6" or self.training == "7":
            training_days = 1.725

        calorie_intake = int(bmr) * training_days

        if self.goal == "1":
            calorie_intake = calorie_intake - 500
        elif self.goal == "3":
            calorie_intake = calorie_intake + 500
        print(f"\nThis is your calorie intake: {calorie_intake:.2f} calories\n")


    def __str__(self):
        with open(self.training_program) as file:
           file = file.read()
           return file

    def give_training_program(self):
        if self.training == "1":
            training_program = "training_1.txt"
        elif self.training == "2":
            training_program = "training_2.txt"
        elif self.training == "3":
            training_program = "training_3.txt"
        elif self.training == "4":
            training_program = "training_4.txt"
        elif self.training == "5":
            training_program = "training_5.txt"
        elif self.training == "6":
            training_program = "training_6.txt"
        elif self.training == "7":
            training_program = "training_7.txt"
        self.training_program = training_program


def main():
    # Indlæser alle brugere fra CSV filen til vores dict så vi kan gøre brug af en eksisterende brugers objekt hvis der skulle komme behov for det.
    User.get_all_users()
    while True:
        user_name = input("What's your name? ")
        if user_name := re.fullmatch(r"[a-z]+", user_name, re.IGNORECASE):
            user_name = user_name.group()
            break
        else:
            print("Invalid input: Please enter a valid name")
            continue
    # Tjekker om det indtastede navn allerede eksistere i systemet
    if User.check_user(user_name):
        #################### Find ud af hvordan du gør brug af brugerens objekt hvis han eksistere i programmet i forvejen
        user_program_options(user_name)


    else:
        # Få data på brugeren og gem det i en CSV fil
        print(f"Welcome {user_name}! First we need some data to get the right program for you.")
                # Ved alle disse while True loops beder vi brugeren om inputs og tjekker efter fejl i brugerens input. Vi beder brugeren om at indtaste et input indtil de skriver et valid input.
        while True:
            gender = input("Male/Female: ").lower()
            if gender := re.fullmatch(r"male|female", gender, re.IGNORECASE):
                gender = gender.group()
                break
            else:
                print('Invalid input: Please enter "Male" or "Female"')
                continue
        # Funktion der opretter en ny bruger, hvis de ikke findes i systemet
        create_user(user_name, gender)
        user = User(name, gender, height, age, weight, goal, training)
        user.save_to_csv()

        users[user_name] = user

        print("Great! Here is your calorie intake and training program")

        user.calorie_intake()

        user.give_training_program()
        print(user)


def create_user(user_name, gender):
        name = user_name

        while True:
            height = input("Height: ")
            if height := re.fullmatch(r"([0-9]{3})( )?(cm)?", height, re.IGNORECASE):
                height = height.group(1)
                break
            else:
                print("Invalid input: Please enter a valid height")
                continue

        while True:
            age = input("Age: ")
            if age := re.fullmatch(r"([0-9]{1,2})(years old)?", age, re.IGNORECASE):
                age = age.group(1)
                break
            else:
                print("Invalid input: Please enter a valid age")
                continue

        while True:
            weight = input("Weight: ")
            if weight := re.fullmatch(r"([0-9,]{2,4})( )?(kg|kilo)?", weight, re.IGNORECASE):
                weight = weight.group(1)
                break
            else:
                print("Invalid input: Please enter a valid weight")
                continue

        print(f"\nNice {name}! Let us know a bit more about your goals and how many days you want to train per week.\n")

        while True:
            goal = input("What is your goal?\n 1. Lose weight\n 2. Stay at my current weight\n 3. Gain weight\n (Enter 1,2 or 3)\n")
            if goal := re.fullmatch(r"1|2|3", goal):
                goal = goal.group()
                break
            else:
                print("Invalid input: Please enter 1, 2 or 3")
                continue

        while True:
            training = input("How many days would you like to train per week?\n (Enter 1,2,3,4,5,6 or 7)\n")
            if training := re.fullmatch(r"1|2|3|4|5|6|7", training):
                training = training.group()
                break
            else:
                print("Invalid input: Please enter 1, 2, 3, 4, 5, 6 or 7")
                continue
        return 


def user_program_options(user_name):
    while True:

        current_user = users[user_name]

        user_input = input("What would you like to do\n 1. track calories\n 2. See my trainingprogram and calorie intake\n 3. Update my data\n 4. Change my trainingprogram\n 5. Exit\n (Enter: 1,2,3,4 or 5)")

        if user_input == "1":
             # Start track calories program
            print("1")

        elif user_input == "2":

            current_user.calorie_intake()

            current_user.give_training_program()
            print(current_user)

        elif user_input == "3":
            print("This is your current data:\n")
            print(current_user.show_user_data())
            print("Please enter your new data:\n")

        elif user_input == "4":
            # Bed brugeren om at indtaste hvor mange gange de ønsker at træne om ugen igen.
            print("4")

        elif user_input == "5":
            # Exit programmet
            sys.exit("Program ended")

        if user_input in user_options:
            break

main()
