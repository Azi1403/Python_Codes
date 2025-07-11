import requests

amount = input("amount of money: ")
from_currency = input("your currency?: ").lower()
to_currency = input("change to which currency?: ").lower()

url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}"

payload = {}
headers = {
"apikey": "BoahibtMD1ufmphURzpag39tHUquRy05"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.json()
print(result)
print(result["date"],result["result"])


