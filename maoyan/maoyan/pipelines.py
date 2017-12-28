# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class MaoyanPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='hujing', db='maoyan', charset='utf8', use_unicode=True)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        for i in range(len(item['rank'])):
            rank = item['rank'][i]
            title = item['title'][i].strip()
            star = item['star'][i].strip()[3:]
            times = item['times'][i].strip()[5:]
            score = str(item['score1'][i]) + str(item['score2'][i])
            link = "http://maoyan.com"+str(item['link'][i])

            # link = "http://maoyan.com"+str(link1)
            # times = times1.strip()[5:]
            # score = str(score1) + str(score2)
            # star = star1[i].strip()[3:]

            pat = 'INSERT INTO top(rank, title, star, times, score, link) VALUES(%s, %s, %s, %s, %s, %s)'
            self.cur.execute(pat, (rank, title, star, times, score, link))
            self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
