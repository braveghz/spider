# -*- coding=utf-8 -*-

from bs4 import BeautifulSoup

html = """
    <html>
    <head><title>The Dormouse's story</title>
    </head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
soup = BeautifulSoup(html, "lxml")

print soup.prettify()  # 格式化输出

# tags的两个属性 name(标签本身的名字)/attrs(标签的所有属性--字典)

print soup.name     # [document]
print soup.p.name   # p

print soup.p.attrs  # {'class': ['title'], 'name': 'dromouse'}
print soup.p.get('class')   # ['title']

soup.p['class'] = "newClass"  # 修改
print soup.p
del soup.p['class']         # 删除

print soup.p.string         # 获取标签内部的文字

print soup.name         # [document]
print soup.attrs        # {}

