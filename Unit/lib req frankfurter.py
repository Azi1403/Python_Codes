import requests
response = requests.get("https://api.frankfurter.dev/v1/latest")
prices = response.json()
print(prices)


print(prices["date"])
print(prices["amount"],prices["base"],"=",prices["rates"]["USD"],"$")