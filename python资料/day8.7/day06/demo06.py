"""
    变量交换
        借助第三方
"""
data01 = 10
data02 = 20
# temp = data01
# data01 = data02
# data02 = temp

# 原理：data02和data01存入元组
#      再拆包
data01,data02 = data02, data01

print(data01)
print(data02)