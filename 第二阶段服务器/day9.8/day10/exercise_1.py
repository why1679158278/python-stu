"""
创建数据库 dict  使用utf8 编码
create database dict charset=utf8;

数据库下创建一张数据表 words 三个字段
id   word  mean

create table words (id int primary key auto_increment,word varchar(30),mean varchar(256));

将dict.txt中的单词插入数据表中
"""

import pymysql
import re

# 链接数据库 (如果连接本机数据库可以不写host，port)
db = pymysql.connect(
    user = 'root',
    password = '123456',
    database = 'dict',
    charset = 'utf8')

# 创建游标 (游标就是执行sql语句操作数据得到结果的对象)
cur = db.cursor()

data = [] # 存放匹配出的单词

# 数据操作
file = open('dict.txt')

# 每次取一行 一个单词
for line in file:
    one_word = re.findall(r"(\w+)\s+(.*)",line)
    data.append(one_word[0])

# 插入数据库
try:
    sql = "insert into words (word,mean) values (%s,%s);"
    cur.executemany(sql,data)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭
cur.close()
db.close()