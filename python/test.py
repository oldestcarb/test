import requests

url = 'https://www.baidu.com'
kw = {'kw':'baidu'}
formdata = {
    'i','biadu',
    'email','qiu@163.com',
    'pwd','123456'
}
headers = {
    'user-agent':'',
    'connection':'keep-alive'
}
proxy = {
    'http':'http://1.1.1.1:1111',
    'https':'https://2.2.2.2:2222'
}
auth = ('name','password')

sess = requests.session()

response = requests.get(url, params = kw, headers = headers, proxies = proxy, auth = auth, verify = False)
responses = sess.post(url, data = formdata, headers = headers)
print(resposne.text,response.content, response.url, response.encoding, response.status_code)

from lxml import etree

html = etree.HTML(text)

result = html.xpath('bookstore/book[last()-1]//a[@href = "link.html"]')[0].text
# /a/@href 获取href属性值
results = html.xpah('/div[contains(@id, 'qiu')]')[0].text

import json
import jsonpath

jsonobj = json.loads(text)
result = jsonpath.jsonpath(jsonobj,'$..')

import re

pattern = re.compile('\d\w',re.S)
a = 'one123two456three789'
result = pattern.match(a, 0, 9)
# search, findall, finditer, split
results = pattern.sub(r'four', s)

# 请求报头
get https://www.baidu.com/ http/1.1
host: www.baidu.com
connection: keep-alive
upgrade-insecure-requests: 1
user-agent:
accept:
referer:
accept-encoding:
accept-language:
accpet-setchar:
cookie:
content-type:

import json 

items = {}
with open('test.json', 'w', encoding = 'utf-8') as f:
    f.write(json.dumps(items, ident = 2, ensure_ascii = False))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://www.baidu.com")
input = browser.find_element(By.ID, 'q')
list = browser.find_elements(By.CSS_SELECTOR,'service li')
wait = WebDriverWait(browser, 10)
inputs = wait.until(EC.presence_of_element_located(By.ID, 'q'))
input.clear()
input.send_keys('baidu')
input.click()
print(browser.page_source, input.text, input.get_attribute('class'))
# input.id, size, location, tag_name
browser.close()