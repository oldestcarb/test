#### 2019-03-25
```
CREATE TABLE disease_kegg (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(255) ,
  acronym varchar(50) ,
  parent_name varchar(255) ,
  update_time date);

CREATE TABLE disease_parent_kegg(
  name varchar(255) PRIMARY KEY,
  parent_name varchar(255) ,
  update_time date);

CREATE TABLE gene_primary_kegg (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(255) ,
  update_time date);

CREATE TABLE gd_kegg (
  disease_id int(11) NOT NULL ,
  gene_id int(11) NOT NULL ,
  update_time date);

ALTER TABLE gene_primary_kegg ADD unique(name);
ALTER TABLE disease_kegg ADD unique(name);

ALTER TABLE gd_kegg ADD CONSTRAINT pk_ke PRIMARY KEY(disease_id, gene_id);
ALTER TABLE gd_kegg ADD CONSTRAINT fk_dis_ke FOREIGN KEY(disease_id) REFERENCES disease_kegg(id);
ALTER TABLE gd_kegg ADD CONSTRAINT fk_ge_ke FOREIGN KEY(gene_id) REFERENCES gene_primary_kegg(id);

ALTER TABLE disease_kegg ADD CONSTRAINT fk_disp_ke FOREIGN KEY(parent_name) REFERENCES disease_parent_kegg(name);

select disease_kegg.id, disease_kegg.name,disease_parent_kegg.name, disease_parent_kegg.parent_name  from disease_kegg inner join disease_parent_kegg on disease_parent_kegg.name = disease_kegg.parent_name where disease_kegg.parent_name ='Head and neck cancers';

select count(*) from  disease_uniprot;
select count(*) from  gene_primary_uniprot;
select count(*) from  gene_synonym_uniprot;
select count(*) from  gd_uniprot;


CREATE TABLE disease_disgenet (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(255) ,
  acronym varchar(50) ,
  parent_name varchar(255) ,
  update_time date);

CREATE TABLE gene_primary_disgenet (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(255) ,
  update_time date);

CREATE TABLE gd_disgenet (
  disease_id int(11) NOT NULL ,
  gene_id int(11) NOT NULL ,
  update_time date);

ALTER TABLE gene_primary_disgenet ADD unique(name);
ALTER TABLE disease_disgenet ADD unique(name);

ALTER TABLE gd_disgenet ADD CONSTRAINT pk_disg PRIMARY KEY(disease_id, gene_id);
ALTER TABLE gd_disgenet ADD CONSTRAINT fk_dis_disg FOREIGN KEY(disease_id) REFERENCES disease_disgenet(id);
ALTER TABLE gd_disgenet ADD CONSTRAINT fk_ge_disg FOREIGN KEY(gene_id) REFERENCES gene_primary_disgenet(id);
```

#### 2019-03-28
```

CREATE TABLE disease_ctd (
  id varchar(50)  NOT NULL PRIMARY KEY,
  name varchar(255) ,
  acronym varchar(50) ,
  parent_name varchar(255) ,
  update_time date);

CREATE TABLE gene_primary_ctd (
  id int(11) NOT NULL PRIMARY KEY,
  name varchar(255) ,
  update_time date);

CREATE TABLE gd_ctd (
  disease_id varchar(50) NOT NULL ,
  gene_id int(11) NOT NULL ,
  update_time date);

ALTER TABLE gene_primary_ctd ADD unique(name);
ALTER TABLE disease_ctd ADD unique(name);

ALTER TABLE gd_ctd ADD CONSTRAINT pk_ctd PRIMARY KEY(disease_id, gene_id);
ALTER TABLE gd_ctd ADD CONSTRAINT fk_dis_ctd FOREIGN KEY(disease_id) REFERENCES disease_ctd(id);
ALTER TABLE gd_ctd ADD CONSTRAINT fk_ge_ctd FOREIGN KEY(gene_id) REFERENCES gene_primary_ctd(id);
```

