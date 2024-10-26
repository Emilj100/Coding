import sys

user_options = ["1", "2", "3", "4", "5"]

while True:
    user_input = input("What would you like to do\n 1. track calories\n 2. See my trainingprogram and calorie intake\n 3. Update my data\n 4. Change my trainingprogram\n 5. Exit\n (Enter: 1,2,3,4 or 5)")

    elif user_input == "1":
            # Start track calories program
            print("1")

    elif user_input == "2":
            # Vis brugerens træningsprogrammer og calorie intake
            print("2")

    elif user_input == "3":
            # Giv brugeren mulighed for at opdatere sin data, som navn, vægt osv
            print("3")

    elif user_input == "4":
            # Bed brugeren om at indtaste hvor mange gange de ønsker at træne om ugen igen.
            print("4")

    elif user_input == "5":
        # Exit programmet
        sys.exit("5")
    
    if user_input in user_options:
          break

    # Find ud af hvordan du beder brugeren om at indtaste igen indtil han indtaster et valid input
