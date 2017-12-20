# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from autopjt.items import AutopjtItem


class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4002203.html']

    def parse(self, response):
        item = AutopjtItem()
        item['name'] = response.xpath('//a[@name="itemlist-title"]/@title').extract()
        item['price'] = response.xpath('//span[@class="price_n"]/text()').extract()
        item['link'] = response.xpath('//a[@name="itemlist-title"]/@href').extract()
        item['comnum'] = response.xpath('//a[@name="itemlist-review"]/text()').extract()
        yield item
        for i in range(1, 60):
            url = "http://category.dangdang.com/pg"+str(i)+"-cid4002203.html"
            yield Request(url, callback=self.parse)