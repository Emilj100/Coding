import sys
import csv
import re

# Dict til at have alle vores brugere.
users = []

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

    def get_all_users(self):
        with open("data.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                users.append({"name": row["name"], "gender": row["gender"], "height": row["height"], "age": row["age"], "weight": row["weight"], "goal": row["goal"], "training": row["training"]})

    @staticmethod
    def check_user(user_name):
        for row in users:
            if user_name in row["name"]:
                return True
        return False


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        while True:
            if name := re.fullmatch(r"[a-z]+", name, re.IGNORECASE):
                self._name = name
                break
            else:
                print("Invalid input: Please enter a valid name")
                continue

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        while True:
            if gender := re.fullmatch(r"male|female", gender, re.IGNORECASE):
                self._gender = gender
                break
            else:
                print('Invalid input: Please enter "Male" or "Female"')
                continue

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        while True:
            if height := re.fullmatch(r"[0-9]{3}( )?(cm)?", height, re.IGNORECASE):
                self._height = height
                break
            else:
                print("Invalid input: Please enter a valid height")
                continue

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        while True:
            if age := re.fullmatch(r"[0-9]{1,2}(years old)?", age, re.IGNORECASE):
                self._age = age
                break
            else:
                print("Invalid input: Please enter a valid age")
                continue

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        while True:
            if weight := re.fullmatch(r"[0-9,]{2,4}( )?(kg)?", weight, re.IGNORECASE):
                self._weight = weight
                break
            else:
                print("Invalid input: Please enter a valid weight")
                continue

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, goal):
        while True:
            if goal := re.fullmatch(r"1|2|3", goal):
                self._goal = goal
                break
            else:
                print("Invalid input: Please enter 1, 2 or 3")
                continue

    @property
    def training(self):
        return self._training

    @training.setter
    def training(self, training):
        while True:
            if training := re.fullmatch(r"1|2|3|4|5|6|7", training):
                self._training = training
                break
            else:
                print("Invalid input: Please enter 1, 2, 3, 4, 5, 6 or 7")
                continue

def main():
    User.get_all_users(self)
    user_name = input("What's your name? ")
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
        # Få data på brugeren og gem det i en CSV fil
        print(f"Welcome {user_name}! First we need some data to get the right program for you.")
        name = user_name
        gender = input("Male/Female: ")
        height = input("Height: ")
        age = input("Age: ")
        weight = input("Weight: ")

        print(f"\nNice {name}! Let us know a bit more about your goals and how many days you want to train per week.\n")
        goal = input("What is your goal?\n 1. To lose weight\n 2. Stay at my current weight\n 3. Gain weight\n (Enter 1,2 or 3)\n")
        training = input("How many days would you like to train per week?\n (Enter 1,2,3,4,5,6 or 7)\n")

        users[user_name] = User(name, gender, height, age, weight, goal, training)

main()
