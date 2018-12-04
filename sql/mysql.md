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
mysqld --console
1. 删除自己手动创建的data文件夹；
2. mysqld -remove 
3. mysqld --initialize-insecure
    > 会发现程序在mysql的根目录下自动创建了data文件夹以及相关的文件
4. mysqld -install
5. net start mysql

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

#### 日常记录
```mysql

# 创建数据库
create database bmnars charset=utf8;
# 创建表
CREATE TABLE _cs_bmnars_link_v2 (
  source_url varchar(254) UNIQUE KEY,
  local_url varchar(254) ,
  source varchar(254) ,
  update_time date ,
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  status varchar(128) DEFAULT 'N');

create table students(
    id int auto_increment primary key not null,
    name varchar(10) not null,
    gender bit default 1,
    birthday datetime);
    
# 修改表结构
alter table 表名 add|change|drop 列名 类型
alter table students add isdelete bit default 0;

# 插入数据
insert into students values(0,'郭靖',1,'1789-1-1',0);
insert into students(name) values('黄蓉');
insert into students(name) values('杨过'),('小龙女'),('郭襄');

# 更新数据
update students set birthday = '1790-1-2' where id = 2;

# 物理删除
delete from students where id = 5;

# 逻辑删除
update students set isdelete = 1 where id =4;

# 备份
mysqldump -u root -p python3 > d:\bup.sql

# 恢复
mysql -uroot –p 数据库名 < ~/Desktop/备份文件.sql

# 查询
select id,name from students where id <=4;
select distinct gender from students;
# 满足其一即可
select * from students where id >3 or isdelete = 0;
select * from students where id in (1,3,5);
select * from students where id between 3 and 5;
# 聚合
select count(*) from students where isdelete = 1;
select max(id) from students where isdelete =1;
select min(id) from students where isdelete =1;
select sum(id) from students where isdelete =0;
select avg(id) from students where isdelete =0;
# 分组
select isdelete,count(*) from students group by isdelete;
select isdelete,count(*) from students group by isdelete having isdelete = 0;

```