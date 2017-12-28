# -*- coding: UTF-8 -*-
import urllib2

import MySQLdb
from lxml import etree

def get_page(url):
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
    opener = urllib2.build_opener()
    opener.addheaders = [headers]
    html_cont = opener.open(url).read()
    page = etree.HTML(html_cont.decode('utf-8'))
    return page

def parse_page(page):
    title1 = page.xpath('//div[@class="movie-item-info"]/p/a/text()')
    url = page.xpath('//dl[@class="board-wrapper"]/dd/a/@href')
    rank = page.xpath('//dl[@class="board-wrapper"]/dd/i/text()')
    star1 = page.xpath('//p[@class="star"]/text()')
    time1 = page.xpath('//p[@class="releasetime"]/text()')
    score1 = page.xpath('//p[@class="score"]//i[@class="integer"]/text()')
    score2 = page.xpath('//p[@class="score"]//i[@class="fraction"]/text()')
    score = []
    title = []
    link = []
    star = []
    times = []
    data = {}
    for i in range(len(rank)):
        link1 = "http://maoyan.com"+url[i]
        score3 = score1[i]+score2[i]
        star2 = star1[i].strip()[3:]
        time2 = time1[i].strip()[5:]
        title2 = title1[i].strip()
        title.append(title2)
        score.append(score3)
        link.append(link1)
        star.append(star2)
        times.append(time2)

    data['rank'] = rank
    data['title'] = title
    data['link'] = link
    data['star'] = star
    data['score'] = score
    data['times'] = times
    return data

def write_to_database(data):
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='hujing', db='maoyan', charset='utf8',
                           use_unicode=True)
    cur = conn.cursor()
    for i in range(0, len(data['rank'])):
        pat = 'INSERT INTO top(rank, title, star, times, score, link) VALUES(%s, %s, %s, %s, %s, %s)'
        cur.execute(pat, (data['rank'][i].decode('gbk'), data['title'][i], data['star'][i], data['times'][i], data['score'][i], data['link'][i]))
        conn.commit()
    conn.close()
    cur.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_page(url)
    data = parse_page(html)
    write_to_database(data)

if __name__ == '__main__':
    for i in range(10):
        main(i*10)