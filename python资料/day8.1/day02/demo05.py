"""
    del - 删除变量
"""
name01 = "悟空"  # 引用计数1
name02 = name01  # 引用计数2
del name01  # 引用计数1
print(name02)  # ?
