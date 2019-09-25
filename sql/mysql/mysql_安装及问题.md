<!--
 * @Description: In User Settings Edit
 * @Author: your name
 * @Date: 2018-12-03 09:50:12
 * @LastEditTime: 2018-12-03 09:50:12
 * @LastEditors: your name
 -->
#### win 10 安装mysql
1. 删除
```
net stop mysql
mysqld remove
```
2. my.ini(安装目录)
```
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8
[mysqld]
#设置3306端口
port = 3306
# 设置mysql的安装目录
basedir=D:\program\program_database\mysql-8.0.13-winx64
# 设置mysql数据库的数据的存放目录
datadir=D:\program\program_database\mysqldata
# 允许最大连接数
max_connections=200
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
# mysql导入导出数据的路径，空表示任意
secure_file_priv = ''


```
3. 安装（bin目录)
```
mysqld install
net start mysql
```
##### mysql服务无法启动
解决方案：
```
mysqld --console
```
1. 删除自己手动创建的data文件夹；
2. ```mysqld -remove ```
3. ```mysqld --initialize-insecure```
    > 会发现程序在mysql的根目录下自动创建了data文件夹以及相关的文件
4. ```mysqld install```
5. ```net start mysql```

##### 添加环境变量
```
D:\program\program_database\mysql-8.0.13-winx64\bin
```
##### 初始设置
```
# root用户密码密码
mysqladmin -u root password root
# 新建用户
create user 'bmnars'@'localhost' identified by 'vi93nwYV';
# 给用户授权
# grant all privileges on 想授权的数据库.* to 'user1'@'%';
# all 可以替换为 select,delete,update,create,drop
grant all privileges on gene_disease_all.* to bmnars@'%';
grant all privileges on bmnars.* to bmnars@localhost;(仅限本地)
```



1. `关于caching-sha2-password问题`
```mysql
Navicat连接 Mysql 8.0.11 出现1251- Client does not support authentication protocol 错误解决方法一样。
root用户登陆

# 修改加密规则
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root' PASSWORD EXPIRE NEVER;
# 更新一下用户的密码 
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
# 刷新权限
FLUSH PRIVILEGES;
alter user 'root'@'localhost' identified by 'root';
# 重启mysql服务,mysqld restart
```
2. `Incorrect integer value: '' for column 'id' at row 1`
```
mysql 5以上的版本如果是空值应该要写NULL或者0(int类型),或者:
   1. 安装mysql的时候去除默认勾选的enable strict SQL mode
   2. 更改mysql中的配置`my.ini`,重启mysql

   # 默认
    sql-mode="STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"，

    # 修改
    sql-mode="NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"，
```


3. `ERROR 1290 (HY000): The MySQL server is running with the --secure-file-priv option so it cannot execute this statement`
```
mysql默认对导入导出的目录有权限限制，也就是说使用命令行进行导入导出的时候，需要指定目录进行操作；
1. 查询mysql 的secure_file_priv 值配置的是什么

show global variables like '%secure%';  

2. 导入导出的路径选择这个;或者更改mysql中的配置`my.ini`,重启mysql

# 空表示无限制,null表示不允许
secure-file-priv=''

```

4.`mysql时区问题`
> [mysql时区](https://dev.mysql.com/doc/refman/8.0/en/mysql-tzinfo-to-sql.html)