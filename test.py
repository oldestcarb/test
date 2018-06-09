import requests

url = "https://www.baidu.com"
headers = {
    "user-agent":"",
    "connnection":"keep-live"
}
kw = {"kw","baidu"}
formdata = {
    "i","baidu",
    "email":"qiu@163.com",
    "pwd":"123456"
}
proxy = {
    "http":"http://1.1.1.1:1111",
    "https":"https://2.2.2.2:2222"
}
auth = ("name":"password")
sess = requests.session()

resposne = requests.get(url, headers = headers, params = kw, proxies = proxy, auth = auth, verify = True)
resposnes = sess.post(url, data = formdata, headers = headers)

print(response.text, response.content, response.url, response.encoding, response.status_code)

from lxml import etree

html = etree.HTML(text)
result = html.xpath('/bookstore/book[last()-1]//a[@href = "link.html"]')
#/a/@href 获取href属性值
results = html.xpath('/div[contains(@id,"qiu")]')

print(result[0].text, results[0].tag)

import json
import jsonpath

jsonobj = json.loads(text)
result = jsonpath.jsonpath(jsonobj,'$..')

import re

pattern = re.compile(r'\d+\d?')
s = "one123two456three789"
a = pattern.match(s,1,9)
# search findall finditer spilt
#b = pattern.spilt(s)
c = pattern.sub(r'four',s)

#请求报头
get https://www.baidu.com/ http/1.1
host: www.baidu.com
connection: keep-alive
upgrade-secure-requests: 1
user-agent:
accept:
referer:
accept-encoding:
accept-language:
accept-charset:
cookie:
content-type: