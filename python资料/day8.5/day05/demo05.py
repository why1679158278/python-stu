"""
    列表 -- 基础操作
        删除
"""
list_names = ["马伟帅", "秦世杰", "乔海瑞", "钱涛"]
# -- 方式1：根据元素删除  列表名.remove(元素)
list_names.remove("乔海瑞")

# -- 方式2：根据定位删除 del 容器名[索引或者切片]
del list_names[0]
del list_names[-2:]
