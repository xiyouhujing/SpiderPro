# -*- coding: UTF-8 -*-
import re

import MySQLdb
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def search():
    try:
        browser.get("https://www.taobao.com/")
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button")))
        input.send_keys(u'美食')
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.total")))
        get_products()
        return total.text
    except TimeoutException:
        return search()

def next_page(page_number):
    try:
        input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit"))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul > li.item.active > span"), str(page_number))
        )
        get_products()
    except TimeoutException:
        next_page(page_number)

def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-itemlist .items .item")))
    html = browser.page_source
    doc = pq(html)
    items = doc("#mainsrp-itemlist .items .item").items()
    for item in items:
        product = {
            'image': item.find(".pic .img").attr("src"),
            'price': item.find(".price").text(),
            'deal': item.find(".deal-cnt").text()[:-3],
            'title': item.find(".title").text(),
            'shop': item.find(".shop").text(),
            'location': item.find(".location").text()
        }
        print product
        save_to_db(product)

def save_to_db(result):
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='hujing', db='taobao', charset='utf8', use_unicode=True)
    cur = conn.cursor()
    pat = 'INSERT INTO meishi(title, image, price, deal, shop, location) VALUES(%s, %s, %s, %s, %s, %s)'
    cur.execute(pat, (result['title'], result['image'], result['price'], result['deal'], result['shop'], result['location']))
    conn.commit()
    cur.close()
    conn.close()

def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2, total+1):
        next_page(i)

if __name__ == '__main__':
    main()