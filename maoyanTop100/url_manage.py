# -*- coding: UTF-8 -*-
class UrlManage(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        return len(self.new_urls) != 0

    def add_new_url(self, root_url):
        for i in range(10):
            page_url = root_url.format(i*10)
            self.new_urls.add(page_url)

    def get_new_url(self):
        page_url = self.new_urls.pop()
        self.old_urls.add(page_url)
        return page_url








