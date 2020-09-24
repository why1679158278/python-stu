--编写一个存储过程，传入一个学生姓名
--通过外部的用户变量得到这个学生的成绩
create procedure get_score(inout uname varchar(32))
begin
set uname=(select score from cls where name=uname);
end


--编写一个函数，掺入两个学生的ID
--返回两个学生的分数只差
create function score(uid1 int,uid2 int)
returns float
begin
declare u1 float;
declare u2 float;
select score from cls where id=uid1 into u1;
select score from cls where id=uid2 into u2;
return u1-u2;
end $$

