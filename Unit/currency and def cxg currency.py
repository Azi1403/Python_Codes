import requests
import bs4

response = requests.get("https://www.tgju.org/profile/price_dollar_rl")
#print(response)
#print(response.text)
soup = bs4.BeautifulSoup(response.text,"html.parser")
#print(soup)
result_list = soup.find_all("span",attrs={"data-col":"info.last_trade.PDrCotVal"})
price = result_list[0].text
print(f"dollar roz: {price} rial")

response = requests.get("https://www.tgju.org/profile/price_eur")
soup = bs4.BeautifulSoup(response.text,"html.parser")
result_list = soup.find_all("span",attrs={"data-col":"info.last_trade.PDrCotVal"})
price = result_list[0].text
print(f"euro roz: {price} rial")

response = requests.get("https://www.tgju.org/profile/price_cny")
soup = bs4.BeautifulSoup(response.text,"html.parser")
result_list = soup.find_all("span",attrs={"data-col":"info.last_trade.PDrCotVal"})
price = result_list[0].text
print(f"cny roz: {price} rial")

# define function for currency
print ("from def euro rate is: ")

def price(currency):
    response = requests.get(f"https://www.tgju.org/profile/price_{currency}")


    soup = bs4.BeautifulSoup(response.text,"html.parser")
    result_list = soup.find_all("span",attrs={"data-col":"info.last_trade.PDrCotVal"})
    price = result_list[0].text
    return f" {price} rial"
print(price('eur'))