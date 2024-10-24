import requests
import json

food_query = input("What did you eat today? ")

# API nøgler (du skal indsætte dine egne værdier her)
API_KEY = "6158963245cf646896228de0c3d0ba3a"
APP_ID = "584633a6"

# URL for Natural Language API endpoint
url = "https://trackapi.nutritionix.com/v2/natural/nutrients"


# Headers for API-anmodningen (inkluderer din API-key og App-ID)
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# Data, der skal sendes i anmodningen - den tekstbaserede forespørgsel
data = {
    "query": food_query
}

# Send POST-forespørgsel til Nutritionix API
response = requests.post(url, headers=headers, json=data)

# Ændre svaret til JSON-format
nutrition_data = response.json()

# Vis det fulde JSON-svar (kan bruges til at analysere data)



print(json.dumps(nutrition_data, indent=4))
