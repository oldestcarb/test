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

import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(2)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
