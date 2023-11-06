"""
This program expects on CLI argument (name or path of csv file) and outputs a table formmatted as ASCII art. 
If user doesn't specify exactly one CLI argument or if the file name doesn't end in .csv, the program should instead exit via sys.exit
"""

import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2 : 
    sys.exit("Too many command-line arguments")

if sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

try: 
    file = open(sys.argv[1], 'r')
except FileNotFoundError:
    sys.exit("File does not exist")

menu = []
reader = csv.reader(file)
for row in reader:
    menu.append(row)


print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))