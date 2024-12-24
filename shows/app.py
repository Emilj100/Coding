from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///store.db")



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    shows = db.execute("SELECT * FROM show WHERE title = ?", request.args.get("q"))
    return render_template("search.html", shows=shows)
