import requests
import json
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

print(response.json())

