# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request

from weibo.items import WeiboItem


class WeiboSpiderSpider(scrapy.Spider):
    name = 'weibo_spider'
    allowed_domains = ['sina.com']
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
    cookies = 'your cookies'

    def start_requests(self):
        for i in range(1, 58):
            nexturl = "https://weibo.cn/1278089051/profile?hasori=1&haspic=1&endtime=20160822&advancedfilter=1&page=" + str(i)
            yield Request(nexturl, callback=self.parse, headers=self.header, cookies=self.cookies)
        # yield Request('https://weibo.cn/1278089051/profile?hasori=1&haspic=1&endtime=20160822&advancedfilter=1&page=1', cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        item = WeiboItem()
        conts = []
        datas = response.xpath('//div[@class="c"]/div/span[@class="ctt"]')
        for i in range(0, len(datas)):
            conts.append(datas[i].xpath('string(.)').extract())
        item['content'] = conts
        item['times'] = response.xpath('//span[@class="ct"]/text()').extract()
        item['likes'] = response.xpath('//div[@class="c"]/div[2]/a[3]/text()').extract()
        item['comments'] = response.xpath('//div[@class="c"]/div/a[@class="cc"]/text()').extract()
        item['transfer'] = response.xpath('//div[@class="c"]/div[2]/a[4]/text()').extract()
        yield item
        # for i in range(2, 58):
        #     nexturl = "https://weibo.cn/1278089051/profile?hasori=1&haspic=1&endtime=20160822&advancedfilter=1&page="+str(i)
        #     yield Request(nexturl, callback=self.parse, headers=self.header,  dont_filter=True)