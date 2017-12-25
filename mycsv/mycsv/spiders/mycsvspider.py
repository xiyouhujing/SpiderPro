# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider

from mycsv.items import MycsvItem


class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    headers = ['name', 'sex', 'addr', 'email']
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        i['name'] = row['name'].encode()
        i['sex'] = row['sex'].encode()
        i['addr'] = row['addr'].encode()
        i['email'] = row['email'].encode()

        print u"名字是：", i['name']
        print u"性别是：", i['sex']
        print u"地址是：", i['addr']
        print u"邮件是：", i['email']
        print "-------------------------------"
        return i
