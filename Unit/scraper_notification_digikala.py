# import requests
# import bs4

# def web_scraping(url,tag,attr_key,attr_value):
#     response = requests.get(url)
#     soup = bs4.BeautifulSoup(response.text,"html.parser")
#     result_list = soup.find_all(tag,attrs={attr_key:attr_value})
#     return result_list

# result = web_scraping("https://www.digikala.com/product/dkp-7463108/%D9%87%D8%AF%D9%81%D9%88%D9%86-%D8%A8%D9%84%D9%88%D8%AA%D9%88%D8%AB%DB%8C-%D9%85%D8%AF%D9%84-p49/#reviews","div","class=","gap-y-3 flex flex-col")
# for item in result:
#     print(item.text)
    
    
# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://www.digikala.com/product/7463108/heimwolle-mitron-p49/#reviews")
# if response.status_code!= 200:
#     print("Failed to retrieve the webpage")
#     exit()

# soup = BeautifulSoup(response.text, "html.parser")
# search = soup.find_all("p", class_="text-body-1 text-neutral-900 mb-1 break-words")

# for review in search:
#     print(review.text)

import requests
import csv
import time

product_id = "7463108"  # Extract from product URL
base_url = f"https://www.digikala.com/ajax/product/comments/{product_id}/?page={{}}&mode=comments"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json'
}

with open("comments.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    page = 1
    
    while True:
        url = base_url.format(page)
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page {page} (Status: {response.status_code})")
            break

        try:
            data = response.json()
            comments = data['data']['comments']
            if not comments:
                break
                
            for comment in comments:
                text = comment['text'].strip()
                writer.writerow([text])
                print(f"Comment saved: {text}")
                
            print(f"Page {page} processed ({len(comments)} comments)")
            page += 1
            time.sleep(1)  # Respectful delay between requests
            
        except (KeyError, ValueError) as e:
            print(f"Error processing page {page}: {e}")
            break

print("Completed saving all comments!")