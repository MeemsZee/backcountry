import json
import requests
import sys

# if there isn't a number provided in the CLI, exit 
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")