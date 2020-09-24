"""
    遍历
"""
dict_ljh = {"name": "李佳豪", "age": 25, "sex": "女"}
# 方式1：for 键 in 字典名称
for key in dict_ljh:
    print(key)

# 方式2：for 值 in 字典名称.values()
for value in dict_ljh.values():
    print(value)

# 方式3：for 键,值 in 字典名称.items()
for key,value in dict_ljh.items():
    print(key)
    print(value)

# 数据类型名称(   ... )
#　[('name', '李佳豪'), ('age', 25), ('sex', '女')]
print(list(dict_ljh.items()))