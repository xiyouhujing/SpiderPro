# -*- coding: utf-8 -*-
import urllib

import scrapy
from scrapy import Request, FormRequest

from doubanpjt.items import DoubanpjtItem


class DoubanspdSpider(scrapy.Spider):
    name = 'doubanspd'
    allowed_domains = ['douban.com']
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }

    def start_requests(self):
        return [Request('https://accounts.douban.com/login', meta={'cookiejar':1}, callback=self.parse)]

    def parse(self, response):
        captcha = response.xpath('//img[@id="captcha_image"]/@src').extract()
        if len(captcha)>0:
            print u"此时有验证码"
            localpath = "F:/SpiderPro/doubanpjt/captcha.png"
            urllib.urlretrieve(captcha[0], filename=localpath)
            print u"请查看本地图片并输入验证码："
            captcha_value = raw_input()
            data = {
                "form_email":"your user name",
                "form_password":"your password",
                "captcha_solution":captcha_value,
                "redir":"https://www.douban.com/people/145022450/",
            }
        else:
            print u"此时没有验证码"
            data = {
                "form_email":"your user name",
                "form_password":"your password",
                "redir":"https://www.douban.com/people/145022450/",
            }
        print u"登陆中..."

        return [FormRequest.from_response(response, meta={"cookiejar": response.meta["cookiejar"]}, headers=self.header, formdata=data, callback=self.next,)]

    def next(self, response):
        print u"此时已经登陆完成并爬取了个人中心的数据"
        # item = DoubanpjtItem()
        username = response.xpath("/html/head/title/text()").extract()
        title = response.xpath("//div[@class='note-header pl2']/a/@title").extract()
        time = response.xpath("//div[@class='note-header pl2']//span[@class='pl']/text()").extract()
        content = response.xpath("//div[@class='mbtr2']//div[@class='note']/text()").extract()
        url = response.xpath("//div[@class='note-header pl2']/a/@href").extract()
        print u"网页标题是："+username[0]
        for i in range(0, len(title)):
            print u"第"+str(i+1)+u"篇文章的信息如下："
            print u"文章标题为："+title[i]
            print u"文章发表时间为：" + time[i]
            print u"文章内容为：" + content[i]
            print u"文章链接为：" + url[i]
            print "----------------------------------"
        # return item


