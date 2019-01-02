import json
import re
import sys
import requests


def test_proxy(proxy):
    # 随机获取代理IP
    # print(proxy)
    # 获取IP不要端口，判断与httpbin返回的IP是否相等
    judge_proxy_pattern = re.compile('(.*):')
    judge_proxy = judge_proxy_pattern.search(proxy).group(1)
    # print(judge_proxy)
    # 随机获取user-agent
    proxies = {'http': 'http://' + proxy, 'https': 'https://' + proxy}
    # print(proxies)
    response = requests.get(
        'http://httpbin.org/get', proxies=proxies, timeout=4)

    # 获取httpbin上的IP
    print(response.text)
    dict_response = json.loads(response.text)
    ip_response = dict_response['origin']
    print(ip_response)


if __name__ == "__main__":

    test_proxy('61.135.217.7:80')