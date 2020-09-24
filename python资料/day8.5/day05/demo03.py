"""
    列表list - 基础操作
        创建
        添加
"""
# 创建
# 写法1:列表名 = [数据1,数据2]
# 姓名列表
list_names = ["马伟帅", "秦世杰", "乔海瑞", "钱涛"]
# 年龄列表
list_ages = [26, 23, 25, 16]
# 写法2:列表名 = list(可迭代对象)
list_name = list("孙悟空")
print(list_name)  # ['孙', '悟', '空']

# 添加
# -- 追加:列表名.append(数据)
list_names.append("何泳涛")
# -- 插入: 列表名.insert(索引,数据)
list_names.insert(2, "张天旺")
print(list_names)
