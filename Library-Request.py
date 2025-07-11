#import requests
#response=requests.get("https://www.filimo.com/")
#print(response)


import requests

amount =input (" amount of money:")
froom = input ("from?")
to = input ("to:?")

url = "https://api.apilayer.com/fixer/convert?to={to}&from={froom}&amount={amount}"

payload = {}
headers= {
  "apikey": "BoahibtMD1ufmphURzpag39tHUquRy05"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()
txt =  response.text
print(result)
print(txt)
