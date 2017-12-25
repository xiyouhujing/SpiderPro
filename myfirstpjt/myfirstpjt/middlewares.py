# -*- coding: utf-8 -*-
# import random
# from myfirstpjt.settings import IPPOOL
# from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
#
# class IPPOOLS(HttpProxyMiddleware):
#     def __init__(self, ip=''):
#         self.ip = ip
#     def process_request(self, request, spider):
#         thisip = random.choice(IPPOOL)
#         print u"当前使用的IP是："+thisip["ipaddr"]
#         request.meta["proxy"] = "http://"+thisip["ipaddr"]