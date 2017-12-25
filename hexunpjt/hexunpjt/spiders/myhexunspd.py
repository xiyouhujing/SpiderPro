# -*- coding: utf-8 -*-
import re
import urllib2

import scrapy
from scrapy import Request

from hexunpjt.items import HexunpjtItem


class MyhexunspdSpider(scrapy.Spider):
    name = 'myhexunspd'
    allowed_domains = ['hexun.com']
    uid = 'fjrs168'

    def start_requests(self):
        yield Request("http://"+str(self.uid)+".blog.hexun.com/p1/default.html", headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"})

    def parse(self, response):
        item = HexunpjtItem()
        item['name'] = response.xpath("//span[@class='ArticleTitleText']/a/text()").extract()
        item['url'] = response.xpath("//span[@class='ArticleTitleText']/a/@href").extract()
        pat1 = '<script type="text/javascript" src="(http://click.tool.hexun.com/.*?)"></script>'
        hcurl = re.compile(pat1).findall(str(response.body))[0]

        headers2 = ('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36")
        opener = urllib2.build_opener()
        opener.addheaders = [headers2]
        urllib2.install_opener(opener)
        data = urllib2.urlopen(hcurl).read()
        pat2 = "'click\d*?','(\d*?)'"
        pat3 = "'comment\d*?','(\d*?)'"
        item['hit'] = re.compile(pat2).findall(str(data))
        item['comment'] = re.compile(pat3).findall(str(data))
        yield item
        pat4 = "blog.hexun.com/p(.*?)/"
        data2 = re.compile(pat4).findall(str(response.body))
        if len(data2)>=2:
            totalurl = data2[-2]
        else:
            totalurl = 1

        print u"一共"+str(totalurl)+u"页"
        for i in range(2, int(totalurl)+1):
            nexturl = "http://"+str(self.uid)+".blog.hexun.com/p"+str(i)+"/default.html"
            yield Request(nexturl, callback=self.parse, headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"})

