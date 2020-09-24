--创建学生表

create table class_1 (
id int primary key auto_increment,
name varchar(20) not null,
age tinyint unsigned,
sex enum('w','m','o'),
score float default 0);


--兴趣爱好表
create table hobby (
id int primary key auto_increment,
name varchar(20) not null,
hobby set('sing','dance','draw'),
level char,
price decimal(7,2),
remark text
);








