"""
pymysql 写操作示例
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

# 写数据操作
# 如果操作的表不支持事务则直接execute后就会生效
# 如果表支持事务则需要 commit 提交才可以
try:
    # 执行多条sql语句 commit 一次即可
    sql = "update cls set score=%s where id=%s;"
    cur.execute(sql,[100,1])
    db.commit() # 提交写操作
except:
    # 取消所有操作
    db.rollback() # 回滚

# 关闭
cur.close()
db.close()
