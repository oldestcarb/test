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
alter table _cs_bmnars_vigenebio_keyword modify status bit not null default 0 ;

drop table _cs_bmnars_vigenebio_result;
alter table _cs_bmnars_vigenebio_keyword add isrun bit not null default 0 ;

alter table _cs_bmnars_vigenebio_kw drop primary key;
alter table _cs_bmnars_vigenebio_kw add id int(11) not null auto_increment primary key;
update _cs_bmnars_vigenebio_kw set isrun=0, status=0;


mysqldump -u bmnars -p bmnars _cs_bmnars_vigenebio_kw > d:\kw.sql
mysqldump -u bmnars -p bmnars _cs_bmnars_vigenebio_rs > d:\rs.sql

source /home/bmnars/spider_porject/vigenebio_spider/kw.sql;
source /home/bmnars/spider_porject/vigenebio_spider/rs.sql;