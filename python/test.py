from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.baidu.com')
input = browser.find_element(By.ID, 'q')
list = browser.find_elements(By.CSS_SELECTOR, 'class')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located(By.ID, 'q'))
input.clear()
input.send_keys()
input.click()
print(browser.page_source, input.text, input.get_attribute('class'))


import pymysql

db = pymysql.connect(host = 'localhost', user = 'bmnars', password = '123456', port = '3306', db = 'bmnars')
cursor = db.cursor()
data = {
    'id':'2018-8-28',
    'name':'mike',
    'age':'332'
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s']*len(data))
sql = 'insert into {table}({keys}) values ({values}) on duplicate key update'.format(table = table, keys = keys, values =values)
update = ', '.join(['{key} = %s'.format(key = key) where key in data]) + ';'
sql += update
try:
    if cursor.execute(sql,tuple(data.values())*2):
        db.commit()
except:
    db.rollback()
cursor.close()
db.close()

conditions = 'age>2;'
sql = 'delete from {table} where {conditions}'.format(table = table, conditions = conditions)
try:
    if cursor.execute(sql):
        db.commit()
except:
    db.rollback()

sql = 'select * from {table} where {conditions}'.format(table = table, conditions = conditions)
cursor.execute(sql)
try:
    if cursor.execute(sql):
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
except:
    print('error')