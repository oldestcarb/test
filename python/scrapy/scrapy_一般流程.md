### 一般流程
1. 新建项目
```python
scrapy startproject exosomemed_spider
```
2. 编辑item(`/Exosomemed_spider/items.py`)
```python
# -*- coding: utf-8 -*-

import scrapy


class ExosomemedSpiderItem(scrapy.Item):
    # 文件名字
    file_name = scrapy.Field()
    # 文章爬取结果
    result = scrapy.Field()
```
