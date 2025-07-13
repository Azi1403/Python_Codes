import requests

url = "https://rest.coinapi.io/v1/assets"

payload = {}
headers = {
  'Accept': 'text/plain',
  'Authorization': '<API_KEY_VALUE>'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.json())