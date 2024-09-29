import random
import sys




try:
    user_input = int(input("Level: "))
    number = random.randint(1, user_input)
    while True:

        if not user_input > 0:
            pass
        elif user_input > 0:
            guess = int(input("Level: "))
        elif user_input < number:
            print("Too small!")
            pass
        elif user_input > number:
            print("Too large!")
            pass
        else:
            print("Just right!")
            sys.exit()




except ValueError:
    pass
