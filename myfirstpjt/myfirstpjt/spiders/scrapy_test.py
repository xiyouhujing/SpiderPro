# -*- coding: utf-8 -*-

import scrapy
from myfirstpjt.items import MyfirstpjtItem

class ScrapyTestSpider(scrapy.Spider):
    name = 'scrapy_test'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://slide.news.sina.com.cn/s/slide_1_2841_225906.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_193_59149.html/d/1#p=1',
                  'http://ent.sina.com.cn/s/m/2017-12-16/doc-ifypsqka3492139.shtml']

    # urls2 = ['http://www.jd.com',
    #          'http://sina.com.cn',
    #          'http://yum.iqianyue.com']

    # def __init__(self, myurl=None, *args, **kwargs):
    #     super(ScrapyTestSpider, self).__init__(*args, **kwargs)
    #     print u"要爬取的网址为：%s" % myurl
    #     self.start_urls = ['%s' % myurl]

    def parse(self, response):
        item = MyfirstpjtItem()
        item['urltitle'] = response.xpath("/html/head/title/text()").extract()
        print u"以下将显示爬取的网址的标题"
        return item