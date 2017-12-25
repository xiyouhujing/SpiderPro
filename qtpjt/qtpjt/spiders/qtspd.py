# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request

from qtpjt.items import QtpjtItem


class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ['http://www.58pic.com/piccate/3-0-0.html']

    def parse(self, response):
        item = QtpjtItem()
        paturl = '(http://pic.qiantucdn.com/58pic/.*?).jpg'
        item['picurl'] = re.compile(paturl).findall(str(response.body))
        patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
        item['picid'] = re.compile(patlocal).findall(str(response.body))
        yield item
        for i in range(1, 101):
            nexturl = "http://www.58pic.com/piccate/3-0-0-" + str(i) + ".html"
            yield Request(nexturl, callback=self.parse)