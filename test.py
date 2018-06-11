# -*- coding:utf-8 -*-

import requests
import json
import time
from lxml import etree
from Queue import Queue
import threading

class Thread_Crawl(threading.Thread):
    def __init__(self, thread_name, page_queue, data_queue):
        super(Thread_Crawl, self).__init__()
        self.thread_name = thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    def run(self):
        print("启动" +　self.thread_name)
        while not crawl_exit:
            try:
                page = self.page_queue.get(False)
                url = "http://www.qiushibaike.com/8hr/page/" + str(page) +"/"
                #print url
                content = requests.get(url, headers = self.headers).text
                time.sleep(1)
                self.data_queue.put(content)                
            except:
                pass
        print("启动" +　self.thread_name)
        
class Thread_Parse(threading.Thread):
    def __init__(self, thread_name, data_queue, filename, lock):
        super(Thread_Parse, self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.filename = filename
        self.lock = lock

    def run(self):
        print("启动" +　thread_name)
        whil not parse_exit:
            try:
                html = self.data_queue.get(False)
                self.parse(html)
            except:
                pass
        print("退出"　+ self.thread_name)

    def parse(self, html):
        html = etree.HTML(html)
            node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')

        for node in node_list:
            # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
            username = node.xpath('./div/a/@title')[0]
            # 图片连接
            image = node.xpath('.//div[@class="thumb"]//@src')#[0]
            # 取出标签下的内容,段子内容
            content = node.xpath('.//div[@class="content"]/span')[0].text
            # 取出标签里包含的内容，点赞
            zan = node.xpath('.//i')[0].text
            # 评论
            comments = node.xpath('.//i')[1].text

            items = {
                "username" : username,
                "image" : image,
                "content" : content,
                "zan" : zan,
                "comments" : comments
            }

            with self.lock:
                self.filename.write(json.dumps(items, ensure_ascii = False).encode("utf-8") + "\n")

crawl_exit = False
parse_exit = False

def main():
    page_queue = Queue(20)
    for i in range(1,21):
        page_queue.put(i)
    
    data_queue = Queue()
    filename = open("duanzi.json","a")

    lock = threading.lock()

    crawl_list = ["采集线程1号","采集线程2号","采集线程3号"]
    thread_crawl = []
    for thread_name in crawl_list:
        thread = Thread_Crawl(thread_name, page_queue, data_queue)
        thread.start()
        thread_crawl.append(thread)

    parse_list = ["解析线程1号","解析线程2号","解析线程3号"]
    thread_parse = []
    for thread_name in parse_list:
        thread = Thread_Parse(thread_name, data_queue, filename, lock)
        thread.start()
        thread_parse.append(thread)

    while not page_queue.empty():
        pass

    global crawl_exit
    crawl_exit = True
    print("page_queue为空")

    for thread in thread_crawl:
        thread.join()
        print("1")

    global parse_exit
    parse_exit = True
    #print("page_queue为空")

    for thread in thread_parse:
        thread.join()
        print("2")

    with lock:
        filename.close()
    
if __name__ == '__main__':
    main()


