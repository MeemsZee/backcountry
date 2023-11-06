"""
Program cleans data.  Splits name into first and last
"""

import csv
import sys

if len(sys.argv) < 3: 
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-4:] != ".csv":
    sys.exit(f"{sys.argv[1]} is not an CSV file")
    
students = []

try:
    file = open(sys.argv[1], 'r')
    
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

reader = csv.DictReader(file)
for row in reader:
    students.append({"name": row["name"], "house": row["house"]})

to_write = []
for student in students:
    #split the student's name into last and first 
    last, first = student["name"].split(",")
    #set value of house
    house = student["house"]
    to_write.append({"first": first.lstrip(), "last": last, "house": house})

#write to file name provided by user
with open(sys.argv[2], 'w') as file2:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(file2, fieldnames=fieldnames)
    writer.writeheader()
    for dict in to_write:
        writer.writerow({"first": dict["first"], "last": dict["last"], "house": dict["house"]})

file.close()
file2.close()






