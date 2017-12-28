# -*- coding: UTF-8 -*-
from lxml import etree


class HtmlParser(object):
    def html_parser(self, html_cont):
        data = {}

        page = etree.HTML(html_cont.decode('utf-8'))
        rank = page.xpath('//dl[@class="board-wrapper"]/dd/i/text()')
        title1 = page.xpath('//div[@class="movie-item-info"]/p/a/text()')
        urls = page.xpath('//dl[@class="board-wrapper"]/dd/a/@href')
        star1 = page.xpath('//p[@class="star"]/text()')
        time1 = page.xpath('//p[@class="releasetime"]/text()')
        score1 = page.xpath('//p[@class="score"]//i[@class="integer"]/text()')
        score2 = page.xpath('//p[@class="score"]//i[@class="fraction"]/text()')

        score = []
        title = []
        link = []
        star = []
        times = []
        for i in range(len(rank)):
            lin = "http://maoyan.com"+str(urls[i])
            sco = score1[i]+score2[i]
            star2 = star1[i].strip()[3:]
            time2 = time1[i].strip()[5:]
            title2 = title1[i].strip()
            title.append(title2)
            score.append(sco)
            link.append(lin)
            star.append(star2)
            times.append(time2)

        data['rank'] = rank
        data['title'] = title
        data['link'] = link
        data['star'] = star
        data['score'] = score
        data['times'] = times

        return data





