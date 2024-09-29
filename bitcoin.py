import requests
import json
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = response.json()
for result in o["bpi"]:
    print(result["rate"])
