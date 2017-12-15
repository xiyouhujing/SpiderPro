# -*- coding: UTF-8 -*-

import urllib2
import time
from bs4 import BeautifulSoup
import pandas


def use_header(url):
    try:
        header = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
        opener = urllib2.build_opener()
        opener.addheaders = [header]
        urllib2.install_opener(opener)
        html_cont = opener.open(url).read()
        return html_cont
    except urllib2.URLError as e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
        time.sleep(10)
    except Exception as e:
        print "exception:" + str(e)
        time.sleep(1)


def get_article_url(pageurl):
    new_urls = set()
    html_cont = use_header(pageurl)
    soup = BeautifulSoup(html_cont, 'html.parser')
    url_nodes = soup.find_all('h3')
    for url_node in url_nodes:
        new_url_node = url_node.find('a')
        new_urls.add(new_url_node['href'])
    return new_urls

def get_content(new_url):
    article_data = {}

    html_cont = use_header(new_url)
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

    title_node = soup.select('#activity-name')[0]
    article_data['title'] = title_node.text.lstrip('\r\n').strip('   ')

    author_node = soup.select('#post-user')[0]
    article_data['author'] = author_node.text

    content_node = soup.select('#js_content')[0]
    article_data['content'] = content_node.text.lstrip('\n')

    return article_data

def parserUrl(page_url):
    article_details = []
    new_urls = get_article_url(page_url)
    for new_url in new_urls:
        article_details.append(get_content(new_url))
    return article_details

root_url = "http://weixin.sogou.com/weixin?query=%E7%89%A9%E8%81%94%E7%BD%91&_sug_type_=&s_from=input&_sug_=y&type=2&page={}&ie=utf8"
article_totle = []
for i in range(1, 5):
    pageurl = root_url.format(i)
    data = parserUrl(pageurl)
    article_totle.extend(data)

df = pandas.DataFrame(article_totle)
df.to_excel('weixin.xlsx')


