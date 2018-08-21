import requests

url = 'https://www.baidu.com'
headers = {
    'user-agent':'',
    'connection':''
}
kw = {
    'kw':'baidu'
}
formdata = {
    'i':'baidu',
    'user':'qiu',
    'pwd':'123456' 
}
proxy = {
    'http':'http://1.1.1.1:1111',
    'https':'https://2.2.2.2:2222'
}
auth = ('qiu','password')
sess = requests.Session()

response = requests.get(url, params = kw, headers = headers, proxies = proxy, auth = auth, verify = False)
resposnes = sess.post(url, data = formdata, headers = headers)

print(response.url, response.text, response.content, response.status_code, response.encoding)


from lxml import etree

html = etree.HTML(content)
response = html.xpath('/bookstore//book[last()-1]//a[@id = "qiu" and contains(@href, "link.html")]')[0].text

import json
import jsonpath

jsonobj = json.laods(html)
response = josnpath.jsonpath(jsonobj, '$..')

with open('./a.json', 'w', encoding = 'utf-8') as f:
    f.write(json.dumps(list, indent = 2, ensure_ascii = False))

import re

pattern = re.compile('\w\d+')
a = '123adcdg323'
b = pattern.search(a)
# match, findall, finditer, spilt
c = re.sub('sdd', a)

get https://www.baidu.com http/1.1

host: www.baidu.com
connection: keep-alive
upgrade-insecure-requests: 1
user-agent:
accept:
referer:
accept-encoding:
accept-language:
accept-charset
cookie:
content-type:



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.baidu.com')
input = browser.find_element(By.ID, 'q')
list = browser.find_elements(By.CSS_SELECTOR, 'li')
wait = WebDriverWait(browser, 10)
inputs = wait.until(EC.presence_of_element_located(By.ID, 'q'))
input.clear()
input.send_keys('baidu')
input.click()
print(browser.page_source, input.text, input.get_attribute('class'))
browser.close()