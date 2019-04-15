# -*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#网页下载器urlopen
resp = urlopen('https://baike.baidu.com/item/%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91').read().decode("utf-8")
#网页解析器BeautifulSoup
soup = BeautifulSoup(resp, 'html.parser')
listurls = soup.find_all('a', href=re.compile('^/item/'))

for url in listurls:
    if not re.search("\.(jpg|JPG)$", url['href']):
        print(url.get_text(),"<------>","https://baike.baidu.com"+url['href'])
