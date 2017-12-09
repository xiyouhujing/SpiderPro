# -*- coding: UTF-8 -*-
import urllib
import urllib2
import re


def craw(url, page):
    pageurl = url.format(page)
    html1 = urllib2.urlopen(pageurl).read()
#    print html1
#    soup = BeautifulSoup(html1, 'html.parser', from_encoding='utf-8')
#    nodes = soup.find_all('li', class_='gl-item')

    imagelist = re.findall(r'<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg|.+?\.png)">', str(html1))

    x = 1
    for imageurl in imagelist:
        imagename = "F:/images/"+str(page)+str(x)+".jpg"
        url = "http://"+imageurl
        try:
            urllib.urlretrieve(url, filename=imagename)
        except urllib2.URLError as e:
            if hasattr(e, "code"):
                x+=1
            if hasattr(e, "reason"):
                x+=1
        x+=1

for i in range(1, 20):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page={}"
    craw(url, i)
