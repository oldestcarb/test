# -*- encoding:utf-8 -*-

import re
import time
import sys
import os
import random
from random import shuffle
import requests
import json

class Proxy():
    def __init__(self):
        super(Proxy).__init__()
        self.url = 'http://httpbin.org/get'
        self.list_ip = sys.path[0] + '/ip_response.txt'
        self.list_user_agent = sys.path[0] + '/user-agents.txt'

    def test_proxy(self):
        """
        测试代理IP是否可用，返回可用IP
        """
        # 随机获取代理IP
        with open(self.list_ip, 'r', encoding = 'utf-8') as f:
            list_proxy = f.readlines()
            shuffle(list_proxy)

        for proxy in list_proxy:
            proxy = proxy.strip()
            # print(proxy)
            # 获取IP不要端口，判断与httpbin返回的IP是否相等
            judge_proxy_pattern = re.compile('(.*):')
            judge_proxy = judge_proxy_pattern.search(proxy).group(1)
            # print(judge_proxy)

            # 随机获取user-agent
            with open(self.list_user_agent, 'r' , encoding = 'utf-8') as f:
                list_user_agent = f.readlines()
            user_agent = random.choice(list_user_agent).strip()
            # print(user_agent)
            headers = {'user-agent':user_agent}

            proxies = {
                'http':'http://' + proxy ,
                'https':'https://' + proxy 
            }
            # print(proxies)

            try:
                response = requests.get(self.url, headers = headers, proxies = proxies, timeout = 4)
            except:
                response = ''
                # list_proxy.remove(proxy)
            if response:
                try:
                    # 获取httpbin上的IP
                    # print(response.text)
                    dict_response = json.loads(response.text)
                    ip_response = dict_response['origin']
                    # print(ip_response)

                except:
                    ip_response = ''
                # 判断返回的IP是否和本地的相等
                if ip_response == judge_proxy:
                    return proxy

def main():
    """
    遍历每一页索引页
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    start_time = time.time()

    get_proxy = Proxy()
    proxy = get_proxy.test_proxy()
    print('proxy:\t' + proxy)
    
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    print('用时:\t' , time.time()-start_time)


if __name__ == '__main__':
    main()