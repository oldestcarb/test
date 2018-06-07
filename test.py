import requests

url = "https://www.baidu.com"
headers = {
    "user-agent":"",
    "connection":"keep-alive"
}
kw = {"kw","baidu"}
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

responose = requests.get(url, headers = headers, params = kw, proxy = proxies, auth = auth, verify = True)
responses = requests.post(url, headers = headers, data = formdata)

print(response.text, response.content, response.url, response.encoding, responses.status_code)

from lxml import etree

html = etree.HTML(text)
result = html.xpath('/bookstore/book[last()-1]//a[@href = "link.html"]')
#/a/@href 获取href属性值
results = html.xpath('/div[contains(@id, "qiu")]')

print(result[0].text, results[0].tag)

import json
import jsonpath

jsonobj = json.loads(text)
result = jsonpath.jsonpath(jsonobj, '$..')

import re

pattern = re.compile(r'\d+\d?')
s = "one123two456three789"
a = pattern.match(s)
# search findall finditer
b = pattern.split(s)
c = pattern.sub(r'four',s)

#请求报头
Get https://www.baidu.com/ HTTP/1.1
Host: www.baidu.com
Connection: Keep-alive
User-Agent: 
Upgrade-Insecure-Requests: 1
referer:
Accept:
Accept-encoding:
Accept-language:
Accept-Charset:
Cookie:
Content-Type: