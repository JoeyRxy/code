# https://www.youtube.com/watch?v=XQgXKtPSzUI
#%%
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

myurl = 'https://www.amazon.com/s/ref=nb_sb_noss?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&field-keywords=%E6%98%BE%E5%8D%A1'

client = urlopen(myurl)
html_text = client.read()

text_soup = soup(html_text, 'html.parser')

client.close()
#%%
mfile = open("test.html", "w")
print(text_soup, file=mfile)
mfile.close()

#%%
containers = text_soup.findAll("div",{"class":"a-section a-spacing-medium"})

len(containers)