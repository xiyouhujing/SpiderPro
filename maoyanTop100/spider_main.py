# -*- coding: UTF-8 -*-
from maoyanTop100 import url_manage, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manage.UrlManage()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, url):
        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.get_html_cont(new_url)
            new_data = self.parser.html_parser(html_cont)
            self.outputer.output_database(new_data)

if __name__ == '__main__':
    root_url = "http://maoyan.com/board/4?offset={}"
    top_spider = SpiderMain()
    top_spider.craw(root_url)
