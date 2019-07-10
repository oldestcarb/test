#### No module named 'MySQLdb'
安装mysql包
pip install mysqlclient
pip install pymysql

#### django富文本编辑器tinymce报错
```
TypeError: build_attrs() takes from 1 to 2 positional arguments but 3 were give
```
这是因为tinymce的版本问题
安装特定版本
```
pip install django-tinymce==2.4.0
```