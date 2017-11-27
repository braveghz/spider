### 还是下载的美人图片

使用Python库
- urllib2
- requests
- bs4

`urlopen` 打开特定URL 获取页面

使用 `BeautifulSoup` 解析一下 得到soup

`find_all` 得到所有图片URL

`requests.get(url).content` 得到图片内容，写到本地