import requests
import json
import sys

x = float(sys.argv[1])

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = response.json()

o = o["bpi"]["USD"]["rate"]

o = o.replace(",", "")

o = float(o)

z = o * x
