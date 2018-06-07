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
    "http":"http://1.1.1.1:111",
    "https":"https://2.2.2.2:2222"
}
auth = ("name","password")
sess = requests.session()

response = requests.get(url, headers = headers, params = kw, proxies = proxy, auth = athe, verify = True)
responses = sess.post(url, data = formdata, headers = headers) 

print(response.text,response.content, response.url, response.encoding, response.status_code)

from lxml import etree

html = etree.HTML(text)

result = html.xpath('/bookstore/book[last()-1]//a[@href = "link.html"]')
#/a/@href 获取href属性值
results = html.xpath('/div[contains(@id,"qiu")]')

print(result[0].text,results[0].tag)

import json
import jsonpath

jsonboj = json.loads(text)
result = jsonpath.jsonpath(jsonobj,'$..')

$ / . @ / . .. // ..

import re

pattern = re.compile(r'\d+')
s = "one123two456three789"
a = pattern.match(s,0,9)
#search findall finditer 
b = pattern.split(s)
c = pattern.sub(r'four',s)