#### 2019-03-29
```
CREATE TABLE disease_curated_disgenet (
  id varchar(50)  NOT NULL PRIMARY KEY,
  name varchar(255) ,
  acronym varchar(50) ,
  parent_name varchar(255) ,
  update_time date);

CREATE TABLE gene_primary_curated_disgenet (
  id int(11) NOT NULL PRIMARY KEY,
  name varchar(255) ,
  update_time date);

CREATE TABLE gd_curated_disgenet (
  disease_id varchar(50) NOT NULL ,
  gene_id int(11) NOT NULL ,
  update_time date);

ALTER TABLE gene_primary_curated_disgenet ADD unique(name);
ALTER TABLE disease_curated_disgenet ADD unique(name);

ALTER TABLE gd_curated_disgenet ADD CONSTRAINT pk_curated_disgenet PRIMARY KEY(disease_id, gene_id);
ALTER TABLE gd_curated_disgenet ADD CONSTRAINT fk_dis_curated_disgenet FOREIGN KEY(disease_id) REFERENCES disease_curated_disgenet(id);
ALTER TABLE gd_curated_disgenet ADD CONSTRAINT fk_ge_curated_disgenet FOREIGN KEY(gene_id) REFERENCES gene_primary_curated_disgenet(id);


CREATE TABLE gene_primary_omim (
  mim_id int(11) PRIMARY KEY,
  entrez_gene_id int(11),
  name varchar(255),
  ensembl_gene_id varchar(50),
  update_time date);


load data infile 'C:/Users/CRAB/Desktop/mim2gene.csv' 
replace into table gene_primary_omim           
fields terminated by ',' 
optionally enclosed by '"' 
lines terminated by '\r\n' 
ignore 1 lines;

insert into gene_primary_omim values('11120360', '', '', 'NULL', '2019-03-29')
select * from gene_primary_omim where mim_id = 11120360;
```

#### 2019-04-03
```

SELECT * FROM `disease_ctd` where name like "%breast%";
SELECT * FROM `disease_curated_disgenet` where name like "%breast%";
SELECT * FROM `disease_disgenet` where name like "%breast%";
SELECT * FROM `disease_kegg` where name like "%breast%";
SELECT * FROM `disease_uniprot` where name like "%breast%";

select gene_primary_kegg.id as gene_id, gene_primary_kegg.name as gene_name , disease_kegg.name as disease_name from gd_kegg inner join disease_kegg on disease_kegg.id = gd_kegg.disease_id INNER JOIN gene_primary_kegg on gene_primary_kegg.id = gd_kegg.gene_id where disease_kegg.name='Breast cancer';
select gene_primary_ctd.id as gene_id, gene_primary_ctd.name as gene_name  , disease_ctd.name as disease_name from gd_ctd inner join disease_ctd on disease_ctd.id = gd_ctd.disease_id INNER JOIN gene_primary_ctd on gene_primary_ctd.id = gd_ctd.gene_id where disease_ctd.name='Breast cancer';
select gene_primary_curated_disgenet.id as gene_id, gene_primary_curated_disgenet.name as gene_name  , disease_curated_disgenet.name as disease_name from gd_curated_disgenet inner join disease_curated_disgenet on disease_curated_disgenet.id = gd_curated_disgenet.disease_id INNER JOIN gene_primary_curated_disgenet on gene_primary_curated_disgenet.id = gd_curated_disgenet.gene_id where disease_curated_disgenet.name='Breast cancer';
select gene_primary_uniprot.id as gene_id, gene_primary_uniprot.name as gene_name  , disease_uniprot.name as disease_name from gd_uniprot inner join disease_uniprot on disease_uniprot.id = gd_uniprot.disease_id INNER JOIN gene_primary_uniprot on gene_primary_uniprot.id = gd_uniprot.gene_id where disease_uniprot.name='Breas cancert';

select gene_primary_kegg.id as gene_id, gene_primary_kegg.name as gene_name , disease_kegg.name as disease_name from gd_kegg inner join disease_kegg on disease_kegg.id = gd_kegg.disease_id INNER JOIN gene_primary_kegg on gene_primary_kegg.id = gd_kegg.gene_id where disease_kegg.name like '%Breast%' ;
select gene_primary_ctd.id as gene_id, gene_primary_ctd.name as gene_name  , disease_ctd.name as disease_name from gd_ctd inner join disease_ctd on disease_ctd.id = gd_ctd.disease_id INNER JOIN gene_primary_ctd on gene_primary_ctd.id = gd_ctd.gene_id where disease_ctd.name like '%Breast%';
select gene_primary_curated_disgenet.id as gene_id, gene_primary_curated_disgenet.name as gene_name  , disease_curated_disgenet.name as disease_name from gd_curated_disgenet inner join disease_curated_disgenet on disease_curated_disgenet.id = gd_curated_disgenet.disease_id INNER JOIN gene_primary_curated_disgenet on gene_primary_curated_disgenet.id = gd_curated_disgenet.gene_id where disease_curated_disgenet.name like '%Breast%';
select gene_primary_uniprot.id as gene_id, gene_primary_uniprot.name as gene_name  , disease_uniprot.name as disease_name from gd_uniprot inner join disease_uniprot on disease_uniprot.id = gd_uniprot.disease_id INNER JOIN gene_primary_uniprot on gene_primary_uniprot.id = gd_uniprot.gene_id where disease_uniprot.name='Breas cancert';

select count(gene_primary_kegg.id) as gene_count, disease_kegg.name as disease_name from gd_kegg inner join disease_kegg on disease_kegg.id = gd_kegg.disease_id INNER JOIN gene_primary_kegg on gene_primary_kegg.id = gd_kegg.gene_id where disease_kegg.name like '%Breast%' group by disease_kegg.name;
select count(gene_primary_ctd.id) as gene_count, disease_ctd.name as disease_name from gd_ctd inner join disease_ctd on disease_ctd.id = gd_ctd.disease_id INNER JOIN gene_primary_ctd on gene_primary_ctd.id = gd_ctd.gene_id where disease_ctd.name like '%Breast%' group by disease_ctd.name;
select count(gene_primary_curated_disgenet.id) as gene_count, disease_curated_disgenet.name as disease_name from gd_curated_disgenet inner join disease_curated_disgenet on disease_curated_disgenet.id = gd_curated_disgenet.disease_id INNER JOIN gene_primary_curated_disgenet on gene_primary_curated_disgenet.id = gd_curated_disgenet.gene_id where disease_curated_disgenet.name like '%Breast%' group by curated_disgenet.name;;
select count(gene_primary_uniprot.id) as gene_count,disease_uniprot.name as disease_name from gd_uniprot inner join disease_uniprot on disease_uniprot.id = gd_uniprot.disease_id INNER JOIN gene_primary_uniprot on gene_primary_uniprot.id = gd_uniprot.gene_id where disease_uniprot.name='Breas cancert' group by disease_uniprot.name;
```

