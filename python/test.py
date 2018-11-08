import requests
import sys
import random

url = 'https://www.baidu.com'
kw = {'kw':'baidu'}
with open(sys.path[0] + '/user-agent.txt', 'r', encoding = 'utf-8') as f:
    list_agents = f.readlines()
    user_agent = random.choice(list_agents).strip()
headers = {'user-agent':user_agent, 'cookie':''}
formdata = {
    'i':'fanyi',
    'email':'qiu@163.com',
    'pwd':'123456' 
}
proxy = {
    'http':'http://1.1.1.1:1111',
    'https':'https://2.2.2.2:2222'
}
auth = ('name','password')
sess = requests.Session()

response = requests.get(url, headers = headers, params = kw, proxies = proxy, auth = auth, verify = False)
responses = sess.post(url, headers = headers, data = formdata)

print(response.text, response.content, response.url, response.status_code, response.encoding)

from lxml import etree

result = htmll.xpath('/bookstore//book[last()-1]//a[contains(@id, "qiu") and @href = "link.html"]')[0].text
# @href

import json
import jsonpath

jsonobj = json.load(html)
resutl = jsonpath.jsonpath(josnobj,'$..')

import re

pattern = re.compile(r'\d+', re.S|re.I)
s = 'sojglsjlj'
a = pattern.match(s, 0, 9)
# search findall finditer split
b = pattern.sub(r'fousr', s)

get https://www.baidu.com/ http/1.1
host www.baidu.com
connection: keep-alive
upgrade-insecure-requsets: 1
user-agent:
accept:
referer:
accept-encoding:
accept-language:
accept-charset:
cookie:
content-type:

with open('../result/test.json', 'a', encoding = 'utf-8') as f:
    f.write(json.dumps(items, indent= 2, ensure_ascii = False))
    # json.dump(items, f , ensure_ascii = False)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.implicitly_wait(10)
broser.get('https://www.baidu.com')
input = browser.find_element(By.ID, 'q')
list = browser.find_elements(By.CSS_SELECTOR, 'service-bdli')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located(By.ID, 'q'))
input.clear(0)
input.send_keys('baidu')
print(browser.page_source, input.text, input.get_attribute('class'))
browser.close()

import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = '123456', port = 3306, db = 'bmnars')
cursor = db.cursor()
data = {
    'id':'202010',
    'name':'bob',
    'age':21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'insert into {table}({keys} values({values}) on duplicate key update'.format(table = table, keys = keys, values = values)
update = ','.join([" {keys} = %s".format(key = key) for key in data]) + ';'
sql += updata
try:
    if cursor.execute(sql, tuple(data.values())*2):
        db.commit()
except:
    db.rollback()
cursor.close()
db.close()

table = 'students'
condition = 'age>20'
sql = 'delete from {table} where {condition};'.format(table = table, condition = condition)

sql = 'select * from students where age>=20;'
try:
    cursor.execute(sql)
    print('count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('row:', row)
        row = cursor.fetchone()
except:
    print('error')