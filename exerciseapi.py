import requests

url = "https://exercisedb.p.rapidapi.com/exercises/name/%7Bname%7D"

querystring = {"offset":"0","limit":"10"}

headers = {
	"x-rapidapi-key": "6992181b32msh2971ae1097ca54dp1a1276jsn8ecf6bcb9516",
	"x-rapidapi-host": "exercisedb.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
