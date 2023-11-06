"""
This program counts the number of lines in a valid python program 
"""

import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too Many Command-line arguments")

if sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

try :
    file = open(sys.argv[1], 'r')
except FileNotFoundError:
    sys.exit("File does not exist")

line_counter = 0

for line in file:
    if line.lstrip().startswith("#"):
        pass
    elif line.split() == []:
        pass
    else:
        line_counter += 1
    
print(line_counter)

