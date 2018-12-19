# -*- encoding:utf-8 -*-

import re
import time
import requests
from lxml import etree
from requests import ConnectionError
import sys
import os
import random
from random import shuffle
import pymysql
import json
import threading
from queue import Queue 

    
def get_kw(kw, judge):
    """
    从表_cs_bmnars_vigenebio_keyword中获取查询关键字
    """
    # 数据库连接
    db = pymysql.connect(host='localhost', user='bmnars', password='vi93nwYV', port=3306, db='bmnars')
    cursor = db.cursor()
    # 更新时间
    update_time = time.strftime('%Y-%m-%d',time.localtime())
    # print('judge:\t', type(judge), judge)

    if judge == 0:
        # 查询状态未更新的关键字，爬取之后状态改为 y
        sql = 'select kw from _cs_bmnars_vigenebio_kw where status = 0 and isrun = 0 and id = %s;'
        # print(sql)
        try:
            cursor.execute(sql, (kw))
            # 获取一行
            row = cursor.fetchone()
            print(row)
            return row[0]
        except:
            print('get kw error!')
        finally:
            cursor.close()
            db.close()

b = get_kw(1,0)
print(b)