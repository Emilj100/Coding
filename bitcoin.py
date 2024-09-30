import requests
import json
import sys

try:
    x = float(sys.argv[1])

except ValueError and requests.RequestException:
    sys.exit()

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = response.json()

o = o["bpi"]["USD"]["rate"]

o = o.replace(",", "")

o = float(o)

z = o * x

print(f"${z:,.4f}")
