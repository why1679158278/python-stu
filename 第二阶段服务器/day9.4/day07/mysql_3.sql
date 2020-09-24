--练习1 使用book表:
--
--1. 统计每位作家出版图书的平均价格
select author,avg(price)
from book
group by author;

--2. 统计每个出版社出版图书数量
select publish,count(bname)
from book
group by publish;

--3. 查看总共有多少个出版社
select count(distinct publish) as 出版社数量
from book;

--4. 筛选出那些出版过超过50元图书的出版社，并
--按照其出版图书的平均价格降序排序
select publish,avg(price) from book
group by publish
having max(price) > 50
order by avg(price) desc;

--5. 统计同一时间出版图书的最高价格和最低价格
select publish_time,max(price),min(price)
from book
group by publish_time;

--外键，级联动作
alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id)
on delete cascade on update cascade;

alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id)
on delete set null on update set null;


--练习2 ： 根据所学的表关系设计，完成朋友圈内容的
--表设计

--用户表
create table user(
id int primary key auto_increment,
name varchar(50),
passwd char(20)
);

--朋友圈
create table pyq(
id int primary key auto_increment,
image varchar(128),
content text,
user_id int,
foreign key(user_id) references user(id)
);

--点赞评论
create table mylike(
id int primary key auto_increment,
uid int,
pid int,
comment text default null,
lk bit default 0,
foreign key(uid) references user(id),
foreign key(pid) references pyq(id)
);



