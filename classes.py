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
            if name := re.fullmatch(r"[a-z]+", name, re.IGNORECASE):
                self._name = name
                break
            else:
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
                continue

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        while True:
            if age := re.fullmatch(r"[0-9]{1,2}(years old))


class Training:



class Calorie:
