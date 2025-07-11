import requests

response = requests.get("https://dog.ceo/api/breeds/image/random")

data = response.json()
print(data)
print(data["message"])