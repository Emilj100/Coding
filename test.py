import requests
import json  # Importer json-modulet for bedre formatering

food_query = input("What did you eat today? ")

API_KEY = "6158963245cf646896228de0c3d0ba3a"
APP_ID = "584633a6"

url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "query": food_query
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    nutrition_data = response.json()
    # Gør output menneskevenligt
    print(json.dumps(nutrition_data, indent=4))
else:
    print("Error:", response.status_code, response.text)
