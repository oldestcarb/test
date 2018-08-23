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

sess = requests.Session()

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
#search findall finditer split
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

#### selenium

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.baidu.com')
input = browser.find_element(By.ID,'q')
list = browser.find_elemens(By.CSS_SELECTOR,'service-bd li')
wait = WebDriverWait(browser, 10)
inputs = wait.until(EC.presence_of_element_located(By.ID,'q'))
input.clear()
input.send_keys('baidu')
input.click()
print(browser.page_source, input.text, input.get_attribute('class'))
# input.id, size, location, tag_name
browser.close()
```


### mysql

#### 插入和更新|主键不存在便插入数据，存在则更新数据
```python
import pymysql

db = pymysql.connect(host='localhost', user='root',password='123456',port=3306,db='bmnars')
cursor = db.cursor()
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data]) + ';'
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
cursor.close()
db.close()

```
#### 删除和查询
```python
# 删除
table = 'students'
condition = 'age > 20'
sql = 'DELETE FROM  {table} WHERE {condition};'.format(table=table, condition=condition)

# 查询
sql = 'SELECT * FROM students WHERE age >= 20;'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
```




