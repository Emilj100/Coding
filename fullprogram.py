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

    def save_to_csv(self):
        with open("data.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "gender", "height", "age", "weight", "goal", "training"])
            writer.writerow({"name": self.name, "gender": self.gender, "height": self.height, "age": self.age, "weight": self.weight, "goal": self.goal, "training": self.training})

    @staticmethod
    def get_all_users():
        with open("data.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                users_name = row["name"]
                users[users_name] = ({"name": row["name"], "gender": row["gender"], "height": row["height"], "age": row["age"], "weight": row["weight"], "goal": row["goal"], "training": row["training"]})

    @staticmethod
    def check_user(user_name):
        for _ in users:
            if user_name in users:
                return True
        return False

def main():
    User.get_all_users()
    while True:
        user_name = input("What's your name? ")
        if user_name := re.fullmatch(r"[a-z]+", user_name, re.IGNORECASE):
            user_name = user_name.group()
            break
        else:
            print("Invalid input: Please enter a valid name")
            continue
    if User.check_user(user_name):
        #################### Find ud af hvordan du gør brug af brugerens objekt hvis han eksistere i programmet i forvejen
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
        create_user(user_name)



def create_user(user_name):
        # Få data på brugeren og gem det i en CSV fil
        print(f"Welcome {user_name}! First we need some data to get the right program for you.")
        name = user_name
        while True:
            gender = input("Male/Female: ")
            if gender := re.fullmatch(r"male|female", gender, re.IGNORECASE):
                gender = gender.group()
                break
            else:
                print('Invalid input: Please enter "Male" or "Female"')
                continue

        while True:
            height = input("Height: ")
            if height := re.fullmatch(r"[0-9]{3}( )?(cm)?", height, re.IGNORECASE):
                height = height.group()
                break
            else:
                print("Invalid input: Please enter a valid height")
                continue

        while True:
            age = input("Age: ")
            if age := re.fullmatch(r"[0-9]{1,2}(years old)?", age, re.IGNORECASE):
                age = age.group()
                break
            else:
                print("Invalid input: Please enter a valid age")
                continue

        while True:
            weight = input("Weight: ")
            if weight := re.fullmatch(r"[0-9,]{2,4}( )?(kg)?", weight, re.IGNORECASE):
                weight = weight.group()
                break
            else:
                print("Invalid input: Please enter a valid weight")
                continue
        print(f"\nNice {name}! Let us know a bit more about your goals and how many days you want to train per week.\n")

        while True:
            goal = input("What is your goal?\n 1. To lose weight\n 2. Stay at my current weight\n 3. Gain weight\n (Enter 1,2 or 3)\n")
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

        user = User(name, gender, height, age, weight, goal, training)
        user.save_to_csv()

        users[user_name] = user
main()
