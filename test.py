import requests
import sys

# Check if user provided the correct command-line argument
if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

# Try to convert the user input to a float
try:
    x = float(sys.argv[1])
except ValueError:
    sys.exit("Error: Invalid number of Bitcoins")

# Try to make the API request
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()  # Check if the request was successful
except requests.RequestException:
    sys.exit("Error: Unable to get data from CoinDesk API")

# Parse the response and calculate the cost
try:
    o = response.json()
    rate = o["bpi"]["USD"]["rate"]
    rate = float(rate.replace(",", ""))  # Remove commas and convert to float
except (KeyError, ValueError):
    sys.exit("Error: Problem parsing the API response")

# Calculate the total cost and print the result formatted
z = rate * x
print(f"${z:,.4f}")
