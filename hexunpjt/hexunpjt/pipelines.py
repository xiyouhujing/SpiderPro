# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class HexunpjtPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='hujing', db='hexun', charset='utf8', use_unicode=True)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        for j in range(0, len(item['name'])):
            name = item['name'][j]
            url = item['url'][j]
            hit = item['hit'][j]
            comment = item['comment'][j]
            sql = 'INSERT INTO myhexun(name, url, hit, comment) VALUES (%s, %s, %s, %s)'
            self.cur.execute(sql, (name, url, hit, comment))
            self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
