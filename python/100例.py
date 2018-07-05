# 1. 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (j !=k) and (i != k):
                print(i, j, k)
'''

# 2. 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
i = int(input('请输入纯利润：'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
fee = 0
for r in range(6):
    if i > arr[r]:
        fee+= (i - arr[r])*rat[r]
        print('部分奖金为：' + str(fee))
        i = arr[r]
print('总奖金为：' + str(fee))

'''

# 4. 输入某年某月某日，判断这一天是这一年的第几天？
'''
year = int(input('请输入年份:'))
month = int(input('请输入月份:'))
day = int(input('请输入第几天:'))
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 1 <= month <= 12 :
    sum = months[month-1] + day
else:
    print('日期输入错误！')
if (year % 400 == 0) or (year % 4 == 0 ) and (year % 100 != 0 ) and (month > 2):
    sum+=1
print('该时间为当年的第' + str(sum) + '天！')

'''

# 5. 输入三个整数x,y,z，请把这三个数由小到大输出
'''
i = input('请输入三个整数x,y,z：').split(',')
list = []
for kw in i:
    list.append(int(kw))
list.sort(reverse = True)
print(list)
'''

# 6. 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
'''
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

print(fib(3))
'''

# 7. 将一个列表的数据复制到另一个列表中
'''
a = [1, 2, 3, 4, 5]
#将a的数据赋值给b 当a的数值发生改变时b不变
#b = a[:]
#浅拷贝：只拷贝第一层，2层以上 都是拷贝元素的地址
#深拷贝：拷贝的内容 不会随原列表list_names内容的更改而更改
b = a.copy()
print(b)
'''

# 8. 输出 9*9 乘法口诀表
'''
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(j) + '*' + str(i) + '=' + str(i*j) + '\t' ,end = '')
    print('\n')
'''

# 9. 暂停一秒输出
'''
import time
 
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1) 
'''

# 10. 暂停一秒输出，并格式化当前时间
'''
import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(2)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

'''

# 13. 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
'''
for i in range(100,1000):
    n = i // 100
    m = (i -n*100) // 10
    k = i -n*100 - m*10
    if i == n**3 + m**3 + k**3:
        print(i)
'''

# 15. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
'''
score = int(input('请输入成绩:'))
if score >= 90:
    print('A')
elif score >= 60 :
    print('B')
else:
    print('C')
'''

# 16. 输出指定格式的日期
'''
import time

print(time.time())
print(time.localtime())
print(time.asctime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) 

import datetime

print(datetime.date.today()) 
print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.date(1941, 1, 5))
'''

# 17. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
'''
import re

kw = input('请输入字符串：')
digit = len(re.findall('\d', kw))
letters = len(re.findall('[a-zA-Z]', kw))
space = len(re.findall('\s', kw))
chin = len(re.findall(r'[\u4E00-\u9FFF]',kw))
others = len(kw) - digit - letters - space - chin

print('数字个数：' + str(digit) + ', 字母个数：' + str(letters) + ', 空格字数：' + str(space) + ', 中文字数：' + str(chin) + ', 其他字符字数：' + str(others))
'''

# 18. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
'''
kw = input("请输入数字以及个数：")

a = kw.split(',')[0]
b = kw.split(',')[1]
s = 0
for i in range(1,int(b)+1):
    s += int(a*i)
print(s)
'''

# 25. 求1+2!+3!+...+20!的和
'''
i = 1
sum = 0
for a in range(1,21):
    i *=a
    sum +=i
print(sum)
'''

# 26. 利用递归方法求5!
'''
def fact(i):
    sum = 0
    if i == 0:
        sum = 1
    else:
        sum = fact(i-1) * i
    return sum

print(fact(5))
'''

# 27. 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
'''
#递归方式
def output(s, l):
    if l == 0:
        return
    print(s[l-1], end = '')
    output(s,l-1)

s =  input('请输入字符串：')
l = len(s)
output(s, l)
#for循环
s =  input('请输入字符串：')
for i in range(len(s)-1, -1, -1):
    print(s[i], end = '')
''' 

# 28. 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
'''
def age(a):
    if a == 1:
        s = 10
    else:
        s = age(a-1)+2
    return s

print(age(5))
'''

# 29. 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
'''
s =  list(input('请输入数字：'))
count = len(s)
print('此为' + str(count) + '位数!')
s.reverse()
for i in range(count):
    print(i, end = '')
'''

# 30. 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
'''
s = input('请输入一串数字：')

flag = True

for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        flag = False
        break
if flag:
    print(s + '是回文数！')
else:
    print(s + '不是回文数！')

#另一种方式
s = input('请输入一串数字：')
a = s[::-1]
if a==s:
    print(s + '是回文数！')
else:
    print(s + '不是回文数！')
'''

# 31. 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
'''
letter = input("please input:")
#while letter  != 'Y':
if letter == 'S':
    print ('please input second letter:')
    letter = input("please input:")
    if letter == 'a':
        print ('Saturday')
    elif letter  == 'u':
        print ('Sunday')
    else:
        print ('data error')
    
elif letter == 'F':
    print ('Friday')
    
elif letter == 'M':
    print ('Monday')
    
elif letter == 'T':
    print ('please input second letter')
    letter = input("please input:")
 
    if letter  == 'u':
        print ('Tuesday')
    elif letter  == 'h':
        print ('Thursday')
    else:
        print ('data error')
        
elif letter == 'W':
    print ('Wednesday')
else:
    print ('data error')
''' 

# 33. 按逗号分隔列表
'''
l = [1,2,3,4,5]
s = ','.join(str(n) for n in l)
print(s)
'''

# 36. 求100之内的素数
'''
for i in range(2, 101):
    if i > 1:
        for m in range(2, i):
            if i%m == 0:
                break       
        else:
            print(i)
'''

# 45. 统计 1 到 100 之和
'''
sum = 0
for i in range(1, 101):
    sum += i
print(sum)
'''

# 46. 求输入数字的平方，如果平方运算后小于 50 则退出
'''
error = 0
again = 1
while again:
    kw = int(input('请输入一个数字：'))
    s = kw*kw
    print(str(kw) + '的平方为：' + str(s))
    if s < 50:
        again = error
'''

# 47. 两个变量值互换
'''
def exchange(a,b):
    a, b = b, a
    return (a,b)

a = 22
b = 33
print(exchange(a,b))
'''

# 50. 输出一个随机数

import random

print(random.random())
print(random.randint(1,100))
print(random.uniform(1,10))
print(random.choice('asdjgsjgl'))