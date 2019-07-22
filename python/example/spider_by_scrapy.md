##### mysql
```mysql
# 创建数据库
create database spider_by_scrapy charset=utf8;

# 创建用户
create user scrapy@'%' identified by 'scrapy';

# 数据库授权
GRANT ALL PRIVILEGES ON spider_by_scrapy.* TO 'scrapy'@'%' with grant option;

# 创建表
create table bcycoser_images(
    id varchar(32) primary key,
    title varchar(255) ,
    url varchar(255)
);

# Navicat报错，修改加密规则
ALTER USER 'scrapy'@'%' IDENTIFIED BY 'scrapy' PASSWORD EXPIRE NEVER;
ALTER USER 'scrapy'@'%' IDENTIFIED WITH mysql_native_password BY 'scrapy';
FLUSH PRIVILEGES;

# 第一次导出数据库(已包括创建数据库, 恢复时无需指定数据库)
mysqldump -u scrapy -p --databases spider_by_scrapy > spider_by_scrapy.sql

# 导入数据库
mysql -u scrapy -p < spider_by_scrapy.sql

# 导出某个表
mysqldump -u scrapy -p spider_by_scrapy acfun_follow_update> acfun_follow_update.sql
```
##### mongo
```mongo
# 备份
mongodump -h localhost -d spider_by_scrapy -o ./

# 恢复
mongorestore -h localhost -d spider_by_scrapy --dir spider_by_scrapy
```