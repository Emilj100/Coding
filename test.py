import requests
import json

api_key = "71433d93ff0445e68f984bb19ca3048f"
url = f"https://api.spoonacular.com/mealplanner/generate?apiKey={api_key}"

params = {
    "timeFrame": "day",  # Kan være 'day' eller 'week'
    "targetCalories": 2000,  # Brugerens daglige kalorimål
    "diet": "vegetarian",  # Diætpræference, fx 'vegetarian', 'vegan', osv.
    "exclude": "nuts, shellfish"  # Ingredienser, der skal undgås
}

response = requests.get(url, params=params)
print(response.json())
