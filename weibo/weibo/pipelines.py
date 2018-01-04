# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class WeiboPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='hujing', db='weibo', charset='utf8', use_unicode=True)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        for j in range(0, len(item['comments'])):
            content = item['content'][j]
            times = item['times'][j]
            likes = item['likes'][j]
            comments = item['comments'][j]
            transfer = item['transfer'][j]
            sql = 'INSERT INTO kkw(content, times, likes, comments, transfer) VALUES (%s, %s, %s, %s, %s)'
            self.cur.execute(sql, (content, times, likes, comments, transfer))
            self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
