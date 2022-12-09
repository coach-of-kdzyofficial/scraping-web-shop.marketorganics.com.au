from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)

shopee_link = "https://shopee.co.id/search?keyword=macbook"
driver.set_window_size(1300,800)
driver.get(shopee_link)
time.sleep(5)

driver.save_screenshot("home.png")
content = driver.page_source
driver.quit()

data = BeautifulSoup(content, 'html.parser')
# print(data.encode("utf-8"))

i = 1
for area in data.find_all('div' ,class_="col-xs-2-4 shopee-search-item-result__item"):
    print(i)
    nama = area.find('div', class_="YPqix5")
    children = nama.findChildre("span", recursive=False)
    for child in children:
        print(child)
    gambar = area.find('img')['src']
    harga = area.find('div', class_="X0xUb5").get_text
    # print(nama)
    # print(gambar)
    # print(harga)
    i+=1
    print("------")