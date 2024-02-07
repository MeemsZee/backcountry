import sqlite3
from datetime import datetime

con = sqlite3.connect("finance.db", check_same_thread=False)
db = con.cursor()

current_time = datetime.now()

query = db.execute("SELECT * FROM transactions")

column_names = query.description
columns = []

for column in column_names:
    columns.append(column[0])

for item in columns:
    print(item)



