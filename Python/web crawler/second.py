import bs4
from bs4 import BeautifulSoup as soup
import re
import requests
# 失败了,为什么呢？
# ATTENTION 动态网页的爬取：通过requests库得到的html和原网页的代码不同 
url = 'https://top.jd.com/?cateId=653'
r = requests.get(url)
r.encoding = r.apparent_encoding
text = soup(r.text, "html.parser")
div = text.find(
    'div', {'class': 'top_sale_list J_saleList clearfix'})
div = soup(div, 'html.parser')

# re compile
regex = re.compile(r'saleitem saleitem[0-9]*')

ans = []

for li in div.find_all('li', {'class': regex}):
    u = soup(li).find('div', {'class': 'saleitem_info'})
    name = u.find('p', {'class': 'saleitem_info_name'}).string
    price = u.find('p', {'class': 'saleitem_info_price'}).string
    ans.append([name, price])

formating = '{:^10}\t{:^10}\t{}\n'
print(formating.format('个数', '价格', '名字'))
count = 0
for i in ans:
    tmp = ans[i]
    count = count + 1
    print(formating.format(count, tmp[0], tmp[1]))
