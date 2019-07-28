# %%
import bs4
from bs4 import BeautifulSoup as soup
import re
import requests
from selenium import webdriver
import time
import lxml

def run(query):
    url = 'https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=' + query

    browser = webdriver.Chrome(executable_path='C:/Users/29388/Documents/code/Python/web crawler/chromedriver.exe')
    browser.get(url)
    time.sleep(5)
    text = browser.page_source
    browser.close()
    text = soup(text, 'lxml')
    file = open("test_taobao.html", "w",encoding='utf-8')
    str = text.prettify()
    file.write(str)
    file.close()
    div = text('div', {'class': 'ctx-box J_MouseEneterLeave J_IconMoreNew'})
    ans = []
    for tmp in div:
        u1 = tmp.find('div', {'calss': 'price g_price g_price-highlight'})
        u2 = tmp.find('div', {'class': 'row row-2 title'})
        ans.append([u1.string, u2.string])
    tl = '{:^6}\t{:^10}\t{}\n'
    print(tl.format('序号', '价格', '名字'))
    count = 0
    for t in ans:
        count = count + 1
        u = ans[t]
        print(tl.format(count, u[0], u[1]))


run('运动鞋')
