import requests
import json
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = response.json()
for currency in o["bpi"]:
    print(o["bpi"][currency]["rate"])
