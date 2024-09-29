import random


def main():
    level = get_level()
    print(level)



def get_level():
    while True:
        user_input = int(input("Level: "))
        if not user_input == 1 or user_input == 2 or user_input == 3:
            continue
        else:
            return user_input
        






if __name__ == "__main__":
    main()
