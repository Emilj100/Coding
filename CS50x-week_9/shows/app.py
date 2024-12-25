from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///movies.db")



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q")
    movies = db.execute("SELECT * FROM movies WHERE title LIKE ?", "%" + q + "%")
    return render_template("search.html", movies=movies)



