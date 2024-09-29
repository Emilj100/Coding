import random


def main():
    score = 0
    level = get_level()

    # Loop for 10 problems
    for _ in range(10):
        x, y = generate_integer(level)
        correct_answer = x + y
        attempts = 0

        # Give the user up to 3 attempts to guess correctly
        while attempts < 3:
            try:
                user_input = int(input(f"{x} + {y} = "))
                if user_input == correct_answer:
                    score += 1
                    break  # Exit loop if the answer is correct
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        # If the user fails 3 attempts, show the correct answer
        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")

    # Print final score
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass  # Keep prompting until a valid level is entered


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()
