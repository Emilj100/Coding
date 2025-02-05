import requests

api_key = "sk-xxxx..."  # Erstat med din egen nøgle
url = "https://api.openai.com/v1/models"

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Fejl ved kaldet: {response.status_code}, {response.text}")
