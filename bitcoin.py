import requests
import json
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o ["USD"]:
    print(result["rate"])
