import requests
import sys
import random

url = 'https:www.baidu.com'
kw = {'kw':'baidu'}
with open(sys.path[0] + '/user-agents.txt', 'r', encoding = 'utf-8') as f:
    list_user_agent = f.readlines()
    user_agent = random.choice(list_user_agent).strip()
headers = {'user-agent':user_agent, cookie:''}
formdata = {
    'i':'fanyi',
    'user':'qiu',
    'pwd':'123456'
}
proxiy = {'http':'http://1.1.1.1:1111','https':'https://2.2.2.2:2222'}
auth = ('qiu','password')
sess = requests.Session()
response = requests.get(url, params = kw, headers = headers, proxies = proxies, auth = auth, verify = False)
responses = sess.post(url, data = formdata, headers = headers)
print(response.text, response.content, response.url, response.status_code, response_encoding)

from lxml import etree

text = etree.HTML(html)
resutl = text.xpath('/bookstore//book[last()-1]//a[contains(@id, "qiu") and @link = "html"]')[0].text
# @href

import json
import jsonpath

wiht open('a.json', 'w', encoding = 'utf-8') as f:
    f.write(json.dumps(list, indent = 2, ensure_ascii = False))
    # json.dump(item, f, ensure_ascii= False)

text = json.loads(thml)
result = jsonpath.jsonpath(text, '$..')

import re

pattern = re.compile(r'\d+', re.S|re.I)
s = 'one123two345sljdg'
a = pattern.match(s, 0, 9)
# search, findall, finditer, split
b = pattern.sub(r'sld', s)

get https://www.baidu.com http/1.1
host www.baidu.com
connection: keep-alive
user-agent:
upgrade-insecure-requests: 1
referer:
accept:
accept-encoding:
accpet-language:
accpet-charset:
content-type:
cookie:

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://www.baidu.com')
wait = browser.implicitly_wait(10)
input = browser.find_element(By.ID, 'qiu')
list = browser.find_elements(By.CSS_SELECTOR, 'service-q')
wait = WebDriverWait(browser, 10)
subb = wait.until(EC.presence_of_element_located((By.ID 'qiu')))
input.clear()
input.send_keys('slgj')
subb.click()
print(browser.page_source, input.get_attribute('cll'), input.text)
browser.close()