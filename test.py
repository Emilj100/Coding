class Person:
    def __init__(self, name, age):
        # Initialiserer attributter for objektet
        self.name = name  # Tildeler værdien af 'name' til objektets 'name'-attribut
        self.age = age    # Tildeler værdien af 'age' til objektets 'age'-attribut

    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

# Opretter objekter af klassen Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Kalder metode på objekterne
print(person1.introduce())  # Output: Hi, my name is Alice and I am 30 years old.
print(person2.introduce())  # Output: Hi, my name is Bob and I am 25 years old.
