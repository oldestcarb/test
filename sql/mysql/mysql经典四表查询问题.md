<!--
 * @Description: mysql经典四表联合查询问题
 * @Author: oldestcrab
 * @Github:
 * @Date: 2019-09-16 15:50:25
 * @LastEditors: oldestcrab
 * @LastEditTime: 2019-09-16 17:34:56
 -->
1. 学生表
```mysql
student(s#, sname, sage, ssex)
# 学生编号， 姓名，出生年月，性别
```
2. 课程表
```mysql
course(C#, cname, t#)
# 课程编号， 课程名称， 教师标号
```
3. 教师表
```mysql
teacher(t#, tname)
# 教师编号，姓名
```
4. 成绩表
```mysql
sc(s#, c#, score)
# 学生编号，课程编号， 分数
```

#### 初始化数据库
```mysql
# 新建库
create database student charset='utf8';
# 进入数据库
use student

# 新建学生表
create table student(
sid int primary key auto_increment,
sname varchar(20),
sage date,
ssex enum('男','女'));

# 新建教师表
create table teacher(
tid int primary key auto_increment,
tname varchar(20));

# 新建课程表
create table course(
cid int primary key auto_increment,
cname varchar(20),
tid int,
foreign key(tid) references teacher(tid));

# 新建成绩表
create table sc(
sid int,
cid int,
score int);
```

#### 插入数据库
```mysql
insert into student values(1,'赵雷','1990-01-01','男'),
	(2,'钱电','1990-12-21','男'),
	(3,'孙风','1990-05-20','男'),
	(4,'李云','1990-08-06','男'),
	(5,'周梅','1991-12-01','女'),
	(6,'吴兰','1992-03-01','女'),
	(7,'郑竹','1989-07-01','女'),
	(8,'王菊','1990-01-20','女');

insert into teacher values(1,'张三'),
		(2,'李四'),
		(3,'王五');

insert into course values(1,'语文',2),
			(2,'数学',1),
			(3,'英语',3);
insert into sc values(1,1,90),
			(1,2,80),
			(1,3,90),
			(2,1,70),
			(2,2,60),
			(2,3,80),
			(3,1,80),
			(3,2,80),
			(3,3,80),
			(4,1,50),
			(4,2,30),
			(4,3,20),
			(5,1,76),
			(5,2,87),
			(6,1,31),
			(6,3,34),
			(7,2,89),
			(7,3,98);
```

#### 问题
1. 查询"01"课程比"02"课程成绩高的学生的信息及课程分数
```mysql
SELECT s.*, sc1.score as `课程01`, sc2.score as '课程02' from student  s, sc sc1, sc sc2
WHERE s.sid=sc1.sid and sc1.sid=sc2.sid and sc1.cid=1 and sc2.cid=2 and sc1.score>sc2.score;
```

2. 查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩
```mysql
SELECT s.sid, sname, AVG( score ) FROM student s, sc
WHERE s.sid = sc.sid
GROUP BY s.sid
HAVING AVG( score ) > 60;
```

3. 查询名字中含有"风"字的学生信息
```mysql
select * from student where sname like '%风%';
```

4. 查询课程名称为"数学"，且分数低于60的学生姓名和分数
```mysql
select s.sname, sc.score from student s, course c, sc
where c.cname='数学'  and sc.score<60 and s.sid=sc.sid and c.cid=sc.cid;
```

5. 查询所有学生的课程及分数情况；
```mysql
select s.sname, c.cname, sc.score
FROM student s, course c, sc
WHERE s.sid=sc.sid and c.cid=sc.cid;
```
6. 查询没学过"张三"老师授课的同学的信息
```mysql
select s.* from student s
where s.sid not in(
select sc.sid from sc,course c,teacher t where t.tid=c.tid and sc.cid=c.cid and t.tname='张三'
);
```

7. 查询学过"张三"老师授课的同学的信息
```mysql
select s.*
FROM student s, course c, sc, teacher t
WHERE s.sid=sc.sid and c.cid=sc.cid and c.tid = t.tid and t.tname ='张三';
```

8. 查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息
```mysql
select s.* from
student s,sc sc1,sc sc2
where s.sid=sc1.sid and sc1.sid=sc2.sid and sc1.cid=1 and sc2.cid=2;
```

9. 查询学过编号为"01"但是没有学过编号为"02"的课程的同学的信息
```mysql
select distinct s.*
FROM student s, sc sc1, sc sc2
where s.sid = sc1.sid and sc1.sid=sc2.sid and sc1.cid='01' and sc2.cid !='02';
```

10. 查询没有学全所有课程的同学的信息
```mysql
select s.*
from student s, sc
where s.sid=sc.sid
GROUP BY sc.sid
having count(sc.cid) != (select count(*) from course);
```