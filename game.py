import random
import sys


user_input = int(input("Level: "))

while True:
    try:
        user_input = int(input("Level: "))

        if not user_input > 0:
            pass

        if user_input > 0:
            number = random.randint(1, user_input)
            break

    except ValueError:
        pass


while True:
    try:
        guess = int(input("Guess: "))

        if guess < number:
            print("Too small!")
            pass
        if guess > number:
            print("Too large!")
            pass
        if guess == number:
            print("Just right!")
            sys.exit()




    except ValueError:
        pass
