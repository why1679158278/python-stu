"""
存储文件本身
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

# 插入二进制数据操作
# with open('timg.jpg','rb') as f:
#     data = f.read()
#
# try:
#     sql = "update cls set image=%s where id=1;"
#     cur.execute(sql,[data])
#     db.commit()
# except:
#     db.rollback()

# 提取文件
sql = "select image from cls where id=1;"
cur.execute(sql)
data = cur.fetchone()[0] # (image,)

with open("小苍.jpg",'wb') as f:
    f.write(data)


# 关闭
cur.close()
db.close()
