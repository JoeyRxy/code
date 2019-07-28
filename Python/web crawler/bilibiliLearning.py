import bs4
from bs4 import BeautifulSoup as soup
import re
import requests


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    text = soup(html, "html.parser")
    for tr in text.find_all('tr', {'class': 'alt'}):
        td = tr.contents
        ulist.append([td[0].string, td[1].string, td[2].string])


def printUnivList(ulist, num):
    for i in range(num):
        u = ulist[i]
        print('{:^10}\t{:^10}\t{:^6}\n'.format(u[0], u[1], u[2]))
    print('Suc'+str(num))


if __name__ == "__main__":
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 100)
