# -*- encoding:utf-8 -*-

import asyncio
import aiohttp
import time
import json
import sys
import re
from proxypool.db import RedisClient
from proxypool.setting import *
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientConnectionError as ProxyConnectionError



class Tester():
    def __init__(self):
        self.redis = RedisClient()
    
    async def test_single_proxy(self, proxy):
        """
        测试单个代理
        :param proxy:代理
        """
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print('正在测试：', proxy)
                async with session.get(TEST_URL, proxy=real_proxy, timeout=7, allow_redirects=False) as response:
                    response_content = await response.json()
                    ip_response = response_content['origin']
                    juege_proxy = re.search('(.*):', proxy).group(1)
                    if ip_response == juege_proxy:
                        self.redis.max(proxy)
                        print('代理可用', proxy)
            except Exception as e:
                self.redis.decrease(proxy)
                print('代理不可用：', proxy)

    def run(self):
        """
        测试主函数
        """
        print('测试器开始运行')
        try:
            count = self.redis.count()
            print('当前共有', count, '个代理!')
            for i in range(0, count, BATCH_TEST_SIEZ):
                start = i
                stop = min(i + BATCH_TEST_SIEZ, count)
                print('正在测试第', start + 1, '-', stop,  '个代理!')
                test_proxies = self.redis.batch(start, stop)
                loop = asyncio.get_event_loop()
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误:', e.args)

if __name__ == "__main__":
    b = Tester()
    b.run()