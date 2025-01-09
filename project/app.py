import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

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

        if not request.form.get("name"):
            return render_template("register-part1.html", error="Must provide Name")
        elif not request.form.get("email"):
            return render_template("register-part1.html", error="Must provide email")
        elif not request.form.get("password"):
            return render_template("register-part1.html", error="Must provide password")
        elif not request.form.get("password") == request.form.get("confirm_password"):
            return render_template("register-part1.html", error="Password must match")

        password = generate_password_hash(request.form.get("password"))

        try:
            db.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", request.form.get("name"), request.form.get("email"), password)
        except ValueError:
            return render_template("register-part1.html", error="Email already exist")

        return redirect("register-part2.html")
    
    else:
        return render_template("register-part1.html")

@app.route("/register-part2", methods=["GET", "POST"])
def registerpart2():
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
    return "logout page"

@app.route("/calorietracker")
@login_required
def calorietracker():
    return "calorietracker page"

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