#### 2019-04-08
```
CREATE TABLE scan_website (
  url varchar(255) PRIMARY KEY,
  code int(11),
  is_parse int(2),
  update_time date);


create user 'bmnars'@'localhost' identified by 'vi93nwYV';
grant all privileges on bmnars.* to bmnars@localhost;

ALTER USER 'bmnars'@'localhost' IDENTIFIED BY 'vi93nwYV' PASSWORD EXPIRE NEVER;
ALTER USER 'bmnars'@'localhost' IDENTIFIED WITH mysql_native_password BY 'vi93nwYV';
FLUSH PRIVILEGES;
alter user 'bmnars'@'localhost' identified by 'vi93nwYV';
mysqld restart
```

#### 2019-04-09
```
alter table scan_website add response_url varchar(255) ;
alter table scan_website add redirect_code int(11);


CREATE TABLE disease_ctd_v2 (
  id varchar(50)  NOT NULL PRIMARY KEY,
  name varchar(255) ,
  acronym varchar(50) ,
  parent_name varchar(255) ,
  directevidence varchar(50),
  update_time date);

CREATE TABLE gene_primary_ctd_v2 (
  id int(11) NOT NULL PRIMARY KEY,
  name varchar(255) ,
  directevidence varchar(50),
  update_time date);

CREATE TABLE gd_ctd_v2 (
  disease_id varchar(50) NOT NULL ,
  gene_id int(11) NOT NULL ,
  directevidence varchar(50),
  update_time date);

ALTER TABLE gene_primary_ctd_v2 ADD unique(name);
ALTER TABLE disease_ctd_v2 ADD unique(name);

ALTER TABLE gd_ctd_v2 ADD CONSTRAINT pk_ctd PRIMARY KEY(disease_id, gene_id);
ALTER TABLE gd_ctd_v2 ADD CONSTRAINT fk_dis_ctd_v2 FOREIGN KEY(disease_id) REFERENCES disease_ctd_v2(id);
ALTER TABLE gd_ctd_v2 ADD CONSTRAINT fk_ge_ctd_v2 FOREIGN KEY(gene_id) REFERENCES gene_primary_ctd_v2(id);

ALTER TABLE gd_ctd_v2 DROP DirectEvidence;
ALTER TABLE disease_ctd_v2 DROP DirectEvidence;
ALTER TABLE gene_primary_ctd_v2 DROP DirectEvidence;

ALTER TABLE gd_ctd_v2 add directevidence varchar(50);
ALTER TABLE disease_ctd_v2 add directevidence varchar(50);
ALTER TABLE gene_primary_ctd_v2 add directevidence varchar(50);
```

