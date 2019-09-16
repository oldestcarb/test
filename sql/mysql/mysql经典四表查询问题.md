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

11. 查询至少有一门课与学号为"01"的同学所学相同的同学的信息
```mysql
SELECT distinct s.* from student s, sc where sc.sid= s.sid and sc.cid in (select cid from sc WHERE sc.sid='01') and sc.sid !='01';
```


12. 查询和"01"号的同学学习的课程完全相同的其他同学的信息
```mysql
# TODO: 还未验证过对错，没想明白
select s.* from student s where s.sid in(
select distinct sc.sid from sc where sid<>1 and sc.cid in(
select distinct cid from sc where sid=1
)group by sc.sid having count(1)=(select count(1) from sc where s.sid=1)
);
```

13. 查询没学过"张三"老师讲授的任一门课程的学生姓名
```mysql
select sname from student s WHERE s.sid not in(
SELECT sc.sid from sc, course c, teacher t WHERE t.tname='张三' and c.tid=t.tid and sc.cid = c.cid
);
```

14. 查询出只有两门课程的全部学生的学号和姓名
```mysql
select s.sid, s.sname
from student s, sc
WHERE s.sid=sc.sid
GROUP BY s.sid
HAVING count(sc.cid)=2;
```

15. 查询1990年出生的学生名单
```mysql
select * from student WHERE sage like '%1990%';
```

16. 查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
```mysql
select sc.cid,avg(score) from sc group by sc.cid order by avg(score) DESC , sc.cid;
```

17. 查询任何一门课程成绩在70分以上的姓名、课程名称和分数；
```mysql
select s.sname, c.cname, sc.score from student s, course c, sc
WHERE s.sid=sc.sid and c.cid=sc.cid and sc.score>70;
```

18. 查询平均成绩大于等于85的所有学生的学号、姓名和平均成绩
```mysql
select s.sid, s.sname, avg(sc.score) from student s, sc
where s.sid=sc.sid
GROUP BY s.sid
HAVING avg(sc.score)>=85
```

19. 查询不及格的课程
```mysql
select s.sid, s.sname, c.cname, sc.score from student s, sc , course c
where s.sid=sc.sid and sc.cid=c.cid and sc.score<60;
```

20. 查询课程编号为01且课程成绩在80分以上的学生的学号和姓名；
```mysql
select s.sid, s.sname from student s, sc
where s.sid=sc.sid and sc.score>80 and sc.cid=1;
```

21. 求每门课程的学生人数
```mysql
SELECT sc.cid, count(sc.sid) from sc group by sc.cid;
```

22. 统计每门课程的学生选修人数（超过5人的课程才统计）。要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列
```mysql
select cid,count(sid) from sc group by cid having count(sid)>5 order by count(sid),cid ASC;
```

23. 查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩
```mysql
select s1.sid,s2.sid,sc1.cid,sc1.score,sc2.score
from student s1,student s2,sc sc1,sc sc2
where s1.sid!=s2.sid and s1.sid=sc1.sid and s2.sid=sc2.sid and sc1.cid!=sc2.cid and sc1.score=sc2.score;
```

24. 检索至少选修两门课程的学生学号
```mysql
select sid from sc group by sid having count(cid)>=2;
```

25. 查询选修了全部课程的学生信息
```mysql
select s.* from student s, sc
WHERE s.sid=sc.sid
GROUP BY s.sid
HAVING count(sc.cid) = (select count(*) from course);
```

26. 查询各学生的年龄
```mysql
select s.sname,(TO_DAYS('2017-09-07')-TO_DAYS(s.sage))/365 as age from student s;
```

27. 查询本月过生日的学生
```mysql
SELECT * from student where sage like '%-08-%'
```

28. 查询下月过生日的学生
```mysql
select s.sname from student s where s.sage like '_____08%';
```