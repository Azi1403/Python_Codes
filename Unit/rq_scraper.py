import requests
import bs4



while True:
    currency = input("currency: GBP,EUR,CNY,usd??").lower()
    if currency == 'usd':
        response = requests.get("https://www.tgju.org/profile/price_dollar_rl")
    else:    
        response = requests.get(f"https://www.tgju.org/profile/price_{currency}")


    soup = bs4.BeautifulSoup(response.text,"html.parser")
    result_list = soup.find_all("span",attrs={"data-col":"info.last_trade.PDrCotVal"})
    price = result_list[0].text
    print(f" {price} rial")
    r=input("do you want to continue:Y/N?").lower()
    if r=='n':
        break
    
    

    