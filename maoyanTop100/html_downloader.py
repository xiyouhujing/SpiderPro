# -*- coding: UTF-8 -*-
import urllib2


class HtmlDownloader(object):
    def get_html_cont(self, new_url):
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
        opener = urllib2.build_opener()
        opener.addheaders = [headers]
        html_cont = opener.open(new_url).read()
        return html_cont