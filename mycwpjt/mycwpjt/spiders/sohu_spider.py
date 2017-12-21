# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mycwpjt.items import MycwpjtItem


class SohuSpiderSpider(CrawlSpider):
    name = 'sohu_spider'
    allowed_domains = ['sohu.com']
    start_urls = ['http://sohu.com/']

    # http: // www.sohu.com / a / 211688971_428290
    rules = (
        Rule(LinkExtractor(allow=('http://www.sohu.com/a/.*?')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MycwpjtItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['name'] = response.xpath('/html/head/title/text()').extract()
        i['link'] = response.xpath("//link[@rel='canonical']/@href").extract()
        print i['name'][0]
        print i['link'][0]
        print "------------------------"
