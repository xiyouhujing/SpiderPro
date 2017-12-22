# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

import MySQLdb


class MysqlpjtPipeline(object):
    def __init__(self):
        # self.file = codecs.open('F:/SpiderPro/mydatas.json', 'wb', encoding="utf-8")
        self.conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='hujing', db='mypydb', charset='utf8', use_unicode=True)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        # i = json.dumps(dict(item), ensure_ascii=False)
        # line = i + '\n'
        # print line
        # self.file.write(line)
        # return item
        name = item['name'][0]
        key = item['keywd'][0]
        sql = "INSERT INTO mytb(title, keywd) VALUES(%s, %s)"
        self.cur.execute(sql, (name, key))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
