import random
import sys



while True:
    try:
        user_input = int(input("Level: "))

        if not user_input > 0:
            pass
        elif user_input > 0:
            number = random.randint(1, user_input)
            guess = int(input("Guess: "))
        elif guess < number:
            print("Too small!")
            pass
        elif guess > number:
            print("Too large!")
            pass
        else:
            print("Just right!")
            sys.exit()




    except ValueError:
        pass
