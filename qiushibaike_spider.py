# -*- coding: UTF-8 -*-
import urllib2
from bs4 import BeautifulSoup
import pandas
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def parserLink(page_url):
    articles = []
    req = urllib2.Request(page_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    data = urllib2.urlopen(req).read()
    soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
    article_urls = soup.find_all('a', class_="contentHerf")

    for item in article_urls:
        article_url = item['href']
        new_url = "https://www.qiushibaike.com" + str(article_url)
        content = getAticleDetial(new_url)
        articles.append(content)
    return articles

def getAticleDetial(new_url):
    contents = {}
    req = urllib2.Request(new_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    article_html = urllib2.urlopen(req).read()
    soup2 = BeautifulSoup(article_html, 'html.parser', from_encoding='utf-8')
    user_node = soup2.find('h2')
    article_node = soup2.find('div', class_="content")
    contents['user'] = user_node.get_text().encode('unicode_escape')
    contents['article'] = article_node.get_text().strip('\n\n').encode('unicode_escape')

    return contents

url = "https://www.qiushibaike.com/8hr/page/{}/"
article_total = []
for i in range(1, 2):
    page_url = url.format(i)
    articles = parserLink(page_url)
    article_total.extend(articles)

df = pandas.DataFrame(article_total)
df.to_excel('qiushi.xlsx')

