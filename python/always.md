#### 去除空格,换行符,制表符
```python
import re
a='I Love\tPy\tthon\n'
b=re.sub('\s','',a)
# \s 表示空白字符：[<空格>\t\r\n\f\v]
# str.replace('\t','').replace('\n','').replace(' ','')   
# strip()
```