import requests

url = 'https://www.baidu.com'
headers = {
    'user-agent':'',
    'connection':'keep-alive'
}
kw = {'kw':'baidu'}
formdata = {
    'i':'baidu',
    'email':'qiu@163.com',
    'pwd':'123456'
}
proxy = {
    'http':'http://1.1.1.1:1111',
    'https':'https://2.2.2.2:2222'
}
auth = ('name', 'password')
sess = requests.session()

response = requests.get(url, params = kw, headers = headers, proxie = proxy, auth = auth, verify = False)
responses = sess.post(url, data = formdata, headers = headers)

print(response.text, response.content, response.url, response.encoding, response.status_code)

from lxml import etree

html = etree.HTML(text)
result = html.xpath('/bookstore/book[last()-1]//a[contains(@id,"qiu") and @href = "link.html"]')[0].text

import json
import jsonpath

jsonobj = josn.loads(text)
result = jsonpath.jsonpath(jsonobj,'$..')

import re

pattern = re.compile(r'\d?\d+', re.S, re.I)
s = 'one123two456three789'
a = pattern.match(s, 0, 9)
# search, findall, finditer, split
b = pattern.sub(r'four', s)

get https://www.baidu.com/ http/1.1
host: www.baidu.com
connection: keep-alive
upgrade-insecure-requests: 1
user-agent:
accept:
referer:
accept-encoding:
accpet-language:
accept-charset:
cookie:
content-type:

