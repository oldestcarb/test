### requests
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

print(response.text,response.content, response.url, response.encoding, response.status_code)


### lxml
form lxml import etree
# / // . .. @

text = ```
    <div></div>
```
html = etree.HTML(text)

# 获取bookstore下倒数第二个book元素下面href为link.html的a标签,a/@href 获取href属性值
result = html.xpath('/bookstore/book[last()-1]//a[@href = "link.html"]')

results = html.xpath('//div[contains(@id,"qiushi")]')

print(result[0].tag, results[0].text)