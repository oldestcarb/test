import requests

url = "https://www.baidu.com"
kw = {"kw":"baidu"}
headers = {
    "user-agent":"",
    "connection":"keep-alive"
}
proxy = {
    "http":"http://1.1.1.1:1111",
    "https":"https://2.2.2.2:2222"
}
auth = ("name","password")
formdata = {
    "i":"baidu",
    "email":"qiu@163.com",
    "pwd":"123456"
}

sess = requests.session()
response = requests.get(url, params = kw, headers = headers, proxies = proxy, auth =  auth, verify = True)
responses = sess.post(url, data = formdata, headers = heasers)

print(response.text, response.content,, response.url, response.encoding, response.status_code)

from lxml import etree

html = etree.HTML(text)
result = html.xpth('/bookstore/book[last()-1]//a[@href = "link.html"]')
# /a/@href 获取href属性值
results = html.xpth('//div/a[contains(@id,"qiushi")]')

print(result[0].text,results[0].tag)

import json
import jsonpath

jsonobj = json.loads(text)
result = jsonpath.jsonpath(jsonobj,'$..')

print(result.text)


