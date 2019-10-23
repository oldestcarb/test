1. 卸载默认安装的mariadb：
```
yum remove mariadb.x86_64
```
2. 获取mysql官方yum源
```
wget https://repo.mysql.com//mysql80-community-release-el7-3.noarch.rpm
```
3. 本地安装yum源
```
yum localinstall mysql80-community-release-el7-3.noarch.rpm
```
4. 使用yum安装
```
yum install mysql-community-server.x86_64
```
5. 启动mysql
```
service mysqld start
```
6. 查找默认登录密码
```
cat /var/log/mysqld.log | grep password
```
7. 登录修改默认密码
```
mysql -u root -p

ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';
```

