from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import csv

try:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.digikala.com/product/7463108/heimwolle-mitron-p49/#reviews")
    time.sleep(2)
    reviews = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".text-body-1.text-neutral-900.mb-1.break-words")))
    with open("comments.csv", "a", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        for review in reviews:
            csv_writer.writerow([review.text])
            print(f"Comment saved: {review.text}")

except WebDriverException as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
