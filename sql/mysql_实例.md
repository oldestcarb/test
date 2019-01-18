create table _cs_bmnars_vigenebio_kw (
    kw varchar(50) not null ,
    update_time date,
    status bit not null default 0,
    isrun bit not null default 0,
    id int(11) not null auto_increment primary key
);  


create table _cs_bmnars_vigenebio_rs (
    id int(11) not null auto_increment primary key,
    product_no varchar(50),
    gene_no varchar(50),
    detail varchar(255),
    price varchar(50),
    supply_time varchar(50),
    update_time date,
    keyword varchar(50)
);

alter table _cs_bmnars_vigenebio_result add keyword varchar(50);
alter table _cs_bmnars_vigenebio_keyword modify status varchar(5) not null default n ;

drop table _cs_bmnars_vigenebio_result;
alter table _cs_bmnars_vigenebio_keyword add isrun bit not null default 0 ;

alter table _cs_bmnars_vigenebio_kw drop primary key;
alter table _cs_bmnars_vigenebio_kw add id int(11) not null auto_increment primary key;
update _cs_bmnars_vigenebio_kw set isrun=0, status=0;


mysqldump -u bmnars -p bmnars _cs_bmnars_vigenebio_kw > d:\kw.sql
mysqldump -u bmnars -p bmnars _cs_bmnars_vigenebio_rs > d:\rs.sql

source /home/bmnars/spider_porject/vigenebio_spider/kw.sql;
source /home/bmnars/spider_porject/vigenebio_spider/rs.sql;

create table _cs_bmnars_vigenebio_result (
    id int(11) not null auto_increment primary key,
    Catalog_Number varchar(50),
    Gene_Symbol varchar(50),
    Species varchar(50),
    Product_names varchar(50),
    Description varchar(255),
    Price varchar(50),
    Delivery varchar(50),
    update_time date,
    keyword varchar(50)
);

alter table _cs_bmnars_vigenebio_keyword modify status int(5) not null default 0 ;

create table _cs_bmnars_vigenebio_keyword (
    kw varchar(50) not null ,
    update_time date,
    status int(5) not null default 0,
    isrun bit not null default 0,
    id int(5) not null auto_increment primary key
);  

关于caching-sha2-password问题
root用户登陆
ALTER USER 'bmnars'@'localhost' IDENTIFIED BY 'vi93nwYV' PASSWORD EXPIRE NEVER;
ALTER USER 'bmnars'@'localhost' IDENTIFIED WITH mysql_native_password BY 'vi93nwYV';
FLUSH PRIVILEGES;
alter user 'bmnars'@'localhost' identified by 'vi93nwYV';
重启mysql服务,mysqld restart

alter table _cs_bmnars_link_v2 drop id;
alter table _cs_bmnars_link_v2  add primary key(source_url);