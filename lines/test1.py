"""
Get user to provide number of Bitcoins they would like to buy. 
"""

import json
import requests
import sys

# if there isn't a number provided in the CLI, exit 
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# if user didn't provide a float, exit
try:
    num_bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# use api to get current bitcoin price
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# store response
o = response.json()

# extract price from json file
price = (o["bpi"]["USD"]["rate"]).replace(",", "")

# calculate price for requested bitcoin 
amount = float(price) * num_bitcoin

print(f"${amount:,.4f}")

