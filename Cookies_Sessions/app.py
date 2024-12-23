from flask import Flask, render_template, request, session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    if request.method == "POST":
        session
    return render_template("login.html")
