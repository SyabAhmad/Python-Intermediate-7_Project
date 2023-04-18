import requests

# Base currency and target currency
base_currency = "EUR"
target_currency = "USD"

# Your API key
api_key = "Your API Key Here"

# Make a request to the apilayer.net API to get the exchange rate
url = f"https://apilayer.net/api/live?access_key={api_key}&currencies={target_currency}&source={base_currency}"
response = requests.get(url)

# to check status is okay or not
# print(response.status_code) # if 200 it is okay

# Parse the response to get the exchange rate
data = response.json()
if data["success"]:
    exchange_rate = data["quotes"][f"{base_currency}{target_currency}"]
else:
    print("Error: ", data["error"]["info"])
    exit()

# Ask the user for the amount to convert
amount = float(input(f"Enter the amount in {base_currency}: "))

# Convert the amount to the target currency
converted_amount = amount * exchange_rate

# Print the result
print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}.")
