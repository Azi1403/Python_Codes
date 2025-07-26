import requests
import bs4

def web_scraping(url,tag,attr_key,attr_value):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    result_list = soup.find_all(tag,attrs={attr_key:attr_value})
    return result_list
    
result = web_scraping("https://divar.ir/s/tehran/auto","h2","class","kt-post-card__title")
for item in result:
    print(item.text)
