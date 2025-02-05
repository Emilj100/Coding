import requests

api_key = "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"  # Erstat med din egen nøgle
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
