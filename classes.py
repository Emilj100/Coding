import re

class User:
    def __init__(self, name, gender, height, age, weight, goal, training)
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
            if name := re.fullmatch(r"[a-zA-Z]+"):
                self._name = name
                break
            else:
                continue


class Training:



class Calorie:
