#### MySQL日常操作记录


##### 创建数据库
```
create database bmnars charset=utf8;
```
##### 创建表
```
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

CREATE TABLE disease_kegg (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(255) ,
  acronym varchar(50) ,
  parent_name varchar(255) ,
  update_time date);

create table articles (
  id int(11) not null,
  title varchar(255) not null,
  content text,
  date varchar(255),
  wechat varchar(255),
  nickname varchar(255)
);
```    
##### 修改表结构
```
alter table 表名 add|change|drop 列名 类型
alter table students add isdelete bit default 0;
# 修改字段名
ALTER  TABLE gene_synonym_uniprot CHANGE pid primary_id int(11);
```
##### 先添加联合主键,然后添加外键
```
ALTER TABLE gd_uniprot ADD CONSTRAINT pk_re PRIMARY KEY(disease_id, gene_id);
ALTER TABLE gd_uniprot ADD CONSTRAINT fk_dis FOREIGN KEY(disease_id) REFERENCES disease_uniprot(id);
ALTER TABLE gd_uniprot ADD CONSTRAINT fk_ge FOREIGN KEY(gene_id) REFERENCES gene_primary_uniprot(id);

alter table articles add constraint pk_art primary key(id);
```
##### 添加唯一约束
```
ALTER TABLE gene_primary_uniprot ADD unique(name);
ALTER TABLE disease_uniprot ADD unique(name);
```
##### 插入数据
```
insert into students values(0,'郭靖',1,'1789-1-1',0);
insert into students(name) values('黄蓉');
insert into students(name) values('杨过'),('小龙女'),('郭襄');
```
##### 更新数据
```
update students set birthday = '1790-1-2' where id = 2;
```
##### 物理删除
```
delete from students where id = 5;
```
##### 逻辑删除
```
update students set isdelete = 1 where id =4;
```
##### 查询
```
select id,name from students where id <=4;
select * from students where id in (1,3,5);
select * from students where id between 3 and 5;
```
##### 一对多内链接查询
```
select * from gene_synonym_uniprot inner join  gene_primary_uniprot on gene_synonym_uniprot.primary_id = gene_primary_uniprot.id where gene_primary_uniprot.id = 100;
```
##### 多对多内链接查询
```
select disease_uniprot.name,gene_primary_uniprot.name  from gd_uniprot inner join  gene_primary_uniprot on gd_uniprot.gene_id = gene_primary_uniprot.id inner join disease_uniprot on gd_uniprot.disease_id = disease_uniprot.id where gd_uniprot.gene_id = 1587;
# 以disease_id分组并且disease_id对应的gene大于1
select gd_kegg.disease_id,disease_kegg.name  from gd_kegg inner join  gene_primary_kegg on gd_kegg.gene_id = gene_primary_kegg.id inner join disease_kegg on gd_kegg.disease_id = disease_kegg.id group by gd_kegg.disease_id having count(gd_kegg.gene_id)>1;
```
##### 聚合
```
select count(*) from students where isdelete = 1;
select max(id) from students where isdelete =1;
select min(id) from students where isdelete =1;
select sum(id) from students where isdelete =0;
select avg(id) from students where isdelete =0;
```
##### 分组
```
select isdelete,count(*) from students group by isdelete;
select isdelete,count(*) from students group by isdelete having isdelete = 0;
```

##### 备份
```
mysqldump -u root -p python3 > d:\bup.sql
mysqldump -u bmnars -p bmnars _cs_bmnars_vigenebio_rs > d:\rs.sql
```
##### 恢复
```
mysql -uroot –p 数据库名 < ~/Desktop/备份文件.sql
source /home/bmnars/spider_porject/vigenebio_spider/kw.sql;
```
##### 导入csv数据
```
load data infile 'C:/Users/CRAB/Desktop/mim2gene.csv' 
replace into table gene_primary_omim           
fields terminated by ',' 
optionally enclosed by '"' 
lines terminated by '\r\n' 
ignore 1 lines;
```