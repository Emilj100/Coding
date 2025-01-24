import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
import re
import requests
import json

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///health.db")

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register-part1", methods=["GET", "POST"])
def registerpart1():
    if request.method == "POST":

        email = request.form.get("email")

        if not request.form.get("name"):
            return render_template("register-part1.html", error="Must provide Name")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return render_template("register-part1.html", error="Must provide valid email")
        elif not request.form.get("password") or not len(request.form.get("password")) >= 8:
            return render_template("register-part1.html", error="Password must be at least 8 characters long")
        elif request.form.get("password") != request.form.get("confirm_password"):
            return render_template("register-part1.html", error="Passwords must match")

        session["name"] = request.form.get("name")
        session["email"] = request.form.get("email")
        session["password"] = generate_password_hash(request.form.get("password"))

        return redirect("/register-part2")

    return render_template("register-part1.html")


@app.route("/register-part2", methods=["GET", "POST"])
def registerpart2():
    if request.method == "POST":

        try:
            age = int(request.form.get("age"))
        except ValueError:
            return render_template("register-part2.html", error="Please enter a valid number for age.")
        if not request.form.get("gender") in ["Male", "Female"]:
            return render_template("register-part2.html", error="Please select a valid gender")
        try:
            height = float(request.form.get("height"))
            weight = float(request.form.get("weight"))
            goal_weight = float(request.form.get("goal_weight"))
        except ValueError:
            return render_template("register-part2.html", error="Height, weight, and goal weight must be numbers")
        if not request.form.get("goal_type") in ["lose weight", "gain weight", "stay at current weight"]:
            return render_template("register-part2.html", error="Please select a valid goal")
        if not request.form.get("experience_level") in ["beginner", "intermediate", "advanced"]:
            return render_template("register-part2.html", error="Please select a valid experience level")
        try:
            training_days = int(request.form.get("training_days"))
            if not (1 <= training_days <= 7):
                return render_template("register-part2.html", error="Training days must be between 1 and 7.")
        except ValueError:
            return render_template("register-part2.html", error="Training days must be a number")

        if request.form.get("gender") == "Male":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        if (1 <= training_days <= 3):
            calorie_intake = bmr * 1.375
        elif (4 <= training_days <= 5):
            calorie_intake = bmr * 1.55
        else:
            calorie_intake = bmr * 1.725
        if request.form.get("goal_type") == "lose weight":
            calorie_intake = round(calorie_intake - 500)
        elif request.form.get("goal_type") == "gain weight":
            calorie_intake = round(calorie_intake + 500)

        try:
            user_id = db.execute(
                """
                INSERT INTO users (name, email, password, age, gender, height, weight, goal_weight, goal_type, training_days, experience_level, daily_calorie_goal)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                session["name"], session["email"], session["password"], age,
                request.form.get("gender"), height, weight, goal_weight,
                request.form.get("goal_type"), training_days, request.form.get("experience_level"), calorie_intake
            )

            session["user_id"] = user_id

        except ValueError:
            return render_template("register-part1.html", error="Email already exist")

        session.pop("name", None)
        session.pop("email", None)
        session.pop("password", None)
        return redirect("/")

    return render_template("register-part2.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")


        if not email:
            return render_template("login.html", error="Must provide email")
        elif not password:
            return render_template("login.html", error="Must provide password")

        rows = db.execute("SELECT * FROM users WHERE email = ?", email)

        if len(rows) != 1 or not check_password_hash(rows[0]["password"], password):
            return render_template("login.html", error="Invalid username and/or password")

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html", error=None)

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

@app.route("/calorietracker", methods=["GET", "POST"])
@login_required
def calorietracker():
    user_id = session["user_id"]

    # Fetch food log for the current day
    food_log = db.execute(
        """
        SELECT id, food_name, serving_qty, serving_unit, calories, proteins, carbohydrates, fats
        FROM food_log
        WHERE user_id = ? AND DATE(created_at) = DATE('now')
        """,
        user_id
    )

    # Fetch macros and calculate remaining calories
    def get_macros():
        return db.execute(
            """
            SELECT SUM(proteins) AS total_proteins,
                   SUM(carbohydrates) AS total_carbohydrates,
                   SUM(fats) AS total_fats,
                   SUM(calories) AS total_calories
            FROM food_log
            WHERE user_id = ? AND DATE(created_at) = DATE('now')
            """,
            user_id
        )[0]

    macros = get_macros()
    calorie_goal = db.execute("SELECT daily_calorie_goal FROM users WHERE id = ?", user_id)[0]["daily_calorie_goal"]
    total_consumed = macros["total_calories"] if macros["total_calories"] else 0
    remaining_calories = calorie_goal - total_consumed

    if request.method == "POST":
        action = request.form.get("action")

        if action == "add":  # Handling for adding food
            food_query = request.form.get("food")
            API_KEY = "6158963245cf646896228de0c3d0ba3a"
            APP_ID = "584633a6"

            url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
            headers = {
                "x-app-id": APP_ID,
                "x-app-key": API_KEY,
                "Content-Type": "application/json"
            }
            data = {"query": food_query}
            response = requests.post(url, headers=headers, json=data)

            failed_items = []  # Items not recognized

            if response.status_code == 200:
                nutrition_data = response.json()

                if "foods" in nutrition_data and nutrition_data["foods"]:
                    recognized_foods = [food["food_name"].lower() for food in nutrition_data["foods"]]

                    # Inputvarer splittet på komma
                    input_items = [item.strip().lower() for item in food_query.split(",")]

                    # Indsæt genkendte fødevarer i databasen
                    for food in nutrition_data["foods"]:
                        try:
                            db.execute(
                                """
                                INSERT INTO food_log (user_id, food_name, serving_qty, serving_unit, calories, proteins, carbohydrates, fats)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                                """,
                                user_id,
                                food["food_name"].title(),
                                food["serving_qty"],
                                food["serving_unit"],
                                food["nf_calories"],
                                food["nf_protein"],
                                food["nf_total_carbohydrate"],
                                food["nf_total_fat"]
                            )
                        except Exception:
                            pass  # Ignorer fejl under tilføjelse af fødevarer

                    # Tjek for ikke-genkendte varer
                    failed_items = [
                        item for item in input_items
                        if not any(recognized_food in item for recognized_food in recognized_foods)
                    ]
                else:
                    # Ingen fødevarer blev genkendt
                    failed_items = [item.strip() for item in food_query.split(",")]

            else:
                # API call failed
                return render_template(
                    "calorietracker.html",
                    food_log=food_log,
                    macros=macros,
                    total_consumed=round(total_consumed),
                    remaining_calories=round(remaining_calories),
                    calorie_goal=round(calorie_goal),
                    error="No valid food items were recognized. Please try again with specific food descriptions."
                )

            # Kun vis fejlbesked, hvis der er varer, der fejlede
            error = None
            if failed_items:
                error = f"The following items could not be processed: {', '.join(failed_items)}."

            # Opdater makrodata og food log efter tilføjelser
            food_log = db.execute(
                """
                SELECT id, food_name, serving_qty, serving_unit, calories, proteins, carbohydrates, fats
                FROM food_log
                WHERE user_id = ? AND DATE(created_at) = DATE('now')
                """,
                user_id
            )
            macros = get_macros()
            total_consumed = macros["total_calories"] if macros["total_calories"] else 0
            remaining_calories = calorie_goal - total_consumed

            # Always render the updated page
            return render_template(
                "calorietracker.html",
                food_log=food_log,
                macros=macros,
                total_consumed=round(total_consumed),
                remaining_calories=round(remaining_calories),
                calorie_goal=round(calorie_goal),
                error=error
            )

        elif action == "delete":  # Handling for deleting food
            food_id = request.form.get("food_id")
            db.execute("DELETE FROM food_log WHERE id = ? AND user_id = ?", food_id, user_id)

            # Opdater makrodata og genindlæs siden
            food_log = db.execute(
                """
                SELECT id, food_name, serving_qty, serving_unit, calories, proteins, carbohydrates, fats
                FROM food_log
                WHERE user_id = ? AND DATE(created_at) = DATE('now')
                """,
                user_id
            )
            macros = get_macros()
            total_consumed = macros["total_calories"] if macros["total_calories"] else 0
            remaining_calories = calorie_goal - total_consumed

            return redirect("/calorietracker")

    return render_template(
        "calorietracker.html",
        food_log=food_log,
        macros=macros,
        total_consumed=round(total_consumed),
        remaining_calories=round(remaining_calories),
        calorie_goal=round(calorie_goal)
    )


@app.route("/traininglog")
@login_required
def traininglog():
    return "traininglog page"

@app.route("/dashboard")
@login_required
def dashboard():
    return "dashboard page"

@app.route("/mealplan", methods=["GET", "POST"])
@login_required
def mealplan():
    user_id = session["user_id"]

    def select_data(user_id):
        meal_plans = db.execute(
            """
            SELECT id, name, calories, protein, carbohydrates, fat
            FROM meal_plans
            WHERE user_id = ?
            ORDER BY created_at DESC
            """,
            user_id
        )
        meals = db.execute(
            """
            SELECT meal_id, meal_plan_id, title, source_url, ready_in_minutes, recipe, imagetype
            FROM meal_plan_meals
            WHERE meal_plan_id IN (SELECT id FROM meal_plans WHERE user_id = ?)
            """,
            user_id
        )
        meals_by_plan = {}
        for meal in meals:
            meal_plan_id = meal["meal_plan_id"]
            if meal_plan_id not in meals_by_plan:
                meals_by_plan[meal_plan_id] = []
            meals_by_plan[meal_plan_id].append(meal)

        return meal_plans, meals_by_plan

    if request.method == "POST":
        if not request.form.get("plan_name"):
            return render_template("mealplan.html", error="Please enter a meal plan name")

        calorie_goal = db.execute("SELECT daily_calorie_goal FROM users WHERE id = ?", user_id)[0]["daily_calorie_goal"]

        api_key = "71433d93ff0445e68f984bb19ca3048f"
        url = "https://api.spoonacular.com/recipes/complexSearch"

        # Hent brugerens valg
        meal_types = ["breakfast", "lunch", "dinner"]  # Standard måltidstyper
        num_meals = int(request.form.get("meals_per_day", 5))  # Antal måltider om dagen

        meals_per_type = num_meals // len(meal_types)  # Fordel måltider ligeligt
        extra_meals = num_meals % len(meal_types)  # Fordel evt. overskydende måltider

        all_meals = []
        for i, meal_type in enumerate(meal_types):
            params = {
                "apiKey": api_key,
                "type": meal_type,
                "diet": request.form.get("diet"),
                "includeIngredients": request.form.get("preferences", "").strip(),
                "excludeIngredients": request.form.get("exclude", "").strip(),
                "intolerances": ",".join(request.form.getlist("intolerances")),
                "number": meals_per_type + (1 if i < extra_meals else 0),  # Tilføj ekstra måltid hvis der er overskud
                "maxCalories": calorie_goal // num_meals,  # Fordel kalorier jævnt
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                all_meals.extend(response.json().get("results", []))
            else:
                return render_template("mealplan.html", error=f"Failed to fetch {meal_type} recipes: {response.text}")

        if not all_meals:
            return render_template("mealplan.html", error="No meals found. Try again.")

        # Indsæt madplan
        meal_plan_id = db.execute(
            """
            INSERT INTO meal_plans (user_id, name, calories, protein, carbohydrates, fat)
            VALUES (?, ?, ?, 0, 0, 0)
            """,
            user_id, request.form.get("plan_name"), calorie_goal
        )

        # Indsæt måltider
        for meal in all_meals:
            db.execute(
                """
                INSERT INTO meal_plan_meals (meal_id, meal_plan_id, title, ready_in_minutes, recipe, imagetype)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                meal["id"], meal_plan_id, meal["title"], meal.get("readyInMinutes", 0), "Recipe unavailable", meal["imageType"]
            )

        meal_plans, meals_by_plan = select_data(user_id)
        return render_template("mealplan.html", meal_plans=meal_plans, meals_by_plan=meals_by_plan)

    else:
        meal_plans, meals_by_plan = select_data(user_id)
        return render_template("mealplan.html", meal_plans=meal_plans, meals_by_plan=meals_by_plan)





