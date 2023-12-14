import os

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

# Configure application
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem" 
Session(app)

# Connect to posts database
con = sqlite3.connect("posts.db", check_same_thread=False)
db = con.cursor()

current_time = datetime.now()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def backcountry():
    return redirect("/")

@app.route("/trailer_tips")
def trailer():
    return render_template("trailer_tips.html")

@app.route("/cooking")
def cooking():
    return render_template("cooking.html")

@app.route("/climbing")
def climbing():
    return render_template("climbing.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    categories = ["Trailer", "Cooking", "Climbing"]

    return render_template("post.html", categories=categories)

@app.route("/login-register", methods=["GET", "POST"])
# make sure you render a different page if register is selected
# if log in is accepted, then redirect with welcome, username where login/register used to be
def login_register():
    # Forget any user_id
    session.clear()

    #Make sure username is not blank
    if request.method == "POST":

    #Make sure username is not blank


        return render_template("login-register.html")


@app.route("/register")
def register():
    return render_template("register.html")