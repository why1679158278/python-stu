"""
pymysql 读数据库操作 select
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
sql = "select name,age,score from cls;"
cur.execute(sql)

# 执行查询操作后可以cur迭代获取数据
for i in cur:
    print(i)

# # 获取一个结果
# one = cur.fetchone()
# print(one)
#
# # 获取多个
# many = cur.fetchmany(3)
# print(many)
#
# # 所有结果
# all = cur.fetchall()
# print(all)

# 关闭
cur.close()
db.close()
