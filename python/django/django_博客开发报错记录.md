<!--
 * @Description: 记录django_博客开发报错记录
 * @Author: oldestcrab
 * @Github:
 * @Date: 2019-09-20 10:40:48
 * @LastEditors: oldestcrab
 * @LastEditTime: 2019-09-20 10:43:23
 -->
1.
```python
RuntimeError: Model class django.contrib.sites.models.Site doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
```
```python
# settings 添加应用
INSTALLED_APPS = [
    # 添加sites
    'django.contrib.sites',
```
2. Django使用MySQL后端日期不能按月过滤的问题及解决方案
> [Django使用MySQL后端日期不能按月过滤的问题及解决方案](https://chowyi.com/Django%E4%BD%BF%E7%94%A8MySQL%E5%90%8E%E7%AB%AF%E6%97%A5%E6%9C%9F%E4%B8%8D%E8%83%BD%E6%8C%89%E6%9C%88%E8%BF%87%E6%BB%A4%E7%9A%84%E9%97%AE%E9%A2%98%E5%8F%8A%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88/)
```python
# Django 项目设置了时区为Asia/Shanghai，而数据库中保存的是UTC时间，数据库时间转换出错。

# 解决办法：windows下

# 下载时区包
https://dev.mysql.com/downloads/timezones.html

mysql -u root -p mysql < file_name

# 重启服务
```