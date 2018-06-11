### requests
```pthon
import requests

url = "https://www.baidu.com"

kw = {"kw":"baidu"}

headers = {
    "user-agent":"",
    "cookie":""
}

formdata = {
    "i":"fanyi",
    "email":"qiu@163.com",
    "pwd":"1234567" 
}

proxy = {
    "http":"http://1.1.1.1:1111",
    "https":"https://2.2.2.2:2222" 
}

auth = ("name","password" )

sess = requests.session()

response = requests.get(url, headers = headers, params = kw, proxies = proxy, auth = auth, verify = True)

responses = sess.post(url, headers = headers, data = formdata)

print(response.text, response.content, response.url, response.encoding, response.status_code)
```

### lxml
```python
from lxml import etree

text = ```
    <div></div>
    ```
html = etree.HTML(text)

# 获取bookstore下倒数第二个book元素下面href为link.html的a标签,a/@href 获取href属性值
result = html.xpath('/bookstore/book[last()-1]//a[@href = "link.html"]')

results = html.xpath('//div[contains(@id,"qiushi")]')

print(result[0].tag, results[0].text)
```

### jsonpath
```
import json
import jsonpath

# 把json格式字符串转换成python对象
jsonobj = json.loads(html)

result = jsonpath.jsonpath(jsonobj,'$..')
```

XPath	|JSONPath	| 描述
:-      | :-        | :-
/	    |$	        | 根节点
.	    |@	        | 现行节点
/	    |.or[]	    | 取子节点
..	    |n/a	    | 取父节点，Jsonpath未支持
//	    |..	        | 就是不管位置，选择所有符合条件的条件
*	    |*	        | 匹配所有元素节点


### re
```python
import re

pattern = re.compile(r'\d+')
s = "one123two456three789"
a = pattern.match(s,0,9)
#search findall finditer spilt
b = pattern.sub(r'four',s)
```
### 请求报头
```
GET https://www.baidu.com/ HTTP/1.1
Host: www.baidu.comm
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: 
Accept:
Referer:
Accept-Encoding:
Accept-Language:
Accept-Charset:
Cookie:
Content-Type:
```
Content-Type   | 	提交数据方式
:-  | :-
application/x-www-form-urlencoded   |	Form 表单提交
multipart/form-data   |	表单文件上传提交
application/json   |	序列化 Json 数据提交
text/xml   |	XML 数据提交

