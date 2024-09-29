import random
import sys


user_input = int(input("Level: "))

while True:
    try: 

    if not user_input > 0:
        user_input = int(input("Level: "))
        pass

    if user_input > 0:
        number = random.randint(1, user_input)
        break

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
