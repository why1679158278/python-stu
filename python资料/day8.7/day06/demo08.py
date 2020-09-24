"""
    定位
    删除
"""
dict_ljh = {"name": "李佳豪", "age": 25, "sex": "女"}
# 字典不能使用 索引 切片
# 1. 定位：字典名[键]
# -- 读取
print(dict_ljh["name"])
# 注意：如果没有键则报错
# 解决：读取数据前,通过in判断.
if "money" in dict_ljh:
    print(dict_ljh["money"])
# -- 修改(与添加数据语法相同)
# 具有key为修改,没有key为添加
dict_ljh["money"] = "佳佳"
print(dict_ljh)

# 2. 删除 del 字典名[键]
del dict_ljh["sex"]
print(dict_ljh)