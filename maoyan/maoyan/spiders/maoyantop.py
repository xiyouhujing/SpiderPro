# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from maoyan.items import MaoyanItem


class MaoyantopSpider(scrapy.Spider):
    name = 'maoyantop'
    allowed_domains = ['maoyan.com']

    def start_requests(self):
        yield Request("http://maoyan.com/board/4?offset=0", headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'})

    def parse(self, response):
        item = MaoyanItem()
        item['rank'] = response.xpath('//dl[@class="board-wrapper"]/dd/i/text()').extract()
        item['title'] = response.xpath('//div[@class="movie-item-info"]/p/a/text()').extract()
        item['link'] = response.xpath('//dl[@class="board-wrapper"]/dd/a/@href').extract()
        item['star'] = response.xpath('//p[@class="star"]/text()').extract()
        item['times'] = response.xpath('//p[@class="releasetime"]/text()').extract()
        item['score1'] = response.xpath('//p[@class="score"]//i[@class="integer"]/text()').extract()
        item['score2'] = response.xpath('//p[@class="score"]//i[@class="fraction"]/text()').extract()

        # for i in range(0, 10):
        #     item['link'][i] = "http://maoyan.com"+link[i]
        #     item['score'][i] = score1[i]+score2[i]
        #     item['star'] = star[i].strip()[3:]
        #     item['times'] = times[i].strip()[5:]
        #     item['title'] = title[i].strip()

        yield item

        for i in range(1, 10):
            nexturl = "http://maoyan.com/board/4?offset=" + str(i*10)
            yield Request(nexturl, callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'})
