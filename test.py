import requests

url = "https://www.baidu.com"
headers = {
    "user-agent":"",
    "connection":"keep-alive"
}
kw = {"kw":"baidu"}
formdata = {
    "i":"baidu",
    "email":"qiu@163.com",
    "pwd":"123456"
}
proxy = {
    "http":"http://1.1.1.1:1111",
    "https":"https://2.2.2.2:2222"
}
auth = ("name","password")
sess = requests.session()

response = requests.get(url, params = kw, headers = headers, proxies = proxy, auth = auth, verify = True)
responses = sess.post(url, data = formdata, headers = headers)

print(response.text, response.content, response.url, response.status_code, response.encoding)

from lxml import etree

html = etree.HTML(text)
result = html.xpath('/bookstore/book[last()-1]//a[@href = "link.html"]')
# /a/@href 获取href属性值
results = html.xpath('/div[contains(@id,"qiu")]')

print(result[0].text, result[0].tag)

import json
import jsonpath

josnobj = json.loads(text)
result = jsonpath.jsonpath(josnobj, '$..')

import re

pattern = re.compile(r'\d?\d+')
s = "one123two456three789"
a = pattern.match(s,0,9)
# search findall finditer split
b = pattern.sub(r'four',s)

# 请求报头
get https://www.baidu.com http/1.1
host: www.baidu.com
connection: keep-alive
upgrade-insecure-requests: 1
user-agent:
accept:
referer:
accept-encoding:
accept-lanuage:
accept-charset:
cookie:
content-type: