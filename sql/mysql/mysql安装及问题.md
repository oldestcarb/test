#### win 10 安装mysql
1. 删除
```
net stop mysql
mysqld -remove
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
basedir=D:\program\mysql\mysql-8.0.13-winx64
# 设置mysql数据库的数据的存放目录
datadir=D:\program\mysql\mysqldata
# 允许最大连接数
max_connections=200
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB


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
4. ```mysqld -install```
5. ```net start mysql```

##### 初始设置
```
# root用户密码密码
mysqladmin -u root password root
# 新建用户
create user 'bmnars'@'localhost' identified by 'vi93nwYV';
# 给用户授权
# grant all privileges on 想授权的数据库.* to 'user1'@'%';
# all 可以替换为 select,delete,update,create,drop
grant all privileges on bmnars.* to bmnars@localhost;
```



#### 关于caching-sha2-password问题
root用户登陆
```mysql
ALTER USER 'bmnars'@'localhost' IDENTIFIED BY 'vi93nwYV' PASSWORD EXPIRE NEVER;
ALTER USER 'bmnars'@'localhost' IDENTIFIED WITH mysql_native_password BY 'vi93nwYV';
FLUSH PRIVILEGES;
alter user 'bmnars'@'localhost' identified by 'vi93nwYV';
# 重启mysql服务,mysqld restart
```