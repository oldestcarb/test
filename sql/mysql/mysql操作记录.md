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
#### 2019-04-23
```
mysqldump -u bmnars -p gene_disease _cs_disease_list > ./_cs_disease_list.sql
mysqldump -u bmnars -p gene_disease  < ./_cs_disease_list.sql

mysqldump -u bmnars -p gene_disease _cs_disease_map > ./_cs_disease_map.sql
mysqldump -u bmnars -p gene_disease _cs_disease_dict > ./_cs_disease_dict.sql

mysql -u bmnars -p gene_disease  < ./_cs_disease_dict.sql
mysql -u bmnars -p gene_disease  < ./_cs_disease_map.sql
mysql -u bmnars -p gene_disease  < ./_cs_disease_list.sql
```
#### 2019-04-24
```
CREATE TABLE `_cs_disease_list_v2` (
  `dis_id` varchar(32) NOT NULL DEFAULT '',
  `parent_id` varchar(32) NOT NULL DEFAULT '',
  `leaf` enum('1','0') DEFAULT '0',
  TreeNumbers varchar(1000),
  ParentTreeNumbers varchar(1000),
  PRIMARY KEY (`dis_id`,`parent_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

create table CTD_diseases_v2(
    DiseaseName varchar(255) primary key,
    DiseaseID varchar(255),
    ParentIDs varchar(2000),
    TreeNumbers varchar(1000),
    ParentTreeNumbers varchar(1000)
);

mysqldump -u bmnars -p gene_disease _cs_disease_dict > ./_cs_disease_dict.sql
mysqldump -u bmnars -p gene_disease _cs_disease_list > ./_cs_disease_list.sql

mysql -u bmnars -p gene_disease  < ./_cs_disease_dict.sql
mysql -u bmnars -p gene_disease  < ./_cs_disease_list.sql
```
#### 2019-04-25
```
mysqldump -u bmnars -p gene_disease _cs_disease_dict > ./_cs_disease_dict.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease _cs_disease_map > ./_cs_disease_map.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease _cs_disease_list > ./_cs_disease_list.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_dict.sql
vi93nwYV
mysql -u bmnars -p gene_disease  < ./_cs_disease_list.sql
vi93nwYV
mysql -u bmnars -p gene_disease  < ./_cs_disease_map.sql
vi93nwYV

drop table `_cs_disease_list`;
drop table `_cs_disease_dict`;
drop table `_cs_disease_map`;

insert ignore into  `disease_all_copy`(name)
SELECT DiseaseName from ctd_diseases_v2;
```
#### 2019-04-26
```
mysqldump -u bmnars -p gene_disease CTD_diseases > ./CTD_diseases.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease disease_ctd_v2 > ./disease_ctd_v2.sql
vi93nwYV
mysql -u bmnars -p gene_disease  < ./CTD_diseases.sql
mysql -u bmnars -p gene_disease  < ./disease_ctd_v2.sql
```
#### 2019-04-28
```
create table _cs_disease_gene_info(
  tax_id int(11),
  GeneID int(11) primary key,
  Symbol varchar(32),
  LocusTag varchar(32),
  Synonyms varchar(255),
  dbXrefs varchar(255),
  chromosome varchar(32),
  map_location varchar(40),
  description varchar(255),
  type_of_gene varchar(32),
  Symbol_from_nomenclature_authority varchar(40),
  Full_name_from_nomenclature_authority varchar(255),
  Nomenclature_status varchar(32),
  Other_designations text,
  Modification_date varchar(32),
  Feature_type text
)

mysqldump -u bmnars -p gene_disease _cs_disease_gene_info > ./_cs_disease_gene_info.sql
vi93nwYV
mysql -u bmnars -p gene_disease  < ./_cs_disease_gene_info.sql
```
#### 2019-04-29
```
create database crispr charset='utf8';
create table equipment(
  id int(11) auto_increment primary key,
  equipment text,
  title varchar(255),
  update_time date
)

create table materials_and_reagents(
  id int(11) auto_increment primary key,
  materials_and_reagents text,
  title varchar(255),
  update_time date
)

