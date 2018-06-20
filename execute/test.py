# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
#import os

browser = webdriver.PhantomJS(executable_path='C:/Users/crab/Desktop/mybooks/execute/phantomjs-2.1.1-windows/bin/phantomjs.exe')


wait = WebDriverWait(browser, 10)


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'http://paper.sciencenet.cn/paper/fieldlist.aspx?id=2'
        browser.get(url)
        '''
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#AspNetPager1.highlight2 input[name = "AspNetPager1_input"]')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#AspNetPager1.highlight2 input[name = "AspNetPager1"]')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#AspNetPager1.highlight2 font[class = "red"]'), str(page)))
        #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        '''
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    with open('html.html', 'a', encoding = 'utf-8') as f:
        f.write(html)
    '''
    result = etree.HTML(html)
    items = result.xpath('')
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')
    '''

def main():
    """
    遍历每一页
    """
    for i in range(1, 2):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()