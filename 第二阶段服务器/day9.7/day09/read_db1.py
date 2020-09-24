"""
pymysql 读数据库操作 select 2
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

# 查询数据操作
name = input("Name:")
sql = "select name,age,score from cls " \
      "where name=%s or score>%s;"
# print(sql)
# 使用第二个参数列表给sql传入值，不能传入关键字，表名字段名
cur.execute(sql,[name,90])

print(cur.fetchall())


# 关闭
cur.close()
db.close()
