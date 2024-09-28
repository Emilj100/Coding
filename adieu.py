import random
import sys

number = random.randint(1,10)

while True:
    try:
        user_input = int(input("Level: "))

        if not user_input >= 0:
            pass
        elif user_input < number:
            print("Too small!")
            pass
        elif user_input > number:
            print("Too large!")
            pass
        else:
            print("Just right!")
            sys.exit




    except ValueError:
        pass

