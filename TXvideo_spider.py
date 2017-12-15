# -*- coding: UTF-8 -*-

import urllib2
import cookielib
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

vid = "2220694119"
comid = "0"
url = "https://coral.qq.com/article/"+vid+"/comment?commentid="+comid+"&reqnum=10"
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "referer": "https://v.qq.com/txyp/coralComment_yp_1.0.htm"
}

cjar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cjar))
headall = []
for key, value in headers.items():
    item = (key, value)
    headall.append(item)

opener.addheaders = headall
urllib2.install_opener(opener)

def craw(vid, comid):
    url = "https://coral.qq.com/article/"+vid+"/comment?commentid="+comid+"&reqnum=10"
    data = urllib2.urlopen(url).read().encode('utf-8', 'ignore')
    return data

idpat = '"id":"(.*?)",'
userpat = '"nick":"(.*?)",'
conpat = '"content":"(.*?)",'

for i in range(1, 10):
    print "--------------------------"
    print "第"+str(i)+"页评论内容"
    data = craw(vid, comid)

    for j in range(0, 10):
        idlist = re.compile(idpat, re.S).findall(data)
        userlist = re.compile(userpat, re.S).findall(data)
        conlist = re.compile(conpat, re.S).findall(data)
        print "user:" + eval('u"'+userlist[j]+'"')
        print "comments:" + eval('u"'+conlist[j]+'"')
        print "\n"

    comid = idlist[5]