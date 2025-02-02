import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
import re
import requests
import json
from datetime import datetime

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
        if not request.form.get("experience_level") in ["Beginner", "Intermediate", "Advanced"]:
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
                INSERT INTO users (name, email, password, age, gender, height, weight, start_weight, goal_weight, goal_type, training_days, experience_level, daily_calorie_goal)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
                """,
                session["name"].title(), session["email"], session["password"], age,
                request.form.get("gender"), height, weight, weight, goal_weight,
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


@app.route("/traininglog", methods=["GET", "POST"])
@login_required
def traininglog():
    user_id = session["user_id"]

    if request.method == "POST":
        # Hent day_id fra formen
        day_id = request.form.get("day_id")

        # Gem day_id i sessionen
        session["day_id"] = day_id

        # Redirect til trainingsession
        return redirect("/trainingsession")

    else:
        # Hent brugerdata
        user_data = db.execute(
            """
            SELECT training_days, experience_level
            FROM users
            WHERE id = ?
            """,
            user_id
        )

        # Hent programdata med sidste vægt fra LastSession
        raw_program_data = db.execute(
            """
            SELECT
                pd.id AS day_id,
                pd.day_number,
                pd.day_name,
                pe.exercise_name,
                pe.sets,
                pe.reps,
                COALESCE(ls.last_weight, pe.weight) AS weight
            FROM
                training_programs tp
            JOIN
                program_days pd ON tp.id = pd.program_id
            JOIN
                program_exercises pe ON pd.id = pe.day_id
            LEFT JOIN LastSession ls
                ON pe.exercise_name = ls.exercise_name
                AND ls.user_id = ?
                AND ls.day_id = pd.id
            WHERE
                tp.days_per_week = ? AND
                tp.experience_level = ?
            ORDER BY
                pd.day_number, pe.exercise_name
            """,
            user_id, user_data[0]["training_days"], user_data[0]["experience_level"]
        )

        # Gruppér dataen efter day_number
        program_data = {}
        for row in raw_program_data:
            day_number = row["day_number"]
            if day_number not in program_data:
                program_data[day_number] = {
                    "day_id": row["day_id"],
                    "day_name": row["day_name"],
                    "exercises": []
                }
            program_data[day_number]["exercises"].append({
                "exercise_name": row["exercise_name"],
                "sets": row["sets"],
                "reps": row["reps"],
                "weight": row["weight"]
            })

        # Hent træningshistorik fra `TrainingLogs`, kun de sidste 7 dage
        training_history = db.execute(
            """
            SELECT date, day_name, exercise_name, sets, reps, weight
            FROM TrainingLogs
            WHERE user_id = ? AND date >= DATE('now', '-7 days')
            ORDER BY DATE(date) DESC, id DESC
            """,
            user_id
        )


        return render_template("traininglog.html", program_data=program_data, training_history=training_history)




@app.route("/trainingsession", methods=["GET", "POST"])
@login_required
def trainingsession():
    user_id = session["user_id"]
    day_id = session.get("day_id")

    if not day_id:
        return redirect("/traininglog")  # Hvis ingen dag er valgt, send brugeren tilbage

    # 🔹 Intern funktion til at hente træningsdata
    def get_training_data(user_id, day_id):
        """
        Henter træningsdata for en given træningsdag inkl. sidste vægt fra LastSession.
        Returnerer en liste af øvelser og dagens info.
        """

        # Hent dagens navn
        day_info = db.execute(
            """
            SELECT day_number, day_name
            FROM program_days
            WHERE id = ?
            """,
            day_id
        )

        # Hent øvelsesdata inkl. seneste vægt fra LastSession
        exercises = db.execute(
            """
            SELECT
                pe.exercise_name,
                pe.sets,
                pe.reps,
                COALESCE(ls.last_weight, NULL) AS weight
            FROM program_exercises pe
            LEFT JOIN LastSession ls
                ON pe.exercise_name = ls.exercise_name
                AND ls.user_id = ?
                AND ls.day_id = pe.day_id
            WHERE pe.day_id = ?
            ORDER BY pe.exercise_name
            """,
            user_id, day_id
        )

        if not day_info:
            return None, None  # Hvis dag_id ikke findes

        return exercises, day_info[0]  # Returner listen af øvelser og dagens info

    if request.method == "POST":
        exercises, day_info = get_training_data(user_id, day_id)  # Hent træningsdata

        if not exercises or not day_info:
            return redirect("/traininglog")  # Hvis dagen ikke findes, redirect

        for exercise in exercises:
            exercise_name = exercise["exercise_name"]
            weight = request.form.get(exercise_name, type=float)

            if weight is None:
                continue  # Spring over, hvis brugeren ikke har indtastet en vægt

            # Indsæt træningen i `TrainingLogs`
            db.execute(
                """
                INSERT INTO TrainingLogs (user_id, date, day_id, day_name, exercise_name, sets, reps, weight)
                VALUES (?, DATE('now'), ?, ?, ?, ?, ?, ?)
                """,
                user_id, day_id, day_info["day_name"], exercise_name, exercise["sets"], exercise["reps"], weight
            )

            # Opdater eller indsæt i `LastSession`
            last_session_exists = db.execute(
                """
                SELECT last_weight FROM LastSession
                WHERE user_id = ? AND day_id = ? AND exercise_name = ?
                """,
                user_id, day_id, exercise_name
            )

            if last_session_exists:
                db.execute(
                    """
                    UPDATE LastSession
                    SET last_weight = ?
                    WHERE user_id = ? AND day_id = ? AND exercise_name = ?
                    """,
                    weight, user_id, day_id, exercise_name
                )
            else:
                db.execute(
                    """
                    INSERT INTO LastSession (user_id, day_id, exercise_name, last_weight)
                    VALUES (?, ?, ?, ?)
                    """,
                    user_id, day_id, exercise_name, weight
                )

        session.pop("day_id", None)  # Ryd sessionen efter træningen er afsluttet
        return redirect("/traininglog")

    else:
        exercises, day_info = get_training_data(user_id, day_id)  # Hent træningsdata

        if not exercises or not day_info:
            return redirect("/traininglog")  # Hvis dagen ikke findes, redirect

        return render_template(
            "training-session.html",
            training_data=exercises,
            day_info=day_info
        )




@app.route("/dashboard")
@login_required
def dashboard():

    return render_template("dashboard.html")

@app.route("/checkin", methods=["GET", "POST"])
@login_required
def checkin():
    user_id = session.get("user_id")

    if request.method == "POST":

        energy = request.form.get("energy")
        sleep = request.form.get("sleep")

        try:
            weight = float(request.form.get("weight"))
        except ValueError:
            return render_template("checkin.html", error="Weight must be a number")

        try:
            energy = int(energy)
            if not 1 <= energy <= 10:
                raise ValueError
        except ValueError:
            return render_template("checkin.html", error="Energy must be a number between 1 and 10.")

        try:
            sleep = float(sleep)
            if not 0 <= sleep <= 24:
                raise ValueError
        except ValueError:
            return render_template("checkin.html", error="Sleep must be a number between 0 and 24.")

        db.execute(
            "INSERT INTO check_ins (user_id, weight, energy, sleep) VALUES (?, ?, ?, ?)",
            user_id, weight, energy, sleep
        )

        return redirect("checkin")

    else:
        checkin_data = db.execute(
            "SELECT weight, energy, sleep, date(created_at) as created_at FROM check_ins WHERE user_id = ?",
            user_id
        )

        # Hent brugerens navn fra users tabellen
        user = db.execute("SELECT name FROM users WHERE id = ?", user_id)
        if user:
            user_name = user[0]["name"]
        else:
            user_name = "User"

        # Beregn gennemsnittene, hvis der er data
        if checkin_data:
            total_weight = sum(entry["weight"] for entry in checkin_data)
            total_energy = sum(entry["energy"] for entry in checkin_data)
            total_sleep  = sum(entry["sleep"] for entry in checkin_data)
            count = len(checkin_data)

            avg_weight = round(total_weight / count, 1)
            avg_energy = round(total_energy / count, 1)
            avg_sleep  = round(total_sleep / count, 1)
        else:
            avg_weight = avg_energy = avg_sleep = "No data yet"


        return render_template(
            "checkin.html",
            avg_weight=avg_weight,
            avg_energy=avg_energy,
            avg_sleep=avg_sleep,
            checkin_data=checkin_data,
            user_name=user_name
        )


@app.route("/weight")
@login_required
def weight_progress():
    user_id = session.get("user_id")

    # Hent alle check-ins for brugeren (sorteret kronologisk, ældste først)
    checkin_data = db.execute(
        "SELECT weight, date(created_at) as created_at FROM check_ins WHERE user_id = ? ORDER BY created_at ASC",
        user_id
    )

    # Hent brugerens oplysninger inkl. navn, start_weight, goal_weight og goal_type
    user = db.execute("SELECT name, start_weight, goal_weight, goal_type FROM users WHERE id = ?", user_id)
    if user:
        user_info   = user[0]
        user_name   = user_info["name"]
        start_weight = user_info.get("start_weight")  # Skal være numerisk
        goal_weight  = user_info.get("goal_weight")
        goal_type    = user_info.get("goal_type", "stay at current weight")
    else:
        user_name = "User"
        start_weight = None
        goal_weight = None
        goal_type = "stay at current weight"

    # Bestem current weight ud fra den seneste check-in
    if checkin_data:
        current_weight = checkin_data[-1]["weight"]
    else:
        current_weight = None

    default_text = "No data yet"

    # Beregn vægtændring (det, der skal vises i det midterste kort)
    if start_weight is not None and current_weight is not None:
        if goal_type.lower() == "lose weight":
            weight_change = round(start_weight - current_weight, 1)
        elif goal_type.lower() == "gain weight":
            weight_change = round(current_weight - start_weight, 1)
        elif goal_type.lower() == "stay at current weight":
            # Her beregner vi den faktiske afvigelse fra startvægten, som kan være både positiv eller negativ.
            weight_change = round(current_weight - start_weight, 1)
        else:
            weight_change = None
    else:
        weight_change = None

    if weight_change is not None:
        if weight_change > 0:
            # Hvis stigning (eller tab i tilfælde af lose, som burde være positivt)
            sign = "-" if goal_type.lower() == "lose weight" else "+"
            weight_change_display = sign + str(abs(weight_change))
        else:
            # Hvis der er et fald (eller negativ ændring ved gain)
            sign = "-" if goal_type.lower() == "lose weight" else "+"
            weight_change_display = sign + str(abs(weight_change))
    else:
        weight_change_display = default_text

    # Vælg et passende label afhængig af måltypen
    if goal_type.lower() == "lose weight":
        weight_change_label = "Weight Lost"
    elif goal_type.lower() == "gain weight":
        weight_change_label = "Weight Gain"
    elif goal_type.lower() == "stay at current weight":
        weight_change_label = "Weight Change"
    else:
        weight_change_label = "Weight Change"

    # Beregn gennemsnitlig ændring per uge baseret på hele perioden
    if checkin_data and start_weight is not None:
        first_entry = checkin_data[0]
        last_entry  = checkin_data[-1]
        try:
            first_date = datetime.strptime(first_entry["created_at"], "%Y-%m-%d")
            last_date  = datetime.strptime(last_entry["created_at"], "%Y-%m-%d")
        except Exception:
            first_date = last_date = datetime.now()

        diff_days = (last_date - first_date).days
        # Hvis perioden er mindre end 7 dage, antages det at dataene dækker 1 uge
        weeks = diff_days / 7 if diff_days >= 7 else 1

        if goal_type.lower() == "lose weight":
            total_change = start_weight - last_entry["weight"]
        elif goal_type.lower() == "gain weight":
            total_change = last_entry["weight"] - start_weight
        elif goal_type.lower() == "stay at current weight":
            total_change = last_entry["weight"] - start_weight
        else:
            total_change = 0

        avg_change_per_week = round(total_change / weeks, 1)
    else:
        avg_change_per_week = None

    if avg_change_per_week is not None:
        if avg_change_per_week > 0:
            sign = "-" if goal_type.lower() == "lose weight" else "+"
            avg_change_display = sign + str(abs(avg_change_per_week))
        else:
            sign = "-" if goal_type.lower() == "lose weight" else "+"
            avg_change_display = sign + str(abs(avg_change_per_week))
    else:
        avg_change_display = default_text



    # Beregn progress procent – hvor stor en del af målet der er opnået
    if start_weight is not None and goal_weight is not None and current_weight is not None:
        if goal_type.lower() == "lose weight":
            progress = ((start_weight - current_weight) / (start_weight - goal_weight)) * 100
        elif goal_type.lower() == "gain weight":
            progress = ((current_weight - start_weight) / (goal_weight - start_weight)) * 100
        elif goal_type.lower() == "stay at current weight":
            progress = 0
        else:
            progress = 0
        progress = min(max(round(progress, 1), 0), 100)
    else:
        progress = None

    # Beregn weight log: Sammenlign hvert check-in med det foregående for at udregne ændringen
    weight_log = []
    for i, entry in enumerate(checkin_data):
        if i == 0:
            change = "-"  # Ingen tidligere check-in
        else:
            prev_weight = checkin_data[i-1]["weight"]
            diff = round(entry["weight"] - prev_weight, 1)
            if diff > 0:
                change = f"+{diff}"
            else:
                change = f"{diff}"
        weight_log.append({
            "date": entry["created_at"],
            "weight": entry["weight"],
            "change": change
        })
    # Begræns weight log til de 10 seneste check-ins
    if len(weight_log) > 10:
        weight_log = weight_log[-10:]

    # Vælg grafdata: de 10 seneste check-ins (hvis der er mindst 10)
    graph_data = checkin_data[-10:] if len(checkin_data) >= 10 else checkin_data

    return render_template(
        "weight.html",
        user_name=user_name,
        current_weight=current_weight if current_weight is not None else default_text,
        weight_lost=weight_change_display,
        weight_change_label=weight_change_label,
        avg_loss_per_week=avg_change_display,
        progress=progress if progress is not None else 0,
        weight_log=weight_log,
        graph_data=graph_data,
        start_weight=start_weight if start_weight is not None else default_text,
        goal_weight=goal_weight if goal_weight is not None else default_text
    )

@app.route("/calories", methods=["GET"])
@login_required
def calories():
    user_id = session.get("user_id")

    # Hent brugerens daglige kaloriemål og navn
    user_data = db.execute("SELECT name, daily_calorie_goal FROM users WHERE id = ?", user_id)
    if user_data:
        user_name = user_data[0]["name"]
        calorie_goal = user_data[0]["daily_calorie_goal"]
    else:
        user_name = "User"
        calorie_goal = 0

    # Beregn start og slut for den aktuelle uge.
    # Eksempelvis: brug Python til at finde mandag og søndag for ugen
    from datetime import datetime, timedelta
    today = datetime.today()
    # Antag, at ugen starter mandag (weekday() = 0 for mandag)
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    start_str = start_of_week.strftime("%Y-%m-%d")
    end_str = end_of_week.strftime("%Y-%m-%d")

    # Hent aggregerede data for den aktuelle uge
    daily_data = db.execute(
        """
        SELECT DATE(created_at) AS day,
               SUM(calories) AS total_calories,
               SUM(proteins) AS total_proteins,
               SUM(carbohydrates) AS total_carbohydrates,
               SUM(fats) AS total_fats
        FROM food_log
        WHERE user_id = ? AND DATE(created_at) BETWEEN ? AND ?
        GROUP BY day
        ORDER BY day ASC
        """,
        user_id, start_str, end_str
    )

    # Udregn nøgletal
    if daily_data:
        total_calories_week = sum([row["total_calories"] for row in daily_data])
        average_daily_intake = round(total_calories_week / len(daily_data), 1)
        total_proteins_week = sum([row["total_proteins"] for row in daily_data])
        avg_protein_intake = round(total_proteins_week / len(daily_data), 1)
    else:
        average_daily_intake = "No data yet"
        avg_protein_intake = "No data yet"

    # Beregn Planned vs. Actual for i dag (hvis data findes)
    today_data = db.execute(
        "SELECT SUM(calories) AS today_calories FROM food_log WHERE user_id = ? AND DATE(created_at) = DATE('now')",
        user_id
    )
    today_calories = today_data[0]["today_calories"] if today_data and today_data[0]["today_calories"] is not None else 0
    planned_vs_actual = calorie_goal - today_calories

    # Beregn Best & Worst Day for ugen
    best_day = min(daily_data, key=lambda row: row["total_calories"]) if daily_data else None
    worst_day = max(daily_data, key=lambda row: row["total_calories"]) if daily_data else None

    return render_template(
        "calories.html",
        user_name=user_name,
        average_daily_intake=average_daily_intake,
        planned_vs_actual=planned_vs_actual,
        calorie_goal=calorie_goal,
        avg_protein_intake=avg_protein_intake,
        daily_data=daily_data,
        best_day=best_day,
        worst_day=worst_day,
        start_of_week=start_str,
        end_of_week=end_str
    )



@app.route("/training")
@login_required
def training():

    return render_template("training.html")

@app.route("/settings")
@login_required
def settings():

    return render_template("settings.html")



@app.route("/mealplan", methods=["GET", "POST"])
@login_required
def mealplan():
    user_id = session["user_id"]

    # Maksimale grænser for makronæringsstoffer
    MAX_PROTEIN = 125
    MAX_CARBS = 250
    MAX_FAT = 87

    def select_data(user_id):
        # Hent alle madplaner
        meal_plans = db.execute(
            """
            SELECT id, name, calories, protein, carbohydrates, fat
            FROM meal_plans
            WHERE user_id = ?
            ORDER BY created_at DESC
            """,
            user_id
        )

        # Hent alle måltider for de madplaner
        meals = db.execute(
            """
            SELECT meal_id, meal_plan_id, title, source_url, ready_in_minutes, imagetype
            FROM meal_plan_meals
            WHERE meal_plan_id IN (SELECT id FROM meal_plans WHERE user_id = ?)
            """,
            user_id
        )

        # Organiser måltiderne pr. madplan
        meals_by_plan = {}
        for meal in meals:
            meal_plan_id = meal["meal_plan_id"]
            if meal_plan_id not in meals_by_plan:
                meals_by_plan[meal_plan_id] = []
            meals_by_plan[meal_plan_id].append(meal)

        return meal_plans, meals_by_plan

    def calculate_macronutrients(calorie_goal, goal_type):
        """Beregner minimum protein, kulhydrat og fedt baseret på mål og kalorieindtag."""
        if goal_type == "weight_loss":
            protein_ratio, carb_ratio, fat_ratio = 0.35, 0.30, 0.35
        elif goal_type == "muscle_gain":
            protein_ratio, carb_ratio, fat_ratio = 0.40, 0.40, 0.20
        else:  # maintenance
            protein_ratio, carb_ratio, fat_ratio = 0.30, 0.40, 0.30

        protein = min(calorie_goal * protein_ratio / 4, MAX_PROTEIN)  # 1 gram protein = 4 kcal
        carbs = min(calorie_goal * carb_ratio / 4, MAX_CARBS)        # 1 gram kulhydrat = 4 kcal
        fat = min(calorie_goal * fat_ratio / 9, MAX_FAT)             # 1 gram fedt = 9 kcal
        return round(protein), round(carbs), round(fat)

    if request.method == "POST":
        action = request.form.get("action")

        if action == "delete":
            plan_id = request.form.get("plan_id")
            if plan_id:
                # Slet madplan og tilknyttede måltider
                db.execute("DELETE FROM meal_plan_meals WHERE meal_plan_id = ?", plan_id)
                db.execute("DELETE FROM meal_plans WHERE id = ? AND user_id = ?", plan_id, user_id)

        elif action == "add":
            # Valider "plan_name"
            if not request.form.get("plan_name"):
                return render_template("mealplan.html", error="Please enter a meal plan name.")

            # Hent brugerens kaloriebudget og mål
            user_data = db.execute("SELECT daily_calorie_goal, goal_type FROM users WHERE id = ?", user_id)[0]
            calorie_goal = user_data["daily_calorie_goal"]

            MAX_CALORIES = 3443
            if calorie_goal > MAX_CALORIES:
                calorie_goal = MAX_CALORIES  # Begræns til 3443 kalorier
                error_message = (
                    "Your daily calorie goal exceeds the maximum we can generate a plan for (3440 kcal). "
                    "We have created a plan with the highest available calorie value."
                )
            else:
                error_message = None

            goal_type = user_data["goal_type"]

            # Beregn makronæringsstoffer for hele planen og fordel dem
            total_protein, total_carbs, total_fat = calculate_macronutrients(calorie_goal, goal_type)
            meal_protein = round(total_protein / 3 * 0.70)
            meal_carbs = round(total_carbs / 3 * 0.70)
            meal_fat = round(total_fat / 3 * 0.70)
            calorie_goal = calorie_goal / 3

            # Spoonacular API-opkald for morgenmad, frokost og aftensmad
            api_key = "71433d93ff0445e68f984bb19ca3048f"
            meal_types = ["breakfast", "main course", "main course"]
            meals = []
            total_calories = 0
            total_protein = 0
            total_carbs = 0
            total_fat = 0
            offset = 0

            for meal_type in meal_types:
                url = "https://api.spoonacular.com/recipes/complexSearch"
                # Tilpas params baseret på diet
                params = {
                    "apiKey": api_key,
                    "type": meal_type,
                    "minCalories": min(calorie_goal - 100, 1100),  # Fordel kalorierne på tre måltider
                    "maxCalories": min(calorie_goal + 100, 1300),
                    "addRecipeNutrition": True,
                    "number": 1,
                    "offset": offset,
                    "instructionsRequired": True,
                    "minProtein": meal_protein,
                    "minCarbs": meal_carbs,
                    "minFat": meal_fat
                }




                response = requests.get(url, params=params)
                if response.status_code == 200:
                    result = response.json().get("results", [])

                    if result:
                        meal = result[0]
                        meals.append(meal)
                        offset += 1

                        # Udtræk faktisk næringsindhold
                        nutrients = meal.get("nutrition", {}).get("nutrients", [])
                        total_calories += next((n["amount"] for n in nutrients if n["name"] == "Calories"), 0)
                        total_protein += next((n["amount"] for n in nutrients if n["name"] == "Protein"), 0)
                        total_carbs += next((n["amount"] for n in nutrients if n["name"] == "Carbohydrates"), 0)
                        total_fat += next((n["amount"] for n in nutrients if n["name"] == "Fat"), 0)

                else:
                    return render_template("mealplan.html", error=f"Failed to fetch {meal_type}. Try again.")

            if not meals or len(meals) != 3:
                return render_template("mealplan.html", error="Could not generate a complete meal plan. Try again.")

            # Indsæt madplan
            meal_plan_id = db.execute(
                """
                INSERT INTO meal_plans (user_id, name, calories, protein, carbohydrates, fat)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                user_id, request.form.get("plan_name"), round(total_calories), round(total_protein), round(total_carbs), round(total_fat)
            )

            # Indsæt måltider
            for meal in meals:
                db.execute(
                    """
                    INSERT INTO meal_plan_meals (meal_id, meal_plan_id, title, source_url, ready_in_minutes, imagetype)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    meal["id"], meal_plan_id, meal["title"], meal["sourceUrl"], meal.get("readyInMinutes", 0), meal["imageType"]
                )

        # Hent opdaterede data
        meal_plans, meals_by_plan = select_data(user_id)
        return render_template("mealplan.html", meal_plans=meal_plans, meals_by_plan=meals_by_plan, error=error_message)

    else:  # GET request
        meal_plans, meals_by_plan = select_data(user_id)
        return render_template("mealplan.html", meal_plans=meal_plans, meals_by_plan=meals_by_plan)

