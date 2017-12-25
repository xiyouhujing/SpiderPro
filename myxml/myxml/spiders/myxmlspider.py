# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, node):
        i = MyxmlItem()
        i['title'] = node.xpath('/rss/channel/item/title/text()').extract()
        i['link'] = node.xpath('/rss/channel/item/link/text()').extract()
        i['author'] = node.xpath('/rss/channel/item/author/text()').extract()

        for j in range(len(i['title'])):
            print u"第"+str(j+1)+u"篇文章"
            print u"标题是"
            print i['title'][j]
            print u"对应的链接是"
            print i['link'][j]
            print u"对应的作者是"
            print i['author'][j]
            print "--------------------------"

        return i
