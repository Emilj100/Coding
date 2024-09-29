import random



def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x, y = generate_integer(level)
        user_input = int(input(f"{x} + {y} = "))

        trys = 1

        for _ in range(3):
            if trys == 3:
                print(f"{x} + {y} = ", x + y, sep="")
            if not user_input == x + y and trys != 3:
                trys += 1
                print("EEE")
                user_input = int(input(f"{x} + {y} = "))

        if user_input == x + y:
            score += 1

    print(score)



def get_level():
    while True:
        try:
            user_input = int(input("Level: "))
            if user_input == 1 or user_input == 2 or user_input == 3:
                return user_input
        except ValueError:
            pass


def generate_integer(level):
    for _ in range(10):
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        else:
            raise ValueError
        return x, y


if __name__ == "__main__":
    main()
