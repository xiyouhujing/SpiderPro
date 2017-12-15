# -*- coding: UTF-8 -*-

import re
import urllib2

url = "https://www.csdn.net/"


def getlink(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    file = urllib2.urlopen(req).read()
    data = str(file)
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    link = list(set(link))
    return link


linklist = getlink(url)
for link in linklist:
    print link[0]