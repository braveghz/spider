# -*- coding=utf-8 -*-

import urllib
import re

question_url = 'https://www.zhihu.com/question/40007169'


def get_img(_url):
    response = urllib.urlopen(_url)
    html = response.read()

    reg = r'data-actualsrc="(.+?\.jpg)"'
    img_re = re.compile(reg)
    img_list = re.findall(img_re, html)

    for i in range(5):
        urllib.urlretrieve(img_list[i], '%s.jpg' % i)


get_img(question_url)

"""
urllib.urlretrieve(url[, filename[, reporthook[, data]]])  # 直接将远程数据下载到本地
正则匹配 需要稍微看一下源代码 决定正则写啥
"""