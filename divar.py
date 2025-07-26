import requests
import bs4


response = requests.get("https://divar.ir/s/tehran/auto")
soup = bs4.BeautifulSoup(response.text,"html.parser")
result_list = soup.find_all("div",attrs={"class":"kt-post-card__description"})


for price in result_list:
    print(price.text)

