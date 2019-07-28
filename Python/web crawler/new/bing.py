from bs4 import BeautifulSoup as soup
import bs4
from selenium import webdriver
import time
browser = webdriver.Chrome(
    executable_path='C:/Users/29388/Documents/code/Python/web crawler/chromedriver.exe')
browser.get("https://cn.bing.com/")
time.sleep(5)

text = browser.page_source

browser.quit()

msoup = soup(text, "lxml")
fId = open("web crawler\\new\\bing.html", "w", encoding="utf-8")
fId.write(msoup.text)
fId.close()
