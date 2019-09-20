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