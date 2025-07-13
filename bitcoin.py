import requests

# Get the number of Bitcoins from the user
number_of_bitcoins = float(input("Enter the number of Bitcoins you'd like to buy: "))
YOUR_API_KEY = "6a0f2e5fd1796dd0e73aa7f89fc59c825348c9d66ffe269c8548a0a7623ffab3"

# Construct the API request
api_url = f"https://rest.coincap.io/v3/assets?apiKey={YOUR_API_KEY}"
response = requests.get(api_url).json()

# print(response)
cur_doller = response['data'][0]['priceUsd']
print(f'current Dollar is:  {cur_doller}')

current_price = response['data'][0]['priceUsd']

cost = number_of_bitcoins * float(current_price)

print(f"The cost of {number_of_bitcoins} Bitcoins is ${cost:.2f}")


