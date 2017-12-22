# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mysqlpjt.items import MysqlpjtItem


class SinaSpiderSpider(CrawlSpider):
    name = 'sina_spider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    # http: // news.sina.com.cn / c / nd / 2017 - 12 - 22 / doc - ifypxrpp3286106.shtml
    rules = (
        Rule(LinkExtractor(allow='http://news.sina.com.cn/.*?/[0-9]{4}-[0-9]{2}-[0-9]{2}/doc-.*?.shtml'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MysqlpjtItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['name'] = response.xpath('/html/head/title/text()').extract()
        i['keywd'] = response.xpath('//meta[@name="keywords"]/@content').extract()
        return i
