import requests

url = "https://exercisedb.p.rapidapi.com/exercises"

headers = {
	"x-rapidapi-key": "6992181b32msh2971ae1097ca54dp1a1276jsn8ecf6bcb9516",
	"x-rapidapi-host": "exercisedb.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
