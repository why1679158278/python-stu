"""
pymysql 写操作示例2 写入多次
"""
import pymysql

# 链接数据库 (如果连接本机数据库可以不写host，port)
db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '123456',
    database = 'stu',
    charset = 'utf8')

# 创建游标 (游标就是执行sql语句操作数据得到结果的对象)
cur = db.cursor()

# 写入多个数据
data_list = [
    ('Dave',17,'m',81),
    ('Ala',16,'w',75),
    ('Levi',18,'m',73),
    ('Sunny',19,'m',62)
]
sql = "insert into cls (name,age,sex,score) " \
      "values (%s,%s,%s,%s);"

try:
    # for i in data_list:
    #     cur.execute(sql,i)
    # 执行多次sql语句 功能同上
    cur.executemany(sql,data_list)
    db.commit()
except:
    db.rollback()


# 关闭
cur.close()
db.close()