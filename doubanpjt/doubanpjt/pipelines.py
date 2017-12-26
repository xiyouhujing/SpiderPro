# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class DoubanpjtPipeline(object):
    # def __init__(self):
    #     self.conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='hujing', db='douban', charset='utf8', use_unicode=True)
    #     self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        # for j in range(0, len(item['title'])):
        #     title = item['title'][j]
        #     time = item['time'][j]
        #     content = item['content'][j]
        #     url = item['url'][j]
        #     pat ="INSERT INTO mydouban(title, time, content, url) VALUES(%s, %s, %s, %s)"
        #     self.cur.execute(pat, (title, time, content, url))
        #     self.conn.commit()
        return item

    # def close_spider(self, spider):
    #     self.cur.close()
    #     self.conn.close()
