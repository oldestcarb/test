```python
import re
```
1.
```python
# name = 'H00048  Hepatocellular carcinoma'
name = = 'H00048  Hepatocellular carcinoma [PATH:hsa05225 hsa05203 hsa05161 hsa05160 hsa05206]'
# 先匹配再替换
re.sub(r'\[.*\]','',re.search(r'H\d+\s+(.*)', name).group(1))
```
2. 匹配网页源码图片网址
