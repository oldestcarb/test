# -*- encoding:utf-8 -*-

from db import RedisClient
import sys

conn = RedisClient()

def set(proxy):
    result = conn.add(proxy)
    print(proxy + ' 录入成功' if result else proxy + ' 录入失败')

def scan():
    addr = input('请输入要导入的代理文件绝对地址：')
    print('开始导入代理')
    with open(addr, 'r', encoding = 'utf-8') as f:
        proxy_list = f.readlines()
    for proxy in proxy_list:
        set(proxy.strip())

if __name__ == '__main__':
    scan()
    print('当前代理池代理总数：' ,conn.count())
