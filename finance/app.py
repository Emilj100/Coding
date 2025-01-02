import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    transactions = db.execute("SELECT symbol, shares FROM transactions WHERE user_id = ?", session["user_id"])

    stocks = []

    for transaction in transactions:

        symbol = transaction["symbol"]
        shares = transaction["shares"]
        stock_data = lookup(symbol)

        if stock_data:

            stock = {
                "symbol": symbol,
                "shares": shares,
                "price": stock_data["price"],
                "total": shares * stock_data["price"]
            }
            stocks.append(stock)

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

    total = 0
    for stock in stocks:
        total += stock["total"]
        stock["price"] = usd(stock["price"])
        stock["total"] = usd(stock["total"])


    total_cash = cash + total
    cash = usd(cash)
    total_cash = usd(total_cash)

    return render_template("index.html", stocks=stocks, cash=cash, total_cash=total_cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        symbol = lookup(symbol)
        if not symbol:
            return apology("Enter valid symbol", 406)
        try:
            shares = int(request.form.get("shares"))
            if not shares > 0:
                return apology("Enter positive number", 407)
        except ValueError:
            return apology("Shares must be a number", 409)
        price = float(symbol["price"])
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        cash = float(cash)
        total = shares * price
        remaining_cash = cash - total
        if remaining_cash < 0:
            return apology("Not enough money", 408)

        owned_shares = db.execute("SELECT shares FROM transactions WHERE user_id = ? AND symbol = ?", session["user_id"], symbol["symbol"] )
        if owned_shares:
            owned_shares = owned_shares[0]["shares"] + shares
            db.execute("UPDATE transactions SET shares = ? WHERE user_id = ? and symbol = ?", owned_shares, session["user_id"], symbol["symbol"])
            db.execute("INSERT INTO transactions_history (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", session["user_id"], symbol["symbol"], shares, symbol["price"])

        else:
            db.execute("INSERT INTO transactions (user_id, symbol, shares) VALUES (?, ?, ?)", session["user_id"], symbol["symbol"], shares)
            db.execute("INSERT INTO transactions_history (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", session["user_id"], symbol["symbol"], shares, symbol["price"])

        db.execute("UPDATE users SET cash = ? WHERE id = ?", remaining_cash, session["user_id"])

        return redirect("/")

    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""





    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        symbol = lookup(symbol)
        if not symbol:
            return apology("Enter valid symbol", 406)
        return render_template("quoted.html", name=symbol["name"], price=symbol["price"], symbol=symbol["symbol"])

    else:
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 403)
        if not request.form.get("password"):
            return apology("must provide password", 403)
        if not request.form.get("password") == request.form.get("confirmation"):
            return apology("Password and confirmation of password doesnt match", 404)

        password = request.form.get("password")
        password = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), password)
        except ValueError:
            return apology("Username already exist", 405)


        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    symbols = db.execute("SELECT symbol FROM transactions WHERE user_id = ?" , session["user_id"])

    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Please select a valid stock", 410)
        symbol = lookup(request.form.get("symbol"))
        if not symbol:
            return apology("Please select a valid stock", 410)
        if not any(request.form.get("symbol") == s["symbol"] for s in symbols):
            return apology("Please select a valid stock that you own", 410)
        try:
            shares = int(request.form.get("shares"))
            if shares <=  0:
                return apology("Please input positive number of shares", 411)
        except ValueError:
            return apology("Shares must be a valid number", 413)
        owned_shares = db.execute("SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = ? AND symbol = ?", session["user_id"], request.form.get("symbol") )
        if owned_shares[0]["total_shares"] < shares:
            return apology("You do not own that many shares of the stock", 412)
        if owned_shares[0]["total_shares"] == shares:
            db.execute("DELETE FROM transactions WHERE user_id = ? AND symbol = ?", session["user_id"], request.form.get("symbol") )
            db.execute("INSERT INTO transactions_history (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", session["user_id"], symbol["symbol"], shares, symbol["price"])

        else:
            db.execute("UPDATE transactions SET shares = ? WHERE user_id = ? AND symbol = ?", owned_shares[0]["total_shares"] - shares, session["user_id"], request.form.get("symbol") )
            db.execute("INSERT INTO transactions_history (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", session["user_id"], symbol["symbol"], shares, symbol["price"])

        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        cash += symbol["price"] * shares
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        return redirect("/")

    else:
        return render_template("sell.html", symbols=symbols)
