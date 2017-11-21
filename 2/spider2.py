# -*- coding=utf-8 -*-


import urllib2
import requests
from bs4 import BeautifulSoup

question_url = 'https://www.zhihu.com/question/40007169'

res = urllib2.urlopen(question_url)
response = res.read()

soup = BeautifulSoup(response, "html.parser")

img_url = []
for link in soup.find_all("img"):
    if link.get('data-actualsrc') is not None:
        img_url.append(link.get('data-actualsrc'))

for i in range(5, 10):
    response = requests.get(img_url[i])
    contents = response.content
    img = open('%s.jpg' % i, 'w')
    img.write(contents)
    img.close()

