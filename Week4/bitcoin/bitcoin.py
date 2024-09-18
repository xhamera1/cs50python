import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing one command-line argument")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    result = float(response["bpi"]["USD"]["rate_float"]) * n
    print(f"${result:<12,}")
except requests.RequestException:
    sys.exit("Error while requesting")

