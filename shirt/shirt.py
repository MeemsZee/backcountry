"""
Program takes in a picture and saves it with a CS50 shirt in the for front
"""

import sys
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

valid_file = (".jpg", ".jpeg", ".png")

if not sys.argv[1].endswith(valid_file) or not sys.argv[2].endswith(valid_file):
    sys.exit("Invalid input")

if sys.argv[1].rsplit(".")[1] != sys.argv[2].rsplit(".")[1]:
    sys.exit("Input and output have different extensions")

try:
    input_image = Image.open(sys.argv[1], 'r')
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

shirt = Image.open("shirt.png")

size = shirt.size
size_1 = input_image.size 

resized_image = ImageOps.fit(input_image, (600, 600))

resized_image.paste(shirt, (0,0), shirt)

resized_image.save(sys.argv[2])