import re

class User:
    def __init__(self, name, gender, height, age, weight, goal, training):
        self.name = name
        self.gender = gender
        self.height = height
        self.age = age
        self.weight = weight
        self.goal = goal
        self.training = training


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        while True:
            if name := re.fullmatch(r"[a-zA-Z]+", name):
                self._name = name
                break
            else:
                continue


    @property
    def gender(self):
        return self._gender

    @gender.setter
    def name(self, gender):
        while True:
            if gender := re.fullmatch(r"male|female", gender, re.IGNORECASE):

class Training:



class Calorie:
