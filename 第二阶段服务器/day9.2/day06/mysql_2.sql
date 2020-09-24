--练习1
--创建一个数据库 books 使用utf8
create database books charset=utf8;
use books;

--该数据库下创建数据表 book
--id  书名  作者 出版  价格  备注
--字段类型和约束自己设计
create table book(
id int primary key auto_increment,
bname varchar(30) not null,
author varchar(30) not null,
publish varchar(50),
price float,
comment text
);

--在该表中插入若干数据  （>=8条）
--
--价格 --》  30  --120
insert into book (bname,author,publish,price,comment)
values
("边城","沈从文","机械工业出版社",36,"小城故事多"),
("骆驼祥子","老舍","机械工业出版社",48,"你是祥子么"),
("茶馆","老舍","中国文学出版社",55,"老北京"),
("呐喊","鲁迅","中国文学出版社",71,"最后的声音"),
("朝花夕拾","鲁迅","人民教育出版社",49,"好时光"),
("围城","钱钟书","中国文学出版社",63,"你心中的围城是什么");

insert into book (bname,author,publish,price)
values
("林家铺子","茅盾","机械工业出版社",44),
("白鹿原","莫言","人民教育出版社",52);

--基础查找练习1  book表：
--
--1. 查询30多元的图书
select * from book where price >=30 and price < 40;

--2. 查询人民教育出版社出版的图书
select * from book where publish="人民教育出版社";

--3. 查询老舍写的中国文学出版社出版的图书
select * from book where publish="中国文学出版社" and author="老舍";

--4. 查找备注不为 空的
select * from book where comment is not null;

--5. 查找价格超过60的图书，只看书名和价格
select bname,price from book where price > 60;

--6. 查找鲁迅或者茅盾写的图书
select * from book where author="茅盾"  or author="鲁迅";

select * from book where author in ("茅盾","鲁迅");

--alter 操作

alter table hobby drop level;
alter table hobby modify tel char(16);
alter table hobby change tel phone char(16);
alter table class_1 rename cls;

--基础练习2  book表：
--1. 将呐喊的价格修改为45元
update book set price=45 where bname="呐喊";

--2. 增加一个字段出版时间 类型为 date 放在价格后面
alter table book add publish_time date after price;

--3. 修改所有老舍的作品出版时间为 2018-10-1
update book set publish_time="2018-10-1" where author="老舍";

--4. 修改所有中国文学出版社出版的作为 出版时间为
--   2020-1-1  但是不要修改老舍的
update book set publish_time="2020-1-1" where publish="中国文学出版社" and author!="老舍";

--5. 修改所有出版时间为Null的图书 出版时间为
--   2019-10-1
update book set publish_time="2019-10-1" where publish_time is null;

--6. 所有鲁迅的图书价格增加5元
update book set price = price+5 where author="鲁迅";

--7. 删除所有价格超过70元或者不到40元的图书
delete from book where price >70 or price<40;

--高级查询
--找到班级中男生第一名
select * from cls where sex='m' order by score desc limit 1;

--找到班级中男生第三名
--OFFSET 表示跳过前两个，limit 1表示取1个
select * from cls where sex='m' order by score desc limit 1 offset 2;

--高级查询查找练习
--1. 查找所有蜀国人信息，按照攻击力排名
select * from sanguo where country="蜀"
order by attack desc;
--2. 将赵云攻击力设置为360，防御设置为70
update sanguo set attack=360,defense=70
where name="赵云";

--3. 吴国英雄攻击力超过300的改为300，最多改2个
update sanguo set attack=300
where country="吴" and attack>300
limit 2;

--4. 查找攻击力超过200的魏国英雄名字和攻击力并显示
--为姓名， 攻击力

select name as 姓名,attack as 攻击力 from sanguo where country="魏" and attack >200;


--5. 所有英雄按照攻击力降序排序，如果相同则按照防御生序排序
select * from sanguo order by attack desc,defense;

--6. 查找名字为3字的
select * from sanguo where name like "___";

--7. 查找攻击力比魏国最高攻击力的人还要高的蜀国英雄
select * from sanguo
where country="蜀" and attack > (select attack from sanguo where country="魏" order by attack desc limit 1);

--8. 找到魏国防御力排名2-3名的英雄
select * from sanguo where country="魏"
order by defense desc limit 2 offset 1;


--9. 查找所有女性角色中攻击力大于180的和男性
--中攻击力小于250的
select * from sanguo where gender="女" and attack > 180
union
select * from sanguo  where gender="男" and attack < 250;


