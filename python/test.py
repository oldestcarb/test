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
input = wait.until(EC.presence_of_element_located(By.ID, 'q'))
input.clear()
input.send_keys('baidu')
input.click()
print(browser.page_source, input.text, input.get_attribute('class'))
browser.close()

# mysql

import pymysql

db = pymysql.connect(host='localhost',user='root',password='123456',port=3306.db='bmnars')
cursor = db.cursor()
data = {
    'id':'20180823',
    'name':'qiu',
    'age':21
}
table = 'students'
keys = ', 'join(data.keys())
value = ', 'join(['%s']*len(data))
sql = 'insert into {talbe}({keys}) values ({valuse}) on duplicat key update'.format(table=table, keys = keys, values = values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql,tuple(data.values())*2):
        db.commit()
except:
    db.rollback()
cursor.close()
db.close()

table = 'students'
condition = 'age>2'
sql = 'delete from {table} where {condition};'.format(table=table,condition=condition)

sql = 'select * from students where age>=20;'
try:
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
except:
    print('error')
