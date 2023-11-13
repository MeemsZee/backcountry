import os

import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
con = sqlite3.connect("birthdays.db", check_same_thread=False)
db = con.cursor()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))
        print(name, month, day)
  
        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?,?,?);", (name, month, day))
        con.commit()
        con.close()

        return redirect("/")

    else:
        new_con = sqlite3.connect("birthdays.db", check_same_thread=False)
        db_cur = new_con.cursor()
        data = db_cur.execute("SELECT name, month, day FROM birthdays;")
        rows = data.fetchall()
        birth_dict = {}
        birth_info = []

        for row in rows:
            birth_dict["name"] = row[0] 
            birth_dict["month"] = row[1] 
            birth_dict["day"] = row[2]
            birth_info.append(birth_dict.copy())

        new_con.close()
        return render_template("index.html", birthday=birth_info)
        

