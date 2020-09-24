import os

# 获取文件大小 字节
print(os.path.getsize("./my.log"))

# 查看一个文件夹下的内容
print(os.listdir("."))

# 判断一个文件是否存在
print(os.path.exists("./my.log"))

# 查看一个文件是否为普通文件  -
print(os.path.isfile('my.log'))

# 删除文件
os.remove("./my.log")


