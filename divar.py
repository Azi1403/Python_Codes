import requests
import bs4


response = requests.get("https://divar.ir/s/tehran/car/quick")
soup = bs4.BeautifulSoup(response.text,"html.parser")
prices_list = soup.find_all("div",attrs={"class":"kt-post-card__description"})
models_list = soup.find_all("h2",attrs={"class":"kt-post-card__title"})

for price in prices_list:
    print(price.text)   #print kilometr and price because tag name is same
    
for price in prices_list: #print just price
    if "کیلومتر" not in price.text:
        print(price.text)
        
for model in models_list: #print model
    print(model.text)


for model in models_list: #print model+price
    for price in prices_list:
        if "کیلومتر" not in price.text:
            print(model.text,price.text)
