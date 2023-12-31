import os

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

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
con = sqlite3.connect("finance.db", check_same_thread=False)
db = con.cursor()

current_time = datetime.now()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        try:
            add_cash = int(request.form.get("cash"))
            if add_cash < 0:
                return apology("Please provide a positive number")
        
            query = db.execute("SELECT cash FROM users WHERE id =?;", (session["user_id"],))
            current_cash = list(query.fetchone())[0]

            new_amt = current_cash + add_cash
            db.execute("UPDATE users SET cash = ? WHERE id = ?", (new_amt, session["user_id"],))
            con.commit()

        except ValueError:
            return apology("Please provide a postive number")

        return render_template("success.html") 

    else:

        query_1= db.execute("SELECT username, cash FROM users WHERE id = ?;", (session["user_id"],))
        username, cash = list(query_1.fetchone())

        query_2= db.execute("SELECT stock_symbol, SUM(qty) FROM transactions WHERE user_id = ? GROUP BY stock_symbol;", (session["user_id"],))
        holdings = query_2.fetchall()

        holdings_dict = {}
        holdings_info = []

        for holding in holdings:
            holdings_dict["stock_symbol"] = holding[0].upper()
            holdings_dict["qty"] = holding[1]
            symbol_price = lookup(holdings_dict["stock_symbol"])["price"]
            holdings_dict["stock_price"] = symbol_price
            holdings_dict["holding_value"] = round(holdings_dict["qty"] * symbol_price, 2)
            holdings_info.append(holdings_dict.copy())

        holdings_value = 0

        for item in holdings_info:
            holdings_value += item["holding_value"]

        grand_total_value = round(holdings_value + cash, 2)

        return render_template("index.html", user=username, holdings=holdings_info, cash_balance=cash, total_value=grand_total_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if len(symbol) == 0:
            return apology("Must Provide Ticker")
        
        stock_quote = lookup(symbol)

        if stock_quote == None:
            return apology("Stock symbol doesn't exist")

        try:
            shares = int(request.form.get("shares"))
            if shares < 1:
                return apology("Number of shares must be positive")
        except ValueError:
            return apology("Number of shares must a number")
        
        cash_object = db.execute("SELECT cash FROM users WHERE id = ?", (session["user_id"],))
        current_cash_amt = list(cash_object.fetchone())
        current_cash_amt = current_cash_amt[0]
        transaction_cost = shares * stock_quote["price"]

        if current_cash_amt < transaction_cost:
            return apology("Insufficient Funds For This Transaction")
        else: 
            new_cash_amt = current_cash_amt - transaction_cost
     
        db.execute("INSERT INTO transactions (user_id, created_on, transaction_type, stock_symbol, qty, transaction_cost) VALUES(?, ?, ? , ? , ?, ?)", (session["user_id"], current_time, 'BUY', symbol, shares, transaction_cost))
        con.commit()

        db.execute("UPDATE users SET cash = ? WHERE id = ?", (new_cash_amt, session["user_id"],))
        con.commit()

        return redirect("/")
    
    else:
        return render_template("buy.html")
    

@app.route("/history")
@login_required
def history():
    query = db.execute("SELECT created_on, transaction_type, stock_symbol, qty FROM transactions WHERE user_id = ? ORDER BY created_on DESC;", (session["user_id"],))
    all_trades = query.fetchall()

    history_dict = {}
    history_list = []

 
    for trade in all_trades:
        history_dict["type"] = trade[1]
        history_dict["stock_symbol"] = trade[2].upper()
        history_dict["qty"] = abs(trade[3])
        history_dict["datetime"] = trade[0].split(".")[0]
        history_list.append(history_dict.copy())
   

    return render_template("history.html", trades=history_list)


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
        user_query = db.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),))
        rows = user_query.fetchall()

        user_dict = {}
        user_info = []

        for row in rows:
            user_dict["id"] = row[0]
            user_dict["username"] = row[1]
            user_dict["hash"] = row[2]
            user_info.append(user_dict.copy())

        #Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(user_info[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = user_info[0]["id"]

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
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if len(symbol) == 0:
            return apology("Must Provide Ticker")
        
        stock_quote = lookup(symbol)
        if stock_quote == None:
            return apology("Stock symbol doesn't exist")
        
 
        return render_template("quoted.html", quote=stock_quote)
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])    
def register():
    if request.method == "POST":
        username = request.form.get("username").lower().strip()
        password = request.form.get("password").strip()
        password_confirm = request.form.get("confirmation").strip()
        query_cur = db.execute("SELECT username FROM users WHERE username = ?;", (username,))
        users_query = query_cur.fetchall()

        if len(username) == 0 or " " in username  or len(users_query) != 0: 
            return apology("Invalid username or username unavailable")
        if len(password) == 0: 
            return apology("Password Required")
        if len(password_confirm) == 0: 
            return apology("Please re-confirm password")
        if password != password_confirm:
            return apology("Passwords must match")
        db.execute("INSERT INTO users (username, hash) VALUES (?,?);", (username, generate_password_hash(password)))
        con.commit()

        id_query = db.execute("SELECT id FROM users WHERE username = ?", (username,))
        user_id = id_query.fetchone()

        session["user_id"] = user_id[0]

        return redirect("/")
        
    else:
        return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    stock_query = db.execute("SELECT stock_symbol, SUM(qty) FROM transactions WHERE user_id = ? GROUP BY stock_symbol;", (session["user_id"],))
    stocks = stock_query.fetchall()
    stock_list = []
    stock_dict = {}
    stock_info = []

    for stock in stocks:
        stock_dict["stock_symbol"] = stock[0]
        stock_list.append(stock[0])
        stock_dict["qty"] = stock[1]
        stock_info.append(stock_dict.copy())

    if request.method == "POST":

        s_symbol = request.form.get("symbol")
        sell_qty = int(request.form.get("shares"))
        
        if s_symbol not in stock_list:
            return apology("You do not own this stock")
       
        
        for stock in stock_info:
             if stock["stock_symbol"] == s_symbol:
                 stock_qty = stock["qty"]

        if sell_qty > stock_qty:
            return apology(f"You do no own this many shares of {s_symbol}")
        
        sell_qty = -sell_qty
        sell_price = round((lookup(s_symbol)["price"] * sell_qty), 2)
        
        db.execute("INSERT INTO transactions (user_id, created_on, transaction_type, stock_symbol, qty, transaction_cost) VALUES(?, ?, ? , ? , ?, ?)", (session["user_id"], current_time, 'SELL',s_symbol, sell_qty, sell_price))
        con.commit()

        query = db.execute("SELECT cash FROM users where id=?;", (session["user_id"],))
        cash_amt = list(query.fetchone())[0]

        new_cash_amt = cash_amt - sell_price

        db.execute("UPDATE users SET cash = ? WHERE id = ?", (new_cash_amt, session["user_id"],))
        con.commit()
        
        return redirect("/")

    else:
        return render_template("sell.html", stocks = stock_list)