grant all privileges on crispr.* to bmnars@localhost;
```

#### 2019-05-07
```
mysqldump -u bmnars -p gene_disease _cs_disease_list > ./_cs_disease_list.sql
vi93nwYV
mysql -u bmnars -p gene_disease  < ./_cs_disease_list.sql
```
#### 2019-05-09
```
mysqldump -u bmnars -p crispr materials_and_reagents > ./materials_and_reagents.sql
vi93nwYV
mysqldump -u bmnars -p crispr equipment > ./equipment.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./materials_and_reagents.sql
mysql -u bmnars -p gene_disease  < ./equipment.sql


CREATE TABLE `aagatlas_list_tmp` (
  `dis_id` varchar(255) NOT NULL DEFAULT '',
  `parent_id` varchar(255) NOT NULL DEFAULT '',
  `leaf` enum('1','0') DEFAULT '0',
  PRIMARY KEY (`dis_id`,`parent_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

mysqldump -u bmnars -p gene_disease _cs_disease_list_all > ./_cs_disease_list_all.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_list_all.sql

CREATE TABLE `aagatlas_list_tmp` (
  `dis_id` varchar(255) NOT NULL DEFAULT '',
  `parent_id` varchar(255) NOT NULL DEFAULT '',
  `leaf` enum('1','0') DEFAULT '0',
	id int(11) primary key auto_increment

) ENGINE=MyISAM DEFAULT CHARSET=utf8;
```
#### 2019-05-13
```
create table pmc_crispr(
  id int(11) auto_increment primary key,
  title varchar(255),
  content text
)

mysqldump -u bmnars -p crispr pmc_crispr > ./pmc_crispr.sql
vi93nwYV
mysql -u bmnars -p gene_disease  < ./pmc_crispr.sql
vi93nwYV

```
#### 2019-05-14
```
create table gene_symbol_correct(
  gene varchar(64) primary key,
  info_geneid int(11) ,
  info_symbol varchar(32),
  info_synonyms varchar(255),
  is_true int(2)
)

alter table gene_symbol_correct change is_true source varchar(32);
update gene_symbol_correct set source = 'symbol' where source ='1';
update gene_symbol_correct set source = 'synonyms' where source ='0';
```

#### 2019-05-15
```
alter table pmc_crispr add abstract text;
alter table pmc_crispr change content content MEDIUMTEXT;

mysqldump -u bmnars -p crispr pmc_crispr > ./pmc_crispr.sql
vi93nwYV
mysql -u bmnars -p gene_disease  < ./pmc_crispr.sql
vi93nwYV

```

#### 2019-05-17
```
mysqldump -u bmnars -p gene_disease _cs_disease_map > ./_cs_disease_map.sql
vi93nwYV
mysql -u bmnars -p gene_disease  < ./_cs_disease_map.sql
vi93nwYV

alter table _cs_disease_map add type int(2);

alter table _cs_disease_map drop primary key;

select distinct dis_id, gene_symbol, gene_id from _cs_disease_map where type =1;
```

#### 2019-05-17
```
mysqldump -u bmnars -p gene_disease _cs_disease_map_1 > ./_cs_disease_map_1.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease _cs_disease_map_2 > ./_cs_disease_map_2.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_map_1.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_map_2.sql
vi93nwYV

mysqldump -u bmnars -p gene_disease _cs_disease_map > ./_cs_disease_map.sql
vi93nwYV
mysql -u bmnars -p gene_disease  < ./_cs_disease_map.sql
vi93nwYV
```

#### 2019-05-24
```
SELECT * FROM `aagatlas_disease` where Disease like   "%systemic lupus erythematosus%";
SELECT * FROM `aagatlas_disease` where Disease like   "%type 1 diabetes mellitus%";

SELECT * FROM `aagatlas_disease` where Disease like   "%Rasmussen encephalitis%";
SELECT * FROM `aagatlas_disease` where Disease like   "%Systemic lupus erythematosus%";
SELECT * FROM `aagatlas_disease` where Disease like   "%Behcet's disease%";
SELECT * FROM `aagatlas_disease` where Disease like   "%Hashimoto's encephalopathy%";
SELECT * FROM `aagatlas_disease` where Disease like   "%Autoimmune limbic encephalitis%";
SELECT * FROM `aagatlas_disease` where Disease like   "%Sydenham's chorea%";


mysqldump -u bmnars -p gene_disease _cs_disease_map > ./_cs_disease_map.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease _cs_disease_dict > ./_cs_disease_dict.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_map.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_dict.sql
vi93nwYV
```

#### 2019-05-28
```
mysqldump -u bmnars -p gene_disease _cs_disease_list > ./_cs_disease_list.sql
vi93nwYV
mysql -u bmnars -p gene_disease  < ./_cs_disease_list.sql
vi93nwYV

CREATE TABLE array_list_new (
  id int(11) AUTO_INCREMENT PRIMARY KEY,
  a varchar(32) ,
  d varchar(32) ,
  gene_symbol varchar(255),
  disease_name varchar(255),
  disease_id varchar(32),
  disease_zh_cn varchar(255)
);
```
#### 2019-05-31
```
CREATE TABLE disease_annotations (
  id int(11) AUTO_INCREMENT PRIMARY KEY,
  Gene_ID varchar(255),
  Gene_Symbol varchar(255),
  Species varchar(255),
  Genetic_Entity_ID varchar(255),
  Genetic_Entity_Symbol varchar(255),
  Genetic_Entity_Type varchar(255),
  Association_Type varchar(255),
  Disease_ID varchar(255),
  Disease_Name varchar(255),
  Evidence_Code varchar(255),
  Source varchar(255),
  Refer text
);

```

#### 2019-06-03
```
mysqldump -u bmnars -p gene_disease _cs_disease_map > ./_cs_disease_map.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease _cs_disease_dict > ./_cs_disease_dict.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease _cs_disease_list > ./_cs_disease_list.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_map.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_dict.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_list.sql
vi93nwYV

mysqldump -u bmnars -p gene_disease disease_annotations > ./disease_annotations.sql
vi93nwYV
mysql -u bmnars -p gene_disease  < ./disease_annotations.sql
vi93nwYV
```
#### 2019-06-12
```
grant all privileges on gene_disease_all.* to bmnars@localhost;

mysqldump -u bmnars -p gene_disease _cs_disease_map > ./_cs_disease_map.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease _cs_disease_dict > ./_cs_disease_dict.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease _cs_disease_list > ./_cs_disease_list.sql
vi93nwYV

mysql -u bmnars -p gene_disease_all  < ./_cs_disease_map.sql
vi93nwYV

mysql -u bmnars -p gene_disease_all  < ./_cs_disease_dict.sql
vi93nwYV

mysql -u bmnars -p gene_disease_all  < ./_cs_disease_list.sql
vi93nwYV

mysqldump -u bmnars -p gene_disease disease_ctd > ./disease_ctd.sql
mysqldump -u bmnars -p gene_disease gd_ctd > ./gd_ctd.sql
mysqldump -u bmnars -p gene_disease gene_primary_ctd > ./gene_primary_ctd.sql

mysql -u bmnars -p gene_disease_all  < ./disease_ctd.sql
vi93nwYV
mysql -u bmnars -p gene_disease_all  < ./gd_ctd.sql
vi93nwYV
mysql -u bmnars -p gene_disease_all  < ./gene_primary_ctd.sql
vi93nwYV

mysqldump -u bmnars -p gene_disease _cs_disease_list_all > ./_cs_disease_list_all.sql
vi93nwYV
mysql -u bmnars -p gene_disease_all  < ./_cs_disease_list_all.sql
vi93nwYV
mysql -u bmnars -p gene_disease_all  < ./_cs_disease_dict_rev1.sql
vi93nwYV


CREATE TABLE _cs_gene (
  `id` varchar(32) NOT NULL DEFAULT '',
  `name` varchar(255) DEFAULT NULL,
  `zh_cn` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
```
#### 2019-06-13
```
create database gene_disease_all charset='utf8';

grant all privileges on gene_disease_all.* to bmnars@'%' IDENTIFIED BY "vi93nwYV";;

GRANT ALL PRIVILEGES ON bmnars.* TO bmnars@"%" IDENTIFIED BY "vi93nwYV";

GRANT ALL PRIVILEGES ON gene_disease.* TO bmnars@"%" IDENTIFIED BY "vi93nwYV";

drop user bmnars@'%';
drop user bmnars@'localhost';
create user bmnars@'%' identified by 'vi93nwYV'
```
#### 2019-06-14
```
mysqldump -u bmnars -p gene_disease_all _cs_disease_map > ./_cs_disease_map.sql

mysql -u bmnars -p gene_disease_all  < ./_cs_disease_map.sql
```

#### 2019-06-17
```
CREATE TABLE array_list_new (
  id int(11) AUTO_INCREMENT PRIMARY KEY,
  a varchar(32) ,
  d varchar(32) ,
  gene_symbol varchar(255),
  disease_name varchar(255),
  disease_id varchar(32),
  disease_zh_cn varchar(255)
);

CREATE TABLE array_list_new_surplus (
  id int(11) AUTO_INCREMENT PRIMARY KEY,
  a varchar(32) ,
  d varchar(32) ,
  gene_symbol varchar(255),
  disease_name varchar(255),
  disease_id varchar(32),
  disease_zh_cn varchar(255)
);

alter table array_list_new_surplus add source varchar(255);


create table aagatlas_result(
    id int(11) AUTO_INCREMENT PRIMARY KEY,
    disease_source varchar(255),
    GeneSymbol varchar(255),
    Disease varchar(255),
    PubMed_ID varchar(255),
    Sentence varchar(5000),
    judge int(2),
    result varchar(255)
);


```
#### 2019-06-18
```
SELECT id, disease_source, GeneSymbol, Disease, PubMed_ID, Sentence FROM `aagatlas_result` where judge =1 and result = "风湿免疫科相关疾病信息检索_右边";

alter table _cs_disease_dict drop primary key;
alter table _cs_disease_dict add primary key(id);

mysqldump -u bmnars -p gene_disease _cs_disease_map_copy_06_03 > ./_cs_disease_map_copy_06_03.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease _cs_disease_list_copy_06_03 > ./_cs_disease_list_copy_06_03.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease _cs_disease_dict_copy_06_03 > ./_cs_disease_dict_copy_06_03.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_map_copy_06_03.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_dict_copy_06_03.sql
vi93nwYV

mysql -u bmnars -p gene_disease  < ./_cs_disease_list_copy_06_03.sql
vi93nwYV

create table pmc_crispr_v2(
  pmc_id int(11)  primary key,
  title varchar(255),
  author text,
  keyword text,
  img_dir varchar(255),
  abstract text
);

mysqldump -u bmnars -p crispr pmc_crispr_v2 > ./pmc_crispr_v2.sql
vi93nwYV

mysql -u bmnars -p crispr  < ./pmc_crispr_v2.sql
vi93nwYV

mysql -u root -p
lwCP1zd6
create database crispr charset='utf8';
grant all privileges on crispr.* to bmnars@'localhost' IDENTIFIED BY "vi93nwYV";
grant all privileges on crispr.* to bmnars@'%' IDENTIFIED BY "vi93nwYV";

```
#### 2019-06-24
```
create table pmc_crispr_v2(
  pmc_id int(11)  primary key,
  title varchar(255),
  author text,
  pub_date varchar(16),
  keyword text,
  img_dir varchar(255),
  abstract text,
  links varchar(255)
);

mysqldump -u bmnars -p crispr pmc_crispr_v2 > ./pmc_crispr_v2.sql
vi93nwYV

mysql -u bmnars -p crispr  < ./pmc_crispr_v2.sql
vi93nwYV
```
#### 2019-06-26
```
CREATE TABLE ctd_infer (
  disease_id varchar(50) NOT NULL ,
  gene_id int(11) NOT NULL
);

CREATE TABLE ctd_infer_12 (

  disease_id varchar(50) NOT NULL ,
  gene_id int(11) NOT NULL
);

CREATE TABLE ctd_infer_36 (

  disease_id varchar(50) NOT NULL ,
  gene_id int(11) NOT NULL,
  primary KEY(disease_id, gene_id)

);
```

#### 2019-06-26
```
create database tiantian charset=utf8;

create user tiantian@'%' identified by 'tiantian';

GRANT ALL PRIVILEGES ON tiantian.* TO 'tiantian'@'%' with grant option;

# 修改加密规则
ALTER USER 'tiantian'@'%' IDENTIFIED BY 'tiantian' PASSWORD EXPIRE NEVER;
# 更新一下用户的密码
ALTER USER 'tiantian'@'%' IDENTIFIED WITH mysql_native_password BY 'tiantian';
# 刷新权限
FLUSH PRIVILEGES;

```
#### 2019-07-04
```

mysqldump -u bmnars -p gene_disease_all _cs_disease_map_millions > ./_cs_disease_map_millions.sql
vi93nwYV


CREATE TABLE array_list_500 (
  a varchar(32) ,
  d varchar(32) ,
  gene_source varchar(32) ,
  gene_symbol varchar(255),
  disease_name varchar(255),
  disease_id varchar(32),
  disease_zh_cn varchar(255),
  primary key(gene_symbol, disease_id)
);
```
#### 2019-07-10
```python
mysqldump -u bmnars -p gene_disease _cs_disease_gene_info > ./_cs_disease_gene_info.sql
vi93nwYV

mysql -u bmnars -p gene_disease_all  < ./_cs_disease_gene_info.sql
vi93nwYV
alter table _cs_gene_compare add info_geneid varchar(255);
alter table _cs_gene_compare add info_symbol varchar(255);
alter table _cs_gene_compare add info_synonyms varchar(255);
alter table _cs_gene_compare add source varchar(255);
```
#### 2019-07-18
```python
create database spider_by_scrapy charset=utf8;
create user scrapy@'%' identified by 'scrapy';
GRANT ALL PRIVILEGES ON spider_by_scrapy.* TO 'scrapy'@'%' with grant option;
create table bcycoser_images(
    id varchar(32) primary key,
    title varchar(255) ,
    url varchar(255)
);

ALTER USER 'scrapy'@'%' IDENTIFIED BY 'scrapy' PASSWORD EXPIRE NEVER;
ALTER USER 'scrapy'@'%' IDENTIFIED WITH mysql_native_password BY 'scrapy';
FLUSH PRIVILEGES;
```
#### 2019-07-19
```python
create database entrez_gene charset=utf8;
GRANT ALL PRIVILEGES ON entrez_gene.* TO 'bmnars'@'%' with grant option;

mysql -h localhost -u root -p  < tables_for_entrezgene.sql
lwCP1zd6
```

#### 2019-07-19
```python
mysqldump -u bmnars -p --databases entrez_gene > entrez_gene.sql


CREATE TABLE `gene_group` (
  `hgnc_id` varchar(50) ,
  `approved_symbol` varchar(50) DEFAULT NULL,
  `approved_name` varchar(250) DEFAULT NULL,
  `previous_symbols` varchar(250) DEFAULT NULL,
  `synonyms` varchar(250) DEFAULT NULL,
  `chromosome` varchar(50) DEFAULT NULL,
  `gene_group` varchar(250) ,
  `root_symbol` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`hgnc_id`,`gene_group`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
```

#### 2019-07-24
```python
mysqldump -u bmnars -p gene_disease gene_group > ./gene_group.sql
vi93nwYV

mysql -u bmnars -p entrez_gene  < ./gene_group.sql
vi93nwYV
```
#### 2019-07-29
```python
CREATE TABLE `pathway_1` (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `doc_1` varchar(250) ,
  `doc_2` varchar(250) ,
  `doc_3` varchar(250),
  `doc_4` varchar(250),
  `doc_5` varchar(250),
  `doc_6` varchar(250) ,
  `doc_7` varchar(250) ,
  `doc_8` text 
) DEFAULT CHARSET=utf8;

CREATE TABLE `pathway_2` (
  `bs_id` varchar(250) ,
  `gene_id` varchar(250) 

) DEFAULT CHARSET=utf8;
```
#### 2019-07-30
```python
alter table pathway_2 add primary key(bs_id,gene_id);

mysqldump -u bmnars -p crispr pathway_2 > ./pathway_2.sql
vi93nwYV

mysql -u bmnars -p entrez_gene  < ./pathway_2.sql
vi93nwYV

alter table gene_group add gene_id int(11) DEFAULT NULL;
alter table gene_group add KEY `gene_group_index` (`gene_id`);
```
#### 2019-07-31
```python
alter table bsid2info drop id;
alter table bsid2info change doc_1 bs_id int(11) primary key;
alter table bsid2info change doc_2 source varchar(50) ;
alter table bsid2info change doc_3 accession varchar(250) ;
alter table bsid2info change doc_4 name varchar(250) ;
alter table bsid2info change doc_5 type_biosystem varchar(50) ;
alter table bsid2info change doc_6 taxonomic_scope varchar(250) ;
alter table bsid2info change tax_id tax_id int(11) ;
alter table bsid2info change doc_8 description text ;

```
#### 2019-08-02
```python
mysqldump -u bmnars -p gene_disease_all _cs_disease_map > ./_cs_disease_map.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease_all _cs_disease_list > ./_cs_disease_list.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease_all _cs_disease_dict > ./_cs_disease_dict.sql
vi93nwYV

mysql -u bmnars -p entrez_gene  < ./_cs_disease_map.sql
vi93nwYV

mysql -u bmnars -p entrez_gene  < ./_cs_disease_dict.sql
vi93nwYV

mysql -u bmnars -p entrez_gene  < ./_cs_disease_list.sql
vi93nwYV
```


#### 2019-08-12
```python
mysqldump -u bmnars -p gene_disease aagatlas_disease > ./aagatlas_disease.sql
vi93nwYV
mysqldump -u bmnars -p gene_disease aagatlas_result > ./aagatlas_result.sql
vi93nwYV

mysql -u bmnars -p gene_disease_all  < ./aagatlas_disease.sql
vi93nwYV

mysql -u bmnars -p gene_disease_all  < ./aagatlas_result.sql
vi93nwYV
```

#### 2019-08-15
```python
# mesh疾病树
create table tree_of_mesh(
    tree_number varchar(100),
    disease_name varchar(250),
    parent_tree_number varchar(100),
    disease_ui varchar(100),
    primary key(tree_number, parent_tree_number)
)DEFAULT CHARSET=utf8;;
```

#### 2019-08-20
```python
# 医生名单
create table doctor(
name varchar(100),
position varchar(100),
professional varchar(100),
hospital varchar(100),
department varchar(100),
primary key(name, hospital)
)DEFAULT CHARSET=utf8;

alter table doctor add mark varchar(100),

```
#### 2019-08-23
```python
# tiantian数据库导出
mysqldump -u tiantian -p tiantian > tiantian.sql
```

#### 2019-08-23
```
# 导入三甲医院名单
mysqldump -u bmnars -p crispr  > ./sanjia.sql
vi93nwYV

mysql -u bmnars -p gene_disease_all  < ./sanjia.sql
vi93nwYV

```
#### 2019-08-20
```
# 官网文章信息
create table gene_article(
title varchar(200) primary key,
content text,
source varchar(100),
pub_date varchar(10)

)DEFAULT CHARSET=utf8;
```

#### 2019-09-03
```
# 博客数据库
create database my_blog charset=utf8;
create user blog@'%' identified by 'blog';
GRANT ALL PRIVILEGES ON my_blog.* TO 'blog'@'%' with grant option;
```

#### 2019-09-06
```
# 全国医院表
create table hospial(
    name varchar(150) primary key,
    province varchar(100),
    city varchar(100),
    grade varchar(100),
    address varchar(255),
    phone varchar(100),
    Summary varchar(255)
);
```