#### 2019-04-09
```
CREATE TABLE scan_website_v2 (
  url varchar(255) PRIMARY KEY,
  code int(11),
  redirect_code int(11),
  redirect_url varchar(255),
  is_parse int(2),
  update_time date);
```
#### 2019-04-12
```
CREATE TABLE scan_website_v3 (
  url varchar(255) PRIMARY KEY,
  code int(11),
  response_url varchar(255),
  update_time date);
```
#### 2019-04-14
```
select count(*) from gene_primary_uniprot;
select count(*) from gene_primary_ctd_v2;
select count(*) from gene_primary_omim;
select count(*) from gene_primary_curated_disgenet;
select count(*) from gene_primary_kegg;

create table gene_all(
  id int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  name varchar(255),
  update_time date
);

alter table gene_all add unique(name);

insert ignore into gene_all(name, '2019-04-15') select name from gene_primary_ctd_v2;

insert ignore into gene_all(name) select name from gene_primary_uniprot;


CREATE TABLE disease_all (
  id int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  mesh_id varchar(50) ,
  name varchar(255) ,
  acronym varchar(50) ,
  parent varchar(255) ,
  update_time date);
alter table disease_all add unique(name);

insert ignore into disease_all(mesh_id, name, acronym, parent) 
select id, name, acronym, parent_name
from disease_ctd_v2;
```

#### 2019-04-16
```
alter table disease_all add source VARCHAR(20);

create table gene_all_v2(
  id int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  name varchar(255),
  update_time date,
  source VARCHAR(20)
);

alter table gene_all_v2 add unique(name);

update gene_all set update_time='2019-04-16';
update disease_all set update_time='2019-04-16';  

INSERT into disease_all(mesh_id, NAME) 
select id,name from disease_ctd_v2 on duplicate key update mesh_id = disease_ctd_v2.id;
```

#### 2019-04-17
```
create table aagatlas_disease(
    GeneSymbol varchar(255),
    Disease varchar(255),
    PubMed_ID varchar(255),
    Sentence varchar(5000),
    update_time date
);

```
#### 2019-04-18
```
create table aagatlas_disease_v2(
    GeneSymbol varchar(255),
    Disease varchar(255),
    PubMed_ID varchar(255),
    Sentence varchar(5000),
    update_time date
);

create table aagatlas_gene(
    GeneSymbol varchar(255),
    Disease varchar(255),
    PubMed_ID varchar(255),
    Sentence varchar(5000),
    update_time date
);

```
#### 2019-04-19
```
alter table  `aagatlas_disease_v2`  RENAME aagatlas_disease;

INSERT into _cs_disease_dict(id, name, alias)
SELECT id, name, acronym FROM `disease_all`;

alter table `aagatlas_disease` add id int(11) not null auto_increment primary key;
alter table `aagatlas_gene` add id int(11) not null auto_increment primary key;
```
#### 2019-04-22
```
insert into _cs_disease_map(dis_id, gene_symbol) VALUES('2857', "A1BG")  on DUPLICATE key update source = CONCAT(source, ',abc');

update _cs_disease_map set source = 'ctd' where source = 'ctd ,ctd';

mysqldump -u bmnars -p gene_disease gene_primary_curated_disgenet > ./gene_primary_curated_disgenet.sql
mysqldump -u bmnars -p gene_disease disease_curated_disgenet > ./disease_curated_disgenet.sql
mysqldump -u bmnars -p gene_disease gd_curated_disgenet > ./gd_curated_disgenet.sql

mysql -u bmnars -p gene_disease < ./gene_primary_curated_disgenet.sql
mysql -u bmnars -p gene_disease < ./gd_curated_disgenet.sql
mysql -u bmnars -p gene_disease < ./disease_curated_disgenet.sql

mysqldump -u bmnars -p gene_disease _cs_disease_dict > ./_cs_disease_dict.sql
mysqldump -u bmnars -p gene_disease gene_all > ./gene_all.sql

create table CTD_diseases(
    DiseaseName varchar(255) primary key,
    DiseaseID varchar(255),
    ParentIDs varchar(2000)
);
```