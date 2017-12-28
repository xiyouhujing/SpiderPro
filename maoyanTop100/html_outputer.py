# -*- coding: UTF-8 -*-
import MySQLdb


class HtmlOutputer(object):

    def output_database(self, data):
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='hujing', db='maoyan', charset='utf8', use_unicode=True)
        cur = conn.cursor()
        for i in range(0, len(data['title'])):
            pat = 'INSERT INTO top(rank, title, star, times, score, link) VALUES(%s, %s, %s, %s, %s, %s)'
            cur.execute(pat, (data['rank'][i].decode('gbk'), data['title'][i], data['star'][i], data['times'][i], data['score'][i], data['link'][i]))
            conn.commit()
        conn.close()
        cur.close()