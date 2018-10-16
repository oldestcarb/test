 ###### 创建表
 ```mysql
 CREATE TABLE _cs_bmnars_link_xml (
  source_url varchar(254) UNIQUE KEY,
  local_url varchar(254) ,
  source varchar(254) ,
  update_time date ,
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  status varchar(128) DEFAULT 'N');
```