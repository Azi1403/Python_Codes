import requests

# Get the number of Bitcoins from the user
number_of_bitcoins = float(input("Enter the number of Bitcoins you'd like to buy: "))

# get my APiKey from website https://pro.coincap.io/dashboard
YOUR_API_KEY = "6a0f2e5fd1796dd0e73aa7f89fc59c825348c9d66ffe269c8548a0a7623ffab3"


api_url = f"https://rest.coincap.io/v3/assets?apiKey={YOUR_API_KEY}"

response = requests.get(api_url).json()

# print(response)
cur_doller = response['data'][0]['priceUsd']
print(f'current Dollar is:  {cur_doller}')

# TypeError: list indices must be integers or slices, not str so because of this error use [0]
current_price = (response['data'][0]['priceUsd'])
cost = number_of_bitcoins * float(current_price)

print(f"The cost of {number_of_bitcoins} Bitcoins is ${cost:.2f}")

# i would like print other cel in dic
print("")
print("its my test to show me cell of usd price for Bitcoin and Ethereum")
pp = (response['data'][0]['id'], response['data'][0]['priceUsd'])
print(pp)

print( response["data"][1]["id"],response['data'][1]["priceUsd"])


