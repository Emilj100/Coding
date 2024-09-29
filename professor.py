import random


def main():
    level = get_level()
    random_integer = generate_integer(level)



def get_level():
    while True:
        user_input = int(input("Level: "))
        if user_input == 1 or user_input == 2 or user_input == 3:
            return user_input
        else:
            continue




def generate_integer(level):



if __name__ == "__main__":
    main()
