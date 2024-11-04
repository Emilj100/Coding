    # YOUR PROJECT TITLE
    #### Video Demo:  <URL HERE>
    #### Description:

    What can the program do?
    My program can help the user to get a custom training program based on how many days the user want to train per week. It can also calculate how many calories the user should eat per day based on the users goal and information.
    The program can also help the user track how many calories he/she has ben eating per day. Lets say the user has been eating 1 banana and 250 gram of chicken today. Then he can input this in the program and the program will tell the user how many calories, protein, carbohydrate and fat he/she has been eating today based on the users input. It is also possible for the user to change his/hers data, goals and traning program.

    My thoughts:
    When i started building this program I had 3 things i wanted to include in the program which is OOP, CSV/data and API. I wanted to include this since i believe it is very important to understand and very useful. I have never tried to code before and this is my first project and im proud of the result! CS50 python is also the first course that I have taken within coding.
    I listened to David's advice that you should build something which is interesting for you. I really like health and fitness, so I thought this would be a great idea.

    The programs structure:
    The program has 1 class, 1 main function and 3 other functions.
    Let me first explain how the class works:

    def __init__ which have all our attributes. For each object/user we want these informations: name, gender, height, age, weight, goal(If they want to lose weight or another goal), training(How many days they want to train per week)

    def save_to_csv which saves the users information to a CSV file

    def get_all_users which takes all of the users from the CSV file when the program starts and put them into a dict as a object

    def show_user_data which shows the users data if they want to see it/change it

    def check_user which check if the user is already exsisting in the program

    def calorie_intake which calculates the users calorie_intake based on the users information

    def __str__ and give_training_program which prints a training program based on how many times the user wants to train per week

    That was all our functions in the class. Lets move on to the main funktion.
    The main functions begins with get_all_users. This loads all the users from the CSV file to a dict, so we can use the users object later if we need it. After this we ask the user about his/hers name. Here we use regular expression to make sure that the user inputs a valid name. Afterwards we check if the user already exist in our dict. If the user exist we call the user_program_options function which shows the user the different things the program can do. If the program doesnt recognize the users name it will start to create an account for the user. Here we get the users information and make sure that the user inputs valid information with reagular expression.



