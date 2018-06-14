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
# 获取bookstore下倒数第二个book元素下面href属性值为link.html且id属性值包含"qiu"的a标签,a/@href 获取href属性值
result = html.xpath('/bookstore/book[last()-1]//a[contains(@id,"qiu") and @href = "link.html"]')[0].text

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

pattern = re.compile(r'\d+', re.S, re.I)
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

#### json

json模块提供了四个功能：dumps、dump、loads、load，用于字符串和python数据类型间进行转换。
>- json.loads() 把Json格式==字符串==解码转换成Python对象
>- json.dumps() 实现python类型转化为json==字符串==，返回一个str对象 把一个Python对象编码转换成Json字符串
>- json.dump()  将Python内置类型序列化为json对象后==写入文件==
>- json.load()  读取==文件==中json形式的字符串元素 转化成python类型

python3 默认的是UTF-8格式，但是在用dump写入的时候仍然要注意
>- 在dump的时候要加上ensure_ascii=False,不然会变成ascii码写到文件中,中文字符都会变成 Unicode 字符
>- 另外python3在向txt文件写中文的时候也要注意在打开的时候加上```encoding='utf-8'```，不然也是乱码

写入json数据：
```python
#coding=utf-8
import json

items = {
				"username" : "username",
				"image" :"image",
				"content" : "content",
				"zan" : "zan",
				"comments" : "comments"
			}
			
with open("../result/test.json",'a', encoding = "utf-8") as f:
	f.write(json.dumps(items, ident=2, ensure_ascii = False) + "\n")
    #另一种方式：
    #json.dump(items , f, ensure_ascii = False )
```