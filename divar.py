import requests
import bs4


response = requests.get("https://divar.ir/s/tehran/car/quick")
soup = bs4.BeautifulSoup(response.text,"html.parser")
result_list = soup.find_all("sh2",attrs={"data-col":"info.last_trade.PDrCotVal"})
price = result_list[0].text
print(f"cny roz: {price} rial")