import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
import re
import requests

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
        try:
            training_days = int(request.form.get("training_days"))
            if not (1 <= training_days <= 7):
                return render_template("register-part2.html", error="Training days must be between 1 and 7.")
        except ValueError:
            return render_template("register-part2.html", error="Training days must be a number")

        try:
            user_id = db.execute(
                """
                INSERT INTO users (name, email, password, age, gender, height, weight, goal_weight, goal_type, training_days)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                session["name"], session["email"], session["password"], age,
                request.form.get("gender"), height, weight, goal_weight,
                request.form.get("goal_type"), training_days
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

@app.route("/calorietracker")
@login_required
def calorietracker():

    if request.method == "POST":

        # Spørger brugeren om hvad de har spist i dag
        food_query = input("What did you eat today? ")

        API_KEY = "6158963245cf646896228de0c3d0ba3a"
        APP_ID = "584633a6"

        url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

        headers = {
            "x-app-id": APP_ID,
            "x-app-key": API_KEY,
            "Content-Type": "application/json"
        }

        data = {
            "query": food_query
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            nutrition_data = response.json()
            print(nutrition_data)
        else:
            print("Error:", response.status_code, response.text)

    else:
        return render_template("calorietracker.html")

@app.route("/traininglog")
@login_required
def traininglog():
    return "traininglog page"

@app.route("/dashboard")
@login_required
def dashboard():
    return "dashboard page"

@app.route("/mealplan")
@login_required
def mealplan():
    return "mealplan page"
