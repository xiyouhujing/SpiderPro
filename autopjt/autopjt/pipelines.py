# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class AutopjtPipeline(object):
    def __init__(self):
        self.file = codecs.open('F:/SpiderPro/dangdang.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        for j in range(0, len(item['name'])):
            name = item['name'][j]
            price = item['price'][j]
            comnum = item['comnum'][j]
            link = item['link'][j]
            goods = {'name':name, 'price':price, 'comnum':comnum, 'link':link}
            i = json.dumps(dict(goods), ensure_ascii=False)
            line = i + '\n'
            self.file.write(line)
        return item

    def close_file(self):
        self.file.close()
