#-*- coding: UTF-8 -*-
import json

from bs4 import BeautifulSoup
import pandas
import requests

root_url = "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}"
commentURL = "http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20"



def getCommentCount(news_url):
    newsid = news_url.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
    comment_node = requests.get(commentURL.format(newsid))
    comment_node.encoding = 'utf-8'
    jd = json.loads(comment_node.text.strip('var data='))
    return jd['result']['count']['total']

def getNewsDetail(news_url):
    res_data = {}
    res = requests.get(news_url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    # <h1 id="artibodyTitle" cid="56044" docid="fyphkhk9474048">这名官员曾导致湖北省监狱系统问题频发 今被双开</h1>
    title_node = soup.select('#artibodyTitle')[0]
    res_data['title'] = title_node.text

    # <span class="time-source" id="navtimeSource">2017年12月01日18:30		<span><span data-sudaclick="content_media_p"><a href="http://mp.weixin.qq.com/s?__biz=MzUzNTA4NTYxMA==&amp;mid=2247492369&amp;idx=3&amp;sn=19f0fea2b304725727bee6216cf04d13&amp;chksm=fa887454cdfffd427aa96ed7ed845d51c9b56dba1d3f70a12865784e5c4f93658d531552bb02&amp;scene=0" target="_blank" rel="nofollow">新京报</a></span></span></span>
    time_node = soup.select('.time-source')[0]
    source_node = soup.select('.time-source span a')[0]
    res_data['time'] = time_node.contents[0].strip()
    res_data['source'] = source_node.text

    # <div class="article article_16" id="artibody">
    article_node = soup.select('#artibody p')[:-1]
    res_data['article'] = '\n'.join(p.text.strip() for p in article_node)

    # <p class="article-editor">责任编辑：张玉 </p>
    editor_node = soup.select('.article-editor')[0]
    res_data['editor'] = editor_node.text


    # comments count
    res_data['comment'] = getCommentCount(news_url)

    return res_data

def parserlinkList(page_url):
    newsdetails = []
    res = requests.get(page_url)
    res.encoding = 'utf-8'
    jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))
    for ent in jd['result']['data']:
        newsdetails.append(getNewsDetail(ent['url']))
    return newsdetails

news_total = []
for i in range(1, 2):
    page_url = root_url.format(i)
    newsary = parserlinkList(page_url)
    news_total.extend(newsary)

df = pandas.DataFrame(news_total)
df.to_excel('news.xlsx')






