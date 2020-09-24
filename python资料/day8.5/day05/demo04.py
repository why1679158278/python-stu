"""
    列表 -- 基础操作
        定位
        遍历
"""
list_names = ["马伟帅", "秦世杰", "乔海瑞", "钱涛"]
# 定位
# -- 索引：容器名[整数]
# -- 1. 读取
element = list_names[-1]
print(element)
# -- 2. 修改
list_names[-1] = "涛涛"
print(list_names)

# -- 切片:容器名[整数:整数:整数]
# -- 1. 通过切片读取，创建新列表(拷贝)
names = list_names[:3]
print(names)
# -- 2. 通过切片修改，遍历右侧数据,依次存入左侧.
list_names[:3] = ["帅帅帅", "秦秦", "瑞瑞"]
# list_names[:3] = 100 # 因为100不能被for
# list_names[:3] = "孙悟空"
print(list_names)

# 遍历:操作容器每个元素
# -- 方式1： for 元素 in 容器
# 适用性：从头到尾依次读取
for name in list_names:
    print(name)

# -- 方式2：for 索引 in range(开始,结束,间隔):
# 适用性：不能用方式1
# len(list_names) - 1 是 最大索引(总数-1)
# -1 索引可以去到0
# -1 倒序

# 功能：倒序
for i in range(len(list_names) - 1, -1, -1):
    print(list_names[i])

# 功能：修改
for i in range(len(list_names)):
    # 文字长度是3的修改为None
    if len(list_names[i]) == 3:
        list_names[i] = None
