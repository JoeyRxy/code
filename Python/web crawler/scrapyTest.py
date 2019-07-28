from selenium import webdriver
import time
browser = webdriver.Chrome(executable_path='C:\Users\29388\Documents\code\Python\web crawler\chromedriver.exe')
browser.get(url)
time.sleep(5)
text = browser.page_source
browser.close()