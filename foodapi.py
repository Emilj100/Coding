import requests
import json

# API nøgler (du skal indsætte dine egne værdier her)
API_KEY = "your_api_key"
APP_ID = "your_app_id"

# URL for Natural Language API endpoint
url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

# Fødevareforespørgsel - du kan ændre teksten efter behov
food_query = "2 eggs and 1 slice of bacon"

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
