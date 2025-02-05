import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
import re
import requests
import json
from datetime import datetime, timedelta

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
            SELECT DATE(created_at) AS created_at, day_name, exercise_name, sets, reps, weight
            FROM TrainingLogs
            WHERE user_id = ? AND DATE(created_at) >= DATE('now', '-7 days')
            ORDER BY DATE(created_at) DESC, id DESC
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

    def get_training_data(user_id, day_id):
        day_info = db.execute(
            """
            SELECT day_number, day_name
            FROM program_days
            WHERE id = ?
            """,
            day_id
        )
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
            return None, None
        return exercises, day_info[0]

    if request.method == "POST":
        exercises, day_info = get_training_data(user_id, day_id)
        if not exercises or not day_info:
            return redirect("/traininglog")

        # Generer ét tidsstempel for hele sessionen
        session_ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for exercise in exercises:
            exercise_name = exercise["exercise_name"]
            weight = request.form.get(exercise_name, type=float)
            if weight is None:
                continue
            # Indsæt træningen i TrainingLogs med det fælles tidsstempel
            db.execute(
                """
                INSERT INTO TrainingLogs (user_id, day_id, day_name, exercise_name, sets, reps, weight, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                user_id, day_id, day_info["day_name"], exercise_name, exercise["sets"], exercise["reps"], weight, session_ts
            )
            # Opdater eller indsæt i LastSession
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
        session.pop("day_id", None)
        return redirect("/traininglog")

    else:
        exercises, day_info = get_training_data(user_id, day_id)
        if not exercises or not day_info:
            return redirect("/traininglog")
        return render_template("training-session.html", training_data=exercises, day_info=day_info)



@app.route("/api/fitness_coach", methods=["POST"])
def fitness_coach():

    data = request.get_json()

    # Hent hele messages-listen fra klientsiden
    # (fx 0..10 beskeder, plus en client-side system prompt, hvis du vil).
    messages = data.get("messages", [])

    # Din system-prompt – f.eks. en mere detaljeret beskrivelse af sidens funktioner:
    system_prompt = (
        "You are a friendly and knowledgeable AI Fitness Coach on an English-language health and fitness website. "
        "The website allows users to:\n"
        "1. Track their daily calorie intake.\n"
        "2. Generate personalized workout plans.\n"
        "3. Log and monitor their workouts (exercises, sets, reps, etc.).\n"
        "4. Receive meal plans matching their calorie needs.\n"
        "5. Provide initial user data upon registration (name, email, password, age, weight, height, goal weight, gender, goal (lose weight, gain weight or maintain weight), Training experience level and training days per week).\n"
        "6. See a personalized dashboard with weekly calorie intake, weight progress, workout frequency, and daily/weekly check-ins.\n\n"
        "Behavior and style:\n"
        "1. Always be clear, concise, and supportive.\n"
        "2. Provide helpful suggestions on training, nutrition, or goal-setting within your knowledge.\n"
        "3. Avoid strict medical advice beyond general fitness.\n"
        "4. Respond in English unless otherwise requested.\n"
        "5. Keep answers relatively short and practical."
    )

    # Vi indsætter system-prompten øverst i messages-listen,
    # så OpenAI altid får at vide, hvordan den skal opføre sig.
    messages.insert(0, {"role": "system", "content": system_prompt})

    # Hent din OpenAI API-nøgle fra environment-variabel
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        return jsonify({"reply": "No OpenAI API key found on the server."}), 500

    # Forbered API-kald
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    payload = {
        "model": "gpt-4",  # Skift til fx "gpt-3.5-turbo" hvis du ønsker
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 150
    }

    try:
        openai_response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload
        )
        openai_response.raise_for_status()  # Fejl hvis status != 200
        response_data = openai_response.json()
        reply = response_data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Error calling OpenAI API:", e)
        reply = "I'm sorry, I couldn't process your request at the moment."

    return jsonify({"reply": reply})



@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    user_id = session.get("user_id")

    # Hent brugeroplysninger fra users-tabellen
    user_data = db.execute("SELECT * FROM users WHERE id = ?", user_id)
    if not user_data:
        return render_template("dashboard.html", error="User not found.", user={})
    user = user_data[0]
    user_name = user.get("name", "User")

    # 1. Seneste Check-in Vægt (fra check_ins)
    latest_checkin_data = db.execute(
        "SELECT weight, created_at FROM check_ins WHERE user_id = ? ORDER BY created_at DESC LIMIT 1",
        user_id
    )
    if latest_checkin_data:
        latest_weight = latest_checkin_data[0]["weight"]
    else:
        latest_weight = "No data yet"

    # 2. Average Caloric Intake for current week (samme som i calories-ruten)
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())  # Mandag
    start_str = start_of_week.strftime("%Y-%m-%d")
    daily_data = db.execute(
        """
        SELECT DATE(created_at) AS day,
               SUM(calories) AS total_calories
        FROM food_log
        WHERE user_id = ?
          AND DATE(created_at) BETWEEN ? AND DATE('now', 'localtime')
          AND DATE(created_at) < DATE('now', 'localtime')
        GROUP BY day
        ORDER BY day ASC
        """,
        user_id, start_str
    )
    if daily_data:
        total_calories_week = sum(row["total_calories"] for row in daily_data)
        average_caloric_intake = round(total_calories_week / len(daily_data), 1)
    else:
        average_caloric_intake = "No data yet"

    # 3. Workouts This Week (fra TrainingLogs)
    sessions_data = db.execute(
        """
        SELECT COUNT(DISTINCT created_at) AS session_count
        FROM TrainingLogs
        WHERE user_id = ?
          AND DATE(created_at) BETWEEN ? AND DATE('now', 'localtime')
        """,
        user_id, start_str
    )
    total_sessions = sessions_data[0]["session_count"] if sessions_data else 0

    # 4. Progress Towards Weight Goal
    start_weight = user.get("start_weight")
    goal_weight = user.get("goal_weight")
    goal_type = user.get("goal_type", "stay at current weight")
    # Hvis der ikke er check-in data, benyt den gemte vægt
    current_weight = latest_weight if latest_weight != "No data yet" else user.get("weight")
    progress = 0
    if start_weight and goal_weight and current_weight:
        if goal_type.lower() == "lose weight":
            progress = ((start_weight - current_weight) / (start_weight - goal_weight)) * 100
        elif goal_type.lower() == "gain weight":
            progress = ((current_weight - start_weight) / (goal_weight - start_weight)) * 100
        elif goal_type.lower() == "stay at current weight":
            progress = 0
        progress = min(max(round(progress, 1), 0), 100)

    # 5. Weight Progress Graph – brug de seneste 10 check-ins (fra start til nu)
    checkin_history = db.execute(
        "SELECT weight, DATE(created_at) as created_at FROM check_ins WHERE user_id = ? ORDER BY created_at ASC",
        user_id
    )
    graph_data = checkin_history[-10:] if len(checkin_history) >= 10 else checkin_history
    weight_labels = [entry["created_at"] for entry in graph_data]
    weight_values = [entry["weight"] for entry in graph_data]

    # 6. Caloric Intake Chart – Current Week
    calorie_days = []
    calorie_values = []
    for row in daily_data:
        try:
            dt = datetime.strptime(row["day"], "%Y-%m-%d")
            weekday = dt.strftime("%A")
        except Exception:
            weekday = row["day"]
        calorie_days.append(weekday)
        calorie_values.append(row["total_calories"])
    calorie_goal = user.get("daily_calorie_goal", 0)

    return render_template(
        "dashboard.html",
        user_name=user_name,
        latest_weight=latest_weight,
        average_caloric_intake=average_caloric_intake,
        total_sessions=total_sessions,
        progress=progress,
        weight_labels=weight_labels,
        weight_values=weight_values,
        calorie_days=calorie_days,
        calorie_values=calorie_values,
        calorie_goal=calorie_goal,
        start_of_week=start_str
    )



@app.route("/checkin", methods=["GET", "POST"])
@login_required
def checkin():
    user_id = session.get("user_id")

    if request.method == "POST":
        energy = request.form.get("energy")
        sleep = request.form.get("sleep")

        # Valider og konverter vægt
        try:
            weight = float(request.form.get("weight"))
        except ValueError:
            return render_template("checkin.html", error="Weight must be a number")

        # Valider energy
        try:
            energy = int(energy)
            if not 1 <= energy <= 10:
                raise ValueError
        except ValueError:
            return render_template("checkin.html", error="Energy must be a number between 1 and 10.")

        # Valider sleep
        try:
            sleep = float(sleep)
            if not 0 <= sleep <= 24:
                raise ValueError
        except ValueError:
            return render_template("checkin.html", error="Sleep must be a number between 0 and 24.")

        # Indsæt check-in data i check_ins tabellen
        db.execute(
            "INSERT INTO check_ins (user_id, weight, energy, sleep) VALUES (?, ?, ?, ?)",
            user_id, weight, energy, sleep
        )

        # Hent eksisterende brugerdata fra users tabellen
        user_data = db.execute("SELECT age, gender, height, training_days, goal_type FROM users WHERE id = ?", user_id)
        if not user_data:
            return render_template("checkin.html", error="User not found")
        user = user_data[0]

        # Udregn BMR med den nye vægt
        age = user["age"]
        gender = user["gender"]
        height = float(user["height"])
        training_days = int(user["training_days"])
        goal_type = user["goal_type"]

        if gender == "Male":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

        # Udregn kalorieindtag baseret på antallet af træningsdage
        if 1 <= training_days <= 3:
            calorie_intake = bmr * 1.375
        elif 4 <= training_days <= 5:
            calorie_intake = bmr * 1.55
        else:
            calorie_intake = bmr * 1.725

        # Juster kalorieindtaget ud fra goal_type
        if goal_type == "lose weight":
            calorie_intake = round(calorie_intake - 500)
        elif goal_type == "gain weight":
            calorie_intake = round(calorie_intake + 500)
        else:
            calorie_intake = round(calorie_intake)

        # Opdater brugerens record med den nye vægt og det nye daglige kalorieindtag
        db.execute(
            "UPDATE users SET weight = ?, daily_calorie_goal = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            weight, calorie_intake, user_id
        )

        return redirect("/checkin")

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

    # Hent brugerens daglige kalorie-mål og navn
    user_data = db.execute("SELECT name, daily_calorie_goal FROM users WHERE id = ?", user_id)
    if user_data:
        user_name = user_data[0]["name"]
        calorie_goal = user_data[0]["daily_calorie_goal"]
    else:
        user_name = "User"
        calorie_goal = 0

    from datetime import datetime, timedelta
    today = datetime.today()
    # Beregn start på ugen (antag at ugen starter mandag)
    start_of_week = today - timedelta(days=today.weekday())
    start_str = start_of_week.strftime("%Y-%m-%d")

    # I stedet for at beregne en fast slutdato (f.eks. i går) kan vi bruge:
    # Vi henter alle data, hvor datoen er før i dag
    # Dette sikrer, at kun fuldførte dage medtages.

    daily_data = db.execute(
        """
        SELECT DATE(created_at) AS day,
               SUM(calories) AS total_calories,
               SUM(proteins) AS total_proteins,
               SUM(carbohydrates) AS total_carbohydrates,
               SUM(fats) AS total_fats
        FROM food_log
        WHERE user_id = ?
          AND DATE(created_at) BETWEEN ? AND DATE('now', 'localtime')
          AND DATE(created_at) < DATE('now', 'localtime')
        GROUP BY day
        ORDER BY day ASC
        """,
        user_id, start_str
    )

    # Hvis der kun er data fra en del af ugen (f.eks. kun én hel dag), så bruges denne dag.
    # Udregn nøgletal for de dage, der er komplette (dvs. før i dag)
    if daily_data:
        total_calories_week = sum([row["total_calories"] for row in daily_data])
        average_daily_intake = round(total_calories_week / len(daily_data), 1)
        total_proteins_week = sum([row["total_proteins"] for row in daily_data])
        avg_protein_intake = round(total_proteins_week / len(daily_data), 1)
    else:
        average_daily_intake = "No data yet"
        avg_protein_intake = "No data yet"

    # Planned vs. Actual: Her kan du f.eks. udregne for den seneste fuldførte dag (det vil sige den seneste dag i daily_data)
    if daily_data:
        latest_day_data = daily_data[-1]
        actual_intake = latest_day_data["total_calories"]
    else:
        actual_intake = 0
    planned_vs_actual = calorie_goal - actual_intake

    # Best & Worst Day: Brug de komplette dage (brug evt. ugedag i stedet for dato)
    from datetime import datetime
    for row in daily_data:
        try:
            dt = datetime.strptime(row["day"], "%Y-%m-%d")
            row["weekday"] = dt.strftime("%A")
        except Exception:
            row["weekday"] = row["day"]

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
        start_of_week=start_str
    )


@app.route("/training", methods=["GET"])
@login_required
def training():
    user_id = session.get("user_id")

    # Beregn start og slut for ugen (mandag til søndag)
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())  # Mandag i denne uge
    end_of_week = start_of_week + timedelta(days=6)            # Søndag i denne uge
    start_str = start_of_week.strftime("%Y-%m-%d")
    end_str = end_of_week.strftime("%Y-%m-%d")

    # Hjælpefunktion: konverter ugekode til datointerval
    def format_week_range(week_label):
        dt = datetime.strptime(week_label + '-1', "%Y-%W-%w")
        week_start = dt.strftime("%Y-%m-%d")
        week_end = (dt + timedelta(days=6)).strftime("%Y-%m-%d")
        return f"{week_start} - {week_end}"

    # Total sessions this week (tæl distinkte created_at)
    sessions = db.execute(
        """
        SELECT COUNT(DISTINCT created_at) AS session_count
        FROM TrainingLogs
        WHERE user_id = ?
          AND DATE(created_at) BETWEEN ? AND DATE('now', 'localtime')
        """,
        user_id, start_str
    )
    total_sessions = sessions[0]["session_count"] if sessions else 0

    # Total sets this week
    sets_data = db.execute(
        """
        SELECT SUM(sets) AS total_sets
        FROM TrainingLogs
        WHERE user_id = ?
          AND DATE(created_at) BETWEEN ? AND DATE('now', 'localtime')
        """,
        user_id, start_str
    )
    total_sets = sets_data[0]["total_sets"] if sets_data and sets_data[0]["total_sets"] is not None else 0

    # Average weight increase (sammenlign den aktuelle uge med forrige uge)
    last_week_start = start_of_week - timedelta(days=7)
    last_week_end   = start_of_week - timedelta(days=1)
    last_start_str  = last_week_start.strftime("%Y-%m-%d")
    last_end_str    = last_week_end.strftime("%Y-%m-%d")

    current_weights = db.execute(
        """
        SELECT exercise_name, AVG(weight) AS avg_weight
        FROM TrainingLogs
        WHERE user_id = ?
          AND DATE(created_at) BETWEEN ? AND DATE('now', 'localtime')
        GROUP BY exercise_name
        """,
        user_id, start_str
    )
    last_weights = db.execute(
        """
        SELECT exercise_name, AVG(weight) AS avg_weight
        FROM TrainingLogs
        WHERE user_id = ?
          AND DATE(created_at) BETWEEN ? AND ?
        GROUP BY exercise_name
        """,
        user_id, last_start_str, last_end_str
    )
    diffs = []
    for cw in current_weights:
        for lw in last_weights:
            if cw["exercise_name"] == lw["exercise_name"] and cw["avg_weight"] is not None and lw["avg_weight"] is not None:
                diff = cw["avg_weight"] - lw["avg_weight"]
                diffs.append(diff)
    avg_weight_increase = round(sum(diffs) / len(diffs), 1) if diffs else 0

    # Volume per muscle group – udeluk "core"
    volume_data = db.execute(
        """
        SELECT pe.muscle, SUM(tl.weight * tl.sets) AS total_volume
        FROM TrainingLogs tl
        JOIN program_exercises pe ON tl.exercise_name = pe.exercise_name AND tl.day_id = pe.day_id
        WHERE tl.user_id = ?
          AND DATE(tl.created_at) BETWEEN ? AND DATE('now', 'localtime')
          AND pe.muscle <> 'core'
        GROUP BY pe.muscle
        """,
        user_id, start_str
    )

    # Training Frequency (last 4 weeks)
    freq_data = db.execute(
        """
        SELECT strftime('%Y-%W', created_at) AS week, COUNT(DISTINCT created_at) AS sessions
        FROM TrainingLogs
        WHERE user_id = ?
        GROUP BY week
        ORDER BY week ASC
        """,
        user_id
    )
    for row in freq_data:
        row["week_range"] = format_week_range(row["week"])

    # Progression Over Time (average weight per week)
    progression_data = db.execute(
        """
        SELECT strftime('%Y-%W', created_at) AS week, AVG(weight) AS avg_weight
        FROM TrainingLogs
        WHERE user_id = ?
        GROUP BY week
        ORDER BY week ASC
        """,
        user_id
    )
    for row in progression_data:
        row["week_range"] = format_week_range(row["week"])

    # Sessions Overview: Gruppe sessioner efter created_at og day_name
    sessions_overview = db.execute(
        """
        SELECT DATE(created_at) AS session_date, day_name, COUNT(*) AS exercises_count
        FROM TrainingLogs
        WHERE user_id = ?
          AND DATE(created_at) BETWEEN ? AND DATE('now', 'localtime')
        GROUP BY created_at, day_name
        ORDER BY created_at DESC
        """,
        user_id, start_str
    )

    return render_template(
        "training.html",
        total_sessions=total_sessions,
        total_sets=total_sets,
        avg_weight_increase=avg_weight_increase,
        volume_data=volume_data,
        freq_data=freq_data,
        progression_data=progression_data,
        sessions_overview=sessions_overview,
        start_of_week=start_str,
        end_of_week=end_str
    )


@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    user_id = session.get("user_id")

    # Hent den nuværende brugerdata, så vi kan bruge eksisterende værdier
    user_data = db.execute("SELECT * FROM users WHERE id = ?", user_id)
    if not user_data:
        return render_template("settings.html", error="User not found.", user={})
    user = user_data[0]

    if request.method == "POST":
        # For hvert felt: hvis en ny værdi er sendt, benyt den, ellers behold den gamle værdi

        # Age
        age_input = request.form.get("age")
        if age_input:
            try:
                age = int(age_input)
            except ValueError:
                return render_template("settings.html", error="Please enter a valid number for age.", user=user)
        else:
            age = user["age"]

        # Gender
        gender_input = request.form.get("gender")
        if gender_input:
            if gender_input not in ["Male", "Female"]:
                return render_template("settings.html", error="Please select a valid gender", user=user)
            gender = gender_input
        else:
            gender = user["gender"]

        # Height og Goal Weight
        height_input = request.form.get("height")
        goal_weight_input = request.form.get("goal_weight")
        try:
            height = float(height_input) if height_input else float(user["height"])
            goal_weight = float(goal_weight_input) if goal_weight_input else float(user["goal_weight"])
        except ValueError:
            return render_template("settings.html", error="Height and goal weight must be numbers", user=user)

        # Goal Type
        goal_type_input = request.form.get("goal_type")
        if goal_type_input:
            if goal_type_input not in ["lose weight", "gain weight", "stay at current weight"]:
                return render_template("settings.html", error="Please select a valid goal", user=user)
            goal_type = goal_type_input
        else:
            goal_type = user["goal_type"]

        # Experience Level
        experience_level_input = request.form.get("experience_level")
        if experience_level_input:
            if experience_level_input not in ["Beginner", "Intermediate", "Advanced"]:
                return render_template("settings.html", error="Please select a valid experience level", user=user)
            experience_level = experience_level_input
        else:
            experience_level = user["experience_level"]

        # Training Days
        training_days_input = request.form.get("training_days")
        if training_days_input:
            try:
                training_days = int(training_days_input)
                if not (1 <= training_days <= 7):
                    return render_template("settings.html", error="Training days must be between 1 and 7.", user=user)
            except ValueError:
                return render_template("settings.html", error="Training days must be a number", user=user)
        else:
            training_days = user["training_days"]

        # Brug eksisterende vægt fra databasen (brugeren opdaterer ikke vægt her)
        weight = float(user["weight"])

        # Udregn BMR ud fra de aktuelle værdier
        if gender == "Male":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

        # Udregn kalorieindtag baseret på træningsdage
        if 1 <= training_days <= 3:
            calorie_intake = bmr * 1.375
        elif 4 <= training_days <= 5:
            calorie_intake = bmr * 1.55
        else:
            calorie_intake = bmr * 1.725

        # Juster efter goal type
        if goal_type == "lose weight":
            calorie_intake = round(calorie_intake - 500)
        elif goal_type == "gain weight":
            calorie_intake = round(calorie_intake + 500)
        else:
            calorie_intake = round(calorie_intake)

        # Opdater brugerens data, inklusiv det nye kalorieindtag.
        # Bemærk: Vægten forbliver uændret.
        db.execute(
            """
            UPDATE users
            SET age = ?,
                gender = ?,
                height = ?,
                goal_weight = ?,
                goal_type = ?,
                experience_level = ?,
                training_days = ?,
                daily_calorie_goal = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            age,
            gender,
            height,
            goal_weight,
            goal_type,
            experience_level,
            training_days,
            calorie_intake,
            user_id
        )

        return redirect("/settings")

    # GET-request: Returner den nuværende brugerdata med en tom error-besked
    return render_template("settings.html", user=user, error="")



